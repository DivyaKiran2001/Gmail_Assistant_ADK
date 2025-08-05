# Gmail_Assistant_ADK
#### Created a Gmail Assistand using Google Agent Development Kit(ADK)


# 📬 Gmail Voice Assistant with Google ADK

This project is a **voice-controlled AI assistant** that lets users **send emails** and **check unread emails** using the **Gmail API** and **Google Agent Development Kit (ADK)**. It understands natural language commands like:

- **"Send an email to my boss saying I'm on leave today."**
- **"Do I have any unread emails?"**

Built using the **Agentic AI approach**, the assistant proactively executes tasks via tool integrations and can be extended for more actions like reading full emails, searching emails, etc.

---

## 🎯 Features

✅ Send emails via Gmail using voice/text commands  
✅ Check and summarize unread emails  
✅ Built using Google’s Agent Development Kit (ADK)  
✅ Gemini-powered agent + Gmail API tools  
✅ Secure OAuth 2.0 authentication  
✅ Real-time WebSocket communication between frontend and backend  
✅ Modular structure for easy extension

---

## 🛠️ Tech Stack

- **Google ADK**
- **Gemini 1.5 Pro / Flash**
- **FastAPI** (backend API)
- **Gmail API** (send/read emails)
- **WebSockets** (real-time chat)
- **OAuth 2.0** for secure Gmail access

---

## 🧠 How It Works

1. User speaks or types a natural language command (e.g., "Email my manager").
2. The **Gemini-powered agent** interprets the intent.
3. ADK routes the action to the right tool:
   - `send_email` to send mail
   - `check_unread_emails` to list unread messages
4. The tool interacts with the Gmail API via an authenticated service.
5. The response is streamed back to the frontend in real time.

---

## 📂 Project Structure

```
gmail-agent/
│
├── main.py                      # FastAPI app + socket interface
├── gmail_assistant/
│   └── agent.py          # ADK agent config + tools
    └── __init__.py        
├── tools/
│   ├── send_email.py           # Tool to send emails
│   ├── check_unread_emails.py  # Tool to list unread mails
│   └── gmail_service.py        # Gmail API service (OAuth logic)
    └── __init__.py        
├── credentials/
│   └── credentials.json        # OAuth 2.0 client credentials
├── static/js                     # Frontend HTML/CSS/JS (optional)
    └── index.html        
│
└── README.md
```

---

## 🚀 Getting Started


###  Setup Gmail API Credentials

- Go to: https://console.cloud.google.com/apis/credentials
- Create OAuth 2.0 Client ID (Desktop App)
- Download `credentials.json` and place it inside `credentials/`

On first run, you'll be prompted to sign in and authorize Gmail access.


---

## 📈 Future Ideas

- Read full email content
- Search inbox
- Schedule recurring emails
- Integration with Google Calendar

---

## 📄 License

MIT
