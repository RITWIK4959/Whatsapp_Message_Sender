from twilio.rest import Client
from datetime import datetime
import time

# Twilio credentials (keep them safe, don’t hardcode in production!)
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_address, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+xxxxxxxxxxx',   # Twilio sandbox WhatsApp number
            body=message_body,
            to=f'whatsapp:{recipient_address}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

# User inputs
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +91XXXXXXXXXX): ')
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Parse datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    # Wait until scheduled time
    time.sleep(delay_seconds)

    # Send message
    send_whatsapp_message(recipient_number, message_body)
