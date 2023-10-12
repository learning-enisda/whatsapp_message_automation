import pandas as pd
import pywhatkit as kit
from datetime import datetime

# Load your dataset (assuming it's a CSV file)
df = pd.read_csv('/home/libra/PycharmProjects/pythonProject/data/your_dataset.csv')

# Define a dictionary to keep track of which numbers have already received a message
sent_messages = {}

# Iterate through the dataset
for index, row in df.iterrows():
    name = row['Name']
    message = row['Message']

    # Add the country code to the number (e.g., +1 for the United States)
    country_code = '+62'  # Modify this according to your needs
    number = country_code + str(row['WhatsAppNumber'])

    # Check if the number has already received a message
    if number in sent_messages:
        print(f"Message already sent to {name} at {sent_messages[number]}")
        continue

    # Compose the message
    message_text = f"Hello {name}, {message}"

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Calculate the time for sending the message (adjust as needed)
    hours, minutes = now.hour, now.minute + 1  # Send the message 1 minute from now

    # Send the message using pywhatkit
    kit.sendwhatmsg(number, message_text, hours, minutes)

    # Update the sent_messages dictionary
    sent_messages[number] = current_time

    print(f"Message sent to {name} at {current_time}")