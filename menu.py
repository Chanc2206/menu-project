import boto3

import pymongo

import os

import sys

from pymongo.mongo_client import MongoClient

from pymongo.server_api import ServerApi

import time

from datetime import datetime



print("\t\t\t\tWelcome to Team Vision")

print("\t\t\t\t-----------------------")



print("""

press1  : Send Email message using python code

press2  : Send SMS message using python code

press3  : Scrap top 5 search results from google using the python code

press4  : Find the current geo coordinates and location using the Python code 

press5  : Convert text-to-audio using the python code

press6  : Control volume of your laptop using python.

press7  : Connect to your mobile and send sms from your mobile messaging app using python.

press8  : Create a function to Send bulk email using python.

press9  : Send WhatsApp Message using terminal

press10 : Output of a command should be spoken from the speaker also.

press11 : Send Email from Linux Terminal.

press12 : Send SMS using terminal.

press13 : Use linux as a zoom server.

press14 : To make a post in telegram, instagram, facebook, discord from the linux terminal

press15 : Change the color of files and folder in linux.

press16 : Reading the entire RAM.

press17 : Change the look and feel of GNOME terminal.

press18 : To create user and set password.

press19 : Running linux in the browser.

press20 : Google search from terminal.

press21 : Run Windows softwares e.g notepad in linux.

press22 : Sync two different folders in linux. It should ask the user which folders to sync.

press23 : On your cmd you print something and it will be converted to ASCII art.

press24 : Launch ec2 instances in aws

press25 : Launch EC2 instance with RHEL GUI")

press26 :  Access logs from the cloud (CloudWatch)

press27 :  Event-driven architecture for audio transcription

press28 :  Connect Python to MongoDB using Lambda

press29 :  Upload an object to S3

press30 :  Integrate Lambda with S3 and SES to send emails

press31 : 

press32 : 

press33 : 

press34 : 

""")



ch = input("Enter your choice: ")



if int(ch) == 1:

    import smtplib

    from email.mime.multipart import MIMEMultipart

    from email.mime.text import MIMEText



    def send_email(sender_email, sender_password, recipient_email, subject, body):

        msg = MIMEMultipart()

        msg['From'] = sender_email

        msg['To'] = recipient_email

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))



        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender_email, sender_password)

            server.send_message(msg)

            print("Email sent successfully!")

        except Exception as e:

            print(f"Failed to send email: {e}")

        finally:

            server.quit()



    sender_email = "shreedank18@gmail.com"

    sender_password = input("Enter your email password: ")

    recipient_email = input("Enter the recipient's email: ")

    subject = input("Enter the subject of the email: ")

    body = input("Enter the body of the email: ")

    send_email(sender_email, sender_password, recipient_email, subject, body)



elif int(ch) == 2:

    from twilio.rest import Client

    from datetime import datetime, timedelta

    import time



    account_sid = 'your_twilio_sid'

    auth_token = 'your_twilio_auth_token'

    twilio_number = 'your_twilio_number'

    client = Client(account_sid, auth_token)



    def send_sms():

        to_number = input("Enter the recipient's phone number (with country code): ")

        message = input("Enter your message: ")

        choice = input("Send now (N) or later (L)? ").upper()



        if choice == 'N':

            send_message(to_number, message)

            print("Message sent!")

        elif choice == 'L':

            hour = int(input("Enter hour to send (0-23): "))

            minute = int(input("Enter minute to send (0-59): "))

            now = datetime.now()

            send_time = now.replace(hour=hour, minute=minute, second=0)



            if send_time <= now:

                send_time += timedelta(days=1)



            wait_time = (send_time - now).total_seconds()

            print(f"Message scheduled for {send_time.strftime('%Y-%m-%d %H:%M')}")

            time.sleep(wait_time)

            send_message(to_number, message)

            print("Scheduled message sent!")

        else:

            print("Invalid choice. Please run the program again.")



    def send_message(to_number, message):

        message = client.messages.create(

            body=message,

            from_=twilio_number,

            to=to_number

        )

        print(f"Message SID: {message.sid}")



    send_sms()



elif int(ch) == 3:

    from googlesearch import search



    def main():

        query = input("Enter the search query: ")

        num_results = 5

        search_results = search(query, num=num_results, stop=num_results, pause=2.0)

        print(f"Top {num_results} search results for '{query}':")

        for idx, result in enumerate(search_results, start=1):

            print(f"{idx}: {result}")



    main()



