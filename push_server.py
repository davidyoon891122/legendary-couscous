from pyfcm import FCMNotification
from dotenv import load_dotenv
import os
from dotenv import dotenv_values

load_dotenv(dotenv_path=".env")

APIKEY = os.getenv("APIKEY")
TOKEN = "fYoSOhp1q0FerU-r3puVyb:APA91bE8NpVhWmoWnscOFQmUrmfeclLsg1pgw9MgVE51W2zxC0pFQEdQTqUMIWSj4fZiAqe8FaUunDxvwh3UMNZXxRAixxMF8M6zM-uN7hdOXz5qzkB6lKdd-eN0HO72vkVvVpVYNf41"

push_service = FCMNotification(APIKEY)

def send_message(body, title):
    result = push_service.notify_single_device(registration_id=TOKEN, message_title=title, message_body=body)
    print("result: {}".format(result))


send_message("This is my custom body!", "Python Push Server")

