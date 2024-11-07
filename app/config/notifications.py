# from pyfcm import FCMNotification
# import os
# from dotenv import load_dotenv

# load_dotenv()

# push_service = FCMNotification(
#     service_account_file=os.getenv("FCM_SERVICE_ACCOUNT_FILE"),
#     project_id=os.getenv("FCM_PROJECT_ID"),
# )
# push_service.api_key = os.getenv("FCM_API_KEY")


# def send_push_notification(token: str, title: str, message: str):
#     result = push_service.notify(
#         fcm_token=token,
#         notification_title=title,
#         notification_body=message,
#     )
#     return result

from pydantic import BaseModel
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

SERVICE_ACCOUNT_FILE = "/Users/tomasdaureli/Dropbox/UADE/Seminario de Gestion de Tecnologia/heycar/heycar-backend/heycar-422b4-firebase-adminsdk-jvfdo-75eccc15fb.json"
PROJECT_ID = "heycar-422b4"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)


def get_access_token():
    credentials.refresh(Request())
    print(credentials.token)
    return credentials.token


class PushNotificationPayload(BaseModel):
    title: str
    body: str
    token: str


def send_notification(payload):
    access_token = get_access_token()

    url = f"https://fcm.googleapis.com/v1/projects/{PROJECT_ID}/messages:send"

    message = {
        "message": {
            "token": payload.token,
            "notification": {
                "title": payload.title,
                "body": payload.body,
            },
            "webpush": {
                "fcm_options": {
                    "link": "https://google.com",
                }
            },
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; UTF-8",
    }

    response = requests.post(url, data=json.dumps(message), headers=headers)

    return {"status": "success", "result": response.json()}
