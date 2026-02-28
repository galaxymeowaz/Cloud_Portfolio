# ==============================================================================
# Automatic Accountant Pipeline
# Created by AzTay (aztay.org) | Copyright (c) 2026
# Unauthorized copying, modification, or distribution is strictly prohibited.
# ==============================================================================
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
        print("==================================================")
        print(" AUTOMATIC ACCOUNTANT PIPELINE ")
        print(" Created by AzTay (aztay.org) ")
        print("==================================================")
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

        # 2. Fetch Existing Sheet Data for Deduplication
        gc = gspread.authorize(creds)
        sheet = gc.open_by_key(SPREADSHEET_ID).sheet1
        existing_records = sheet.get_all_values()
        
        # Build a set of existing signatures to prevent duplicate entries (Signature: "Date_Client")
        existing_signatures = set()
        for row in existing_records[1:]: # Skip header
            if len(row) >= 2:
                existing_signatures.add(f"{row[0]}_{row[1]}")
        
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
                
                # Regex to search for custom rates like "$150", "[$150]", "@150", or "($150)" in the title
                rate_match = re.search(r'[\$\[\@\(]\s*[\$\@]?\s*(\d+(?:\.\d+)?)\s*[\]\)]?', raw_title)
                
                # Clean the title of rates
                if rate_match:
                    client_rate = float(rate_match.group(1))
                    # Remove the exact rate string from the title
                    clean_title = raw_title.replace(rate_match.group(0), '')
                else:
                    client_rate = HOURLY_RATE
                    clean_title = raw_title
                    
                # Clean up any messy double spaces left over before parsing the hyphen
                clean_title = re.sub(r'\s+', ' ', clean_title).strip()
                    
                # Dynamically parse the "Service" if a hyphen is used (e.g., "Client - Web Design")
                if '-' in clean_title:
                    client = clean_title.split('-', 1)[0].strip()
                    service_name = clean_title.split('-', 1)[1].strip()
                else:
                    client = clean_title.strip()
                    service_name = "Consulting / Meeting"
                    
                amount_owed = duration_hours * client_rate
                
                # Format Date to include the specific times: YYYY-MM-DD (01:00 PM - 03:00 PM)
                time_format = f"{start.strftime('%Y-%m-%d')} ({start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')})"
                
                # Check Deduplication Signature
                signature = f"{time_format}_{client}"
                if signature in existing_signatures:
                    print(f"Skipping Duplicate: {signature}")
                    continue
                
                row = [
                    time_format,                      # [A] Event Date & Time
                    client,                           # [B] Client
                    service_name,                     # [C] Service
                    f"${amount_owed:.2f}",             # [D] Amount Owed
                    "UNPAID",                         # [E] Status
                    "",                               # [F] Payment Received Date
                    ""                                # [G] Comments (Manual Entry)
                ]
                rows_to_append.append(row)
                existing_signatures.add(signature) # Prevent intra-batch duplicates
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