elif int(ch) == 4:

    import geocoder



    def get_current_location():

        g = geocoder.ip('me')

        if g.latlng:

            latitude, longitude = g.latlng

            location = f"{g.city}, {g.state}, {g.country}"

            print(f"Latitude: {latitude}, Longitude: {longitude}")

            print(f"Location: {location}")

        else:

            print("Unable to determine location.")



    get_current_location()



elif int(ch) == 5:

    from gtts import gTTS



    text = input("Enter the text you want to convert to speech: ")

    tts = gTTS(text=text, lang='en')

    tts.save("output.mp3")

    print("Audio saved as output.mp3")



elif int(ch) == 6:

    import ctypes

    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



    def set_volume(level):

        level = max(0, min(level, 100))

        devices = AudioUtilities.GetSpeakers()

        volume = devices.Activate(IAudioEndpointVolume._iid_, 23, None)

        volume = ctypes.cast(volume, ctypes.POINTER(IAudioEndpointVolume))

        volume.SetMasterVolumeLevelScalar(level / 100, None)

        print(f"Volume set to {level}%")



    try:

        level = int(input("Enter the volume level (0-100): "))

        set_volume(level)

    except ValueError:

        print("Please enter a valid number between 0 and 100.")



elif int(ch) == 7:

    print("Feature not yet implemented.")



elif int(ch) == 8:

    import smtplib

    from email.message import EmailMessage



    def send_bulk_emails(subject, body, recipients, smtp_server, smtp_port, email, password):

        message = EmailMessage()

        message.set_content(body)

        message['Subject'] = subject

        message['From'] = email



        try:

            with smtplib.SMTP(smtp_server, smtp_port) as server:

                server.starttls()

                server.login(email, password)

                for recipient in recipients:

                    message['To'] = recipient

                    server.send_message(message)

                    print(f"Email sent to {recipient}")

        except Exception as e:

            print(f"An error occurred: {e}")



    subject = "Your Subject Here"

    body = "This is the body of the email."

    recipients = ["recipient1@example.com", "recipient2@example.com"]

    smtp_server = "smtp.gmail.com"

    smtp_port = 587

    email = "your_email@example.com"

    password = "your_password"

    send_bulk_emails(subject, body, recipients, smtp_server, smtp_port, email, password)



elif int(ch) == 9:

    import pywhatkit

    from datetime import datetime, timedelta



    def send_whatsapp_message():

        phone_number = input("Enter the phone number (with country code): ")

        message = input("Enter your message: ")

        choice = input("Send now (N) or later (L)? ").upper()



        if choice == 'N':

            pywhatkit.sendwhatmsg_instantly(phone_number, message)

            print("Message sent!")

        elif choice == 'L':

            hour = int(input("Enter hour to send (0-23): "))

            minute = int(input("Enter minute to send (0-59): "))

            now = datetime.now()

            send_time = now.replace(hour=hour, minute=minute, second=0)



            if send_time <= now:

                send_time += timedelta(days=1)



            pywhatkit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)

            print(f"Message scheduled for {send_time.strftime('%Y-%m-%d %H:%M')}")

        else:

            print("Invalid choice. Please run the program again.")



    send_whatsapp_message()



elif int(ch) == 10:

    import subprocess

    import pyttsx3



    def speak_output(command):

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = result.stdout.strip()

        print(output)



        engine = pyttsx3.init()

        engine.say(output)

        engine.runAndWait()



    command = input("Enter a command to execute: ")

    speak_output(command)

elif int(ch) == 11:

    import smtplib

    from email.mime.multipart import MIMEMultipart

    from email.mime.text import MIMEText



    def send_email(sender_email, sender_password, recipient_email, subject, body):

        msg = MIMEMultipart()

        msg['From'] = sender_email

        msg['To'] = recipient_email

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))



        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender_email, sender_password)

            server.send_message(msg)

            print("Email sent successfully!")

        except Exception as e:

            print(f"Failed to send email: {e}")

        finally:

            server.quit()



    sender_email = "shreedank18@gmail.com"

    sender_password = input("Enter your email password: ")

    recipient_email = input("Enter the recipient's email: ")

    subject = input("Enter the subject of the email: ")

    body = input("Enter the body of the email: ")

    send_email(sender_email, sender_password, recipient_email, subject, body)



