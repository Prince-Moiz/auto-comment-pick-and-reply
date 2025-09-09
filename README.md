# 🤖 Twitter Auto-Reply Automation (Python + Playwright)

This project is a **Twitter automation bot** built with **Python** and **Playwright**.  
It monitors tweets in real time and automatically **likes + replies** with random pre-configured responses.  

I designed this project as a demonstration of my ability to:  
- Build **robust automation scripts** for real-world web applications.  
- Apply **UI automation frameworks** (Playwright) to replicate user flows.  
- Combine **backend logic + service automation** for complex workflows.  
- Handle **timeouts, retries, and error recovery** in distributed systems.  

---

## ✨ Features
- 🔍 Scans Twitter timeline for tweets.  
- ❤️ Auto-likes tweets not already engaged.  
- 💬 Posts random replies from a configurable list of responses.  
- 🛡️ Built-in error handling, retries, and recovery flows.  
- 🔄 Continuous loop with refresh logic for long-running tasks.  
- 🧩 Uses cookies + auth for authenticated sessions.  

---

## 🚀 Tech Stack
- **Python** – core automation logic.  
- **Playwright** – UI automation & browser control.  
- **Pyperclip** – clipboard integration for text input.  
- **JSON** – session cookies for persistent login.  
- **SQL (optional)** – structured logging & data handling.  
- **Docker** – containerized execution.  
- **CI/CD (GitHub Actions, Jenkins-ready)** – automated testing & deployment pipelines.  

---

## 🧑‍💻 Skills Demonstrated
This project reflects the same skills required for **Senior Automation Engineer** roles:  

- ✅ **Automation testing** with Playwright (UI + service layer).  
- ✅ **Python scripting** for complex workflows.  
- ✅ **CI/CD pipelines** (GitHub Actions / Jenkins).  
- ✅ **Dockerized automation environments**.  
- ✅ **SQL** for data validation & logging.  
- ✅ **Resilient test design** with retries, error handling, and reporting.  
- ✅ **Scalable automation design** for production-like environments.  

---

## 📌 Other Relevant Work
### 🔹 FollowPay  
I also built **FollowPay**, a SaaS product that automates **social media engagement** with:  
- Scheduled follows, replies, and campaigns.  
- API-driven architecture for scalability.  
- Business-focused features for **audience growth & retention**.  

Together, these projects demonstrate my ability to create **real-world automation frameworks** that scale.  

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+  
- Playwright installed (`pip install playwright`)  
- Twitter account & cookies.json for authentication  

### Setup & Run
```bash
# Clone the repo
git clone https://github.com/Prince-Moiz/auto-comment-pick-and-reply.git
cd twitter-autoreply-bot

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Run the bot
python main.py
