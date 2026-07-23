
<h1 align="center">🚀 Internet Complaint Bot</h1>

<p align="center">
An AI-powered Python bot that automatically monitors internet speed, verifies slow network performance through multiple tests, and sends a professional complaint email to your ISP.
</p>

---

## ✨ Features

<ul>
  <li>🌐 Automated Speedtest using Selenium</li>
  <li>📊 Download & Upload speed monitoring</li>
  <li>🔄 Three consecutive verification tests</li>
  <li>🤖 AI-generated complaint email using Gemini</li>
  <li>📧 Automatic email sending via Gmail SMTP</li>
  <li>🔐 Secure credentials with <code>.env</code></li>
</ul>

## 🛠️ Tech Stack

<p>
Python • Selenium • Google Gemini API • SMTP • python-dotenv
</p>

## 📂 Project Structure

```text
.
├── main.py
├── internet.py
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/Jyoti-Ranjan-Rout/internet-complaint-bot.git
cd internet-complaint-bot
pip install -r requirements.txt
```

## ▶️ Run

```bash
python main.py
```

## 🔒 Environment Variables

```env
API=your_gemini_api_key
EMAIL=your_email@gmail.com
PASS=your_gmail_app_password
EMAIL_R=receiver@gmail.com
```

## 🔄 Workflow

```text
Speed Test
    ↓
Below Threshold?
    ↓
Verify 3 Times
    ↓
Generate AI Email
    ↓
Send Complaint
```

<h3 align="center">⭐ Star this repository if you found it useful!</h3>