elif int(ch) == 12:

    print("Feature not yet implemented.")



elif int(ch) == 13:

    import os



    def run_command(command):

        print(f"Executing: {command}")

        os.system(command)



    def setup_jitsi_meet():

        # Update the system

        run_command("yum update -y")



        # Set the hostname (replace 'meet.yourdomain.com' with your actual domain)

        hostname = "www.streetkart.online"

        run_command(f"hostnamectl set-hostname {hostname}")



        # Install necessary dependencies

        run_command("yum install -y epel-release")

        run_command("yum install -y nginx certbot java-11-openjdk")



        # Add the Jitsi repository

        repo_content = """[jitsi]

name=Jitsi

baseurl=https://download.jitsi.org/stable/

gpgcheck=1

gpgkey=https://download.jitsi.org/jitsi-key.gpg.key"""



        with open("/etc/yum.repos.d/jitsi-stable.repo", "w") as repo_file:

            repo_file.write(repo_content)



        # Install Jitsi Meet

        run_command("yum install -y jitsi-meet")



        # Configure SSL using Let's Encrypt

        run_command("/usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh")



        # Open required firewall ports

        run_command("firewall-cmd --permanent --add-port=80/tcp")

        run_command("firewall-cmd --permanent --add-port=443/tcp")

        run_command("firewall-cmd --permanent --add-port=10000/udp")

        run_command("firewall-cmd --reload")



        # Start and enable services

        run_command("systemctl start nginx")

        run_command("systemctl enable nginx")

        run_command("systemctl start jitsi-videobridge2")

        run_command("systemctl enable jitsi-videobridge2")

        run_command("systemctl start jicofo")

        run_command("systemctl enable jicofo")

        run_command("systemctl start prosody")

        run_command("systemctl enable prosody")



        print(f"Jitsi Meet server setup complete. Access it at https://{hostname}")



    if __name__ == "__main__":

        setup_jitsi_meet()



elif int(ch) == 14:

    from instagrapi import Client



    # Replace with your Instagram credentials

    USERNAME = 'streetkart_app'

    PASSWORD = 'mishu@1234'



    def post_to_instagram(image_path, caption):

        cl = Client()

        cl.login(USERNAME, PASSWORD)

        cl.photo_upload(image_path, caption)



    # Example usage

    post_to_instagram('/root/Downloads/images.jpg', 'Hello from Street kart!')



elif int(ch) == 15:

    import os



    # Define ANSI escape codes for colors

    COLORS = {

        'reset': '\033[0m',

        'red': '\033[31m',

        'green': '\033[32m',

        'yellow': '\033[33m',

        'blue': '\033[34m',

        'magenta': '\033[35m',

        'cyan': '\033[36m',

        'white': '\033[37m'

    }



    def colorize(text, color):

        return f"{COLORS[color]}{text}{COLORS['reset']}"



    def list_colored_files_and_folders(directory):

        for item in os.listdir(directory):

            if os.path.isdir(os.path.join(directory, item)):

                print(colorize(item, 'blue'))  # Folders in blue

            else:

                print(colorize(item, 'green'))  # Files in green



    list_colored_files_and_folders(".")  # List current directory



elif int(ch) == 16:

    print("Feature not yet implemented.")



