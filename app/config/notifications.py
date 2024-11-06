# from pyfcm import FCMNotification
# import os
# from dotenv import load_dotenv

# load_dotenv()

# push_service = FCMNotification(
#    service_account_file=os.getenv("FCM_SERVICE_ACCOUNT_FILE"),
#    project_id=os.getenv("FCM_PROJECT_ID"),
# )
# push_service.api_key = os.getenv("FCM_API_KEY")


# def send_push_notification(token: str, title: str, message: str):
#    result = push_service.notify_single_device(
#        registration_id=token,
#        message_title=title,
#        message_body=message,
#    )
#    return result
