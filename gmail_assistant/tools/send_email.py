from email.mime.text import MIMEText
import base64
from google.adk.tools import tool
from tools.gmail_serivce import get_gmail_service_via_oauth


def send_email(recipient:str,subject:str,body:str) -> str:
    """
        Send an email using Gmail API.

        Args:
            recipient (str): Email address of the recipient.
            subject (str): Subject of the email.
            body (str): Email message content.

        Returns:
            str: Confirmation message.
    """
    service = get_gmail_service_via_oauth()
    if not service:
        return "❌ Gmail authentication failed. Please check your credentials."

    try:
        message = MIMEText(body)
        message['to'] = recipient
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Send the email
        service.users().messages().send(
            userId="me",body={"raw":raw}
        ).execute()

        return f"✅ Email successfully sent to {recipient}."
    
    except Exception as e:
        return f"❌ Failed to send email: {str(e)}"


