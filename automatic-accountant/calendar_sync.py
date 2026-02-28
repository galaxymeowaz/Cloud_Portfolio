import os
import json
import datetime
import re
from googleapiclient.discovery import build
from google.oauth2 import service_account
import gspread

# Environment Variables Configuration
HOURLY_RATE = int(os.environ.get('HOURLY_RATE', 150))
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEETS_SPREADSHEET_ID')
CALENDAR_ID = os.environ.get('CALENDAR_ID', 'primary')
SYNC_DAYS_BACK = int(os.environ.get('SYNC_DAYS_BACK', 1))

def get_credentials():
    """
    Load Service Account Credentials.
    In AWS Lambda, using a secure secrets manager is best, but for Free Tier
    we assume deploying a credentials.json file or loading via ENV JSON block.
    """
    scopes = [
        'https://www.googleapis.com/auth/calendar.readonly',
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    if os.path.exists('credentials.json'):
        return service_account.Credentials.from_service_account_file('credentials.json', scopes=scopes)
    return None

def lambda_handler(event, context):
    try:
        print("--- LEDGER SYNC INITIATED ---")
        creds = get_credentials()
        if not creds:
            print("ERROR: credentials.json missing. Ensure it's bundled in the Docker image securely or loaded via Secrets Manager.")
            return {"statusCode": 500, "body": "Missing Google Auth Credentials"}

        # 1. Fetch Calendar Events (Targeting the past N days)
        cal_service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        past_time = (datetime.datetime.utcnow() - datetime.timedelta(days=SYNC_DAYS_BACK)).isoformat() + 'Z'
        
        print(f"Scanning Calendar: {CALENDAR_ID} for the past {SYNC_DAYS_BACK} days...")
        
        events_result = cal_service.events().list(
            calendarId=CALENDAR_ID, timeMin=past_time, timeMax=now,
            singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        
        if not events:
            print(f"No meetings found in the last {SYNC_DAYS_BACK} days.")
            return {"statusCode": 200, "body": json.dumps("No meetings found.")}

        # 2. Append to Google Sheets
        gc = gspread.authorize(creds)
        sheet = gc.open_by_key(SPREADSHEET_ID).sheet1
        
        rows_to_append = []
        for event in events:
            start_str = event['start'].get('dateTime')
            end_str = event['end'].get('dateTime')
            
            # Skip all-day events (they only have 'date', not 'dateTime')
            if start_str and end_str:
                start = datetime.datetime.fromisoformat(start_str.replace('Z', '+00:00'))
                end = datetime.datetime.fromisoformat(end_str.replace('Z', '+00:00'))
                duration_hours = (end - start).total_seconds() / 3600
                
                # Assume title format "Client Name" or "Client Name [$250]"
                raw_title = event.get('summary', 'Unknown Client').strip()
                
                # Regex to search for custom rates like "$150", "[150]", "@150", or "($150)" in the title
                rate_match = re.search(r'[\$\[\@\(]\s*(\d+(?:\.\d+)?)\s*[\]\)]?', raw_title)
                
                if rate_match:
                    client_rate = float(rate_match.group(1))
                    # Clean the client name by removing the rate section
                    client = raw_title.replace(rate_match.group(0), '').split('-')[0].strip()
                else:
                    client_rate = HOURLY_RATE
                    client = raw_title.split('-')[0].strip()
                    
                amount_owed = duration_hours * client_rate
                
                row = [
                    start.strftime("%Y-%m-%d"),       # [A] Event Date
                    client,                           # [B] Client
                    "Consulting / Meeting",           # [C] Service
                    f"${amount_owed:.2f}",             # [D] Amount Owed
                    "UNPAID",                         # [E] Status
                    "",                               # [F] Payment Received Date
                    ""                                # [G] Comments (Manual Entry)
                ]
                rows_to_append.append(row)
                print(f"Prepared bill for {client}: ${amount_owed:.2f}")

        if rows_to_append:
            # Batch append for API efficiency
            sheet.append_rows(rows_to_append)
            print(f"Successfully appended {len(rows_to_append)} rows to the Ledger.")

        return {
            'statusCode': 200,
            'body': json.dumps('Ledger Sync Complete!')
        }
        
    except Exception as e:
        print(f"System Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }

if __name__ == "__main__":
    # Local Docker test stub
    print("Testing locally...")
    lambda_handler({}, {})