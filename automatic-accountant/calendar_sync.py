import os
import json

# This is the "Main Brain" of the robot
def lambda_handler(event, context):
    # 1. Try to get the secrets from the Environment (Docker/AWS)
    # The .get() method prevents crashing if the key is missing
    cal_id = os.environ.get('CALENDAR_ID', 'MISSING_CALENDAR_ID')
    sheet_id = os.environ.get('SHEET_ID', 'MISSING_SHEET_ID')

    # 2. Print the status (This is what you will see in the terminal)
    print(f"--- ROBOT REPORT ---")
    print(f"Status: Waking Up...")
    print(f"Target Calendar: {cal_id}")
    print(f"Target Sheet: {sheet_id}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sync Complete!')
    }

# This block allows the script to run LOCALLY (on your laptop/Docker)
# AWS ignores this, but Docker uses it.
if __name__ == "__main__":
    # Create fake data so the function doesn't crash
    fake_event = {}
    fake_context = {}
    
    print("Starting Docker Test...")
    # Manually trigger the function
    lambda_handler(fake_event, fake_context)
    print("Docker Test Finished.")