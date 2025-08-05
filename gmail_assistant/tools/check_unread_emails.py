"""
Tool to check unread emails using the Gmail API.
"""

from google.adk.tools import tool
from tools.gmail_serivce import get_gmail_service_via_oauth

def check_unread_emails():
    """
        Fetch and list unread emails in the user's inbox.

        Returns:
            str: A summary of up to 5 unread emails.
    """

    service = get_gmail_service_via_oauth()

    if not service:
        return "❌ Gmail authentication failed. Please check your credentials."
    
    try:
        response = service.users().messages().list(
            userId="me",
            labelIds=["INBOX"],
            q="is:unread",
            maxResults=5
        ).execute()

        messages = response.get("message",[])
        if not messages:
            return "📭 No unread emails found."
        
        summaries = []
        for msg in messages:
            message = service.users().messages().get(userId="me",id=msg["id"]).execute()
            headers = message.get("payload",{}).get("headers")

            subject = next((h["value"] for h in headers if h["name"] == "Subject" ),"(No Subject)")
            sender = next((h["value"] for h in headers if h["name"]=="From"),"(Unknown Sender)")
            
            summaries.append(f"📨 From: {sender} | Subject: {subject}")

    
        return "\n".join(summaries)
    
    except Exception as e:
        return f"❌ Error retrieving unread emails: {str(e)}"
        

     