elif int(ch) == 17:

    import subprocess



    def set_gnome_terminal_preference(schema, key, value):

        # Construct the gsettings command

        command = ["gsettings", "set", schema, key, value]

        # Execute the command

        subprocess.run(command, check=True)

        print(f"Set {key} to {value} for {schema}")



    def change_gnome_terminal_look_and_feel():

        # Set profile ID (default in most cases, might need to be customized)

        profile_id = "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:<profile_id>/"



        # Font settings

        font = input("Enter the font you want to use (e.g., 'Monospace 12'): ")

        set_gnome_terminal_preference(profile_id, "font", f"'{font}'")



        # Background color

        bg_color = input("Enter the background color in HEX (e.g., '#000000' for black): ")

        set_gnome_terminal_preference(profile_id, "background-color", f"'{bg_color}'")



        # Foreground color

        fg_color = input("Enter the foreground color in HEX (e.g., '#FFFFFF' for white): ")

        set_gnome_terminal_preference(profile_id, "foreground-color", f"'{fg_color}'")



        # Use transparent background

        use_transparent_bg = input("Use transparent background? (true/false): ").lower()

        if use_transparent_bg == 'true':

            transparency = input("Enter transparency level (0 to 1, e.g., 0.5): ")

            set_gnome_terminal_preference(profile_id, "use-transparent-background", "true")

            set_gnome_terminal_preference(profile_id, "background-transparency-percent", str(int(float(transparency) * 100)))

        else:

            set_gnome_terminal_preference(profile_id, "use-transparent-background", "false")



        # Set theme variant

        dark_theme = input("Use dark theme? (true/false): ").lower()

        set_gnome_terminal_preference(profile_id, "use-theme-colors", "false")

        set_gnome_terminal_preference(profile_id, "use-theme-transparency", "false")

        set_gnome_terminal_preference("org.gnome.desktop.interface", "gtk-theme", "'Adwaita-dark'" if dark_theme == 'true' else "'Adwaita'")



    # Example usage

    change_gnome_terminal_look_and_feel()



elif int(ch) == 18:

    import subprocess



    def create_user(username, password):

        try:

            # Create the user

            subprocess.run(['useradd', '-m', username], check=True)

            print(f"User '{username}' created successfully.")



            # Set the password for the user

            # The password is passed to 'passwd' command using 'chpasswd'

            subprocess.run(['chpasswd'], input=f'{username}:{password}'.encode(), check=True)

            print(f"Password for user '{username}' set successfully.")

        except subprocess.CalledProcessError as e:

            print(f"An error occurred: {e}")

            print(f"Failed to create user '{username}' or set password.")



    def main():

        # Prompt for username and password

        username = input("Enter the username: ")

        password = input("Enter the password: ")



        # Create the user and set the password

        create_user(username, password)



    if __name__ == "__main__":

        main()



elif int(ch) == 20:

    import requests

    from bs4 import BeautifulSoup

    import urllib.parse



    def google_search(query):

        # Encode the query to be URL-safe

        query = urllib.parse.quote_plus(query)



        # Construct the Google search URL

        url = f"https://www.google.com/search?q={query}"



        # Define the headers to mimic a browser request

        headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

        }



        # Send the GET request to Google

        response = requests.get(url, headers=headers)



        # Parse the HTML response

        soup = BeautifulSoup(response.text, "html.parser")



        # Find and print all the search result links

        for g in soup.find_all('div', class_='BVG0Nb'):

            a_tag = g.find('a')

            if a_tag:

                link = a_tag['href']

                print(f"Title: {a_tag.text}")

                print(f"Link: {link}\n")



    if __name__ == "__main__":

        query = input("Enter your search query: ")

        google_search(query)



elif int(ch) == 21:

    print("Feature not yet implemented.")



elif int(ch) == 22:

    import subprocess

    import os



    def sync_folders(source_folder, destination_folder):

        # Ensure the source and destination folders exist

        if not os.path.isdir(source_folder):

            print(f"Source folder does not exist: {source_folder}")

            return

        if not os.path.isdir(destination_folder):

            print(f"Destination folder does not exist: {destination_folder}")

            return



        # Construct the rsync command

        rsync_command = [

            'rsync',

            '-av',           # Archive mode and verbose output

            '--delete',      # Delete files that are not in the source directory

            source_folder + '/',  # Add trailing slash to sync contents, not the folder itself

            destination_folder

        ]



        try:

            # Run the rsync command

            result = subprocess.run(rsync_command, capture_output=True, text=True)

            # Print the output and error messages

            print("Output:")

            print(result.stdout)

            print("Errors:")

            print(result.stderr)

            if result.returncode == 0:

                print("Sync completed successfully!")

            else:

                print("Sync failed with errors.")

        except FileNotFoundError:

            print("rsync command not found. Please install rsync.")

        except Exception as e:

            print(f"An error occurred: {e}")



    if __name__ == "__main__":

        source_folder = input("Enter the path to the source folder: ")

        destination_folder = input("Enter the path to the destination folder: ")

        sync_folders(source_folder, destination_folder)



elif int(ch) == 23:

    import pyfiglet



    def text_to_ascii():

        text = input("Enter the text you want to convert to ASCII art: ")

        ascii_art = pyfiglet.figlet_format(text)

        print(ascii_art)



    text_to_ascii()



elif int(ch) == 24:

    import boto3



    def create_ec2_instance():

        ec2 = boto3.resource('ec2')

        instances = ec2.create_instances(

            ImageId='ami-0c55b159cbfafe1f0',

            MinCount=1,

            MaxCount=1,

            InstanceType='t2.micro',

            KeyName='your-key-pair'

        )

        for instance in instances:

            print(f"EC2 instance {instance.id} created.")



    create_ec2_instance()



elif int(ch) == 25:

    import boto3



    def launch_rhel_gui():

        ec2 = boto3.resource('ec2')

        instances = ec2.create_instances(

            ImageId='ami-0e4d38ebd047c3d1a',

            MinCount=1,

            MaxCount=1,

            InstanceType='t2.micro',

            KeyName='your-key-pair',

            UserData='''

            #!/bin/bash

            yum update -y

            yum groupinstall -y "Server with GUI"

            systemctl set-default graphical.target

            systemctl isolate graphical.target

            '''

        )

        for instance in instances:

            print(f"RHEL GUI EC2 instance {instance.id} created.")



    launch_rhel_gui()



elif int(ch) == 26:

    import boto3



    def access_cloudwatch_logs():

        log_group_name = input("Enter the log group name: ")

        log_stream_name = input("Enter the log stream name: ")



        logs_client = boto3.client('logs')

        response = logs_client.get_log_events(

            logGroupName=log_group_name,

            logStreamName=log_stream_name

        )



        for event in response['events']:

            print(f"Timestamp: {event['timestamp']} - Message: {event['message']}")



    access_cloudwatch_logs()



elif int(ch) == 27:

    import json

    import boto3



    def transcribe_audio(event, context):

        s3 = boto3.client('s3')

        transcribe = boto3.client('transcribe')

        bucket = event['Records'][0]['s3']['bucket']['name']

        key = event['Records'][0]['s3']['object']['key']

        job_name = f"TranscriptionJob_{key}"

        job_uri = f"s3://{bucket}/{key}"



        transcribe.start_transcription_job(

            TranscriptionJobName=job_name,

            Media={'MediaFileUri': job_uri},

            MediaFormat='mp3',

            LanguageCode='en-US'

        )



        print(f"Started transcription job for {key}")



    transcribe_audio(event, context)



elif int(ch) == 28:

    import pymongo

    import boto3

    import json



    def lambda_handler(event, context):

        client = boto3.client('secretsmanager')

        secret_name = "your_mongodb_secret"

        response = client.get_secret_value(SecretId=secret_name)

        secret = json.loads(response['SecretString'])

        uri = secret['MONGODB_URI']



        mongo_client = pymongo.MongoClient(uri)

        db = mongo_client['your_database']

        collection = db['your_collection']



        document = event['document']

        result = collection.insert_one(document)



        return {

            'statusCode': 200,

            'body': json.dumps(f"Document inserted with ID: {result.inserted_id}")

        }



elif int(ch) == 29:

    import boto3



    def upload_to_s3():

        s3 = boto3.client('s3')

        bucket_name = 'your_bucket_name'

        file_name = input("Enter the file name to upload: ")

        object_name = input("Enter the S3 object name: ")



        try:

            s3.upload_file(file_name, bucket_name, object_name)

            print(f"{file_name} uploaded to {bucket_name}/{object_name}")

        except Exception as e:

            print(f"Error uploading file: {e}")



    upload_to_s3()



elif int(ch) == 30:

    import boto3



    def lambda_s3_ses_handler(event, context):

        s3_client = boto3.client('s3')

        ses_client = boto3.client('ses')

        bucket = event['Records'][0]['s3']['bucket']['name']

        key = event['Records'][0]['s3']['object']['key']

        email_body = f"File {key} was uploaded to {bucket}"



        response = ses_client.send_email(

            Source='your_email@example.com',

            Destination={'ToAddresses': ['recipient@example.com']},

            Message={

                'Subject': {'Data': 'S3 Upload Notification'},

                'Body': {'Text': {'Data': email_body}}

            }

        )

        print("Email sent.")



    lambda_s3_ses_handler(event, context)



else:

    print("Invalid choice, please run the script again.")

