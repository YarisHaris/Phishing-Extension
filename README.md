# 🛡️ Phishing Link Detection Browser Extension + Flask API

A real-time phishing link detection system built using a browser extension and a Python Flask backend. It highlights and blocks suspicious URLs by analyzing links on any visited page and checking them against phishing threat sources.

---

## 🚀 Features

- 🔍 **Real-time Link Scanning** – Automatically scans all `<a>` tags on a webpage
- ☁️ **Flask Backend API** – Uses Google Safe Browsing API to verify suspicious URLs
- 🚨 **Link Highlighting** – Flags dangerous links with red border and tooltips
- ⛔ **Navigation Blocking** – Prevents users from clicking on dangerous links
- 📱 **Cross-platform Ready** – Testable on Chrome, Firefox, and even via Android WebView

---

## 🛠️ Technologies Used

- ✅ **JavaScript** (for content script)
- ✅ **Manifest V2/V3** (for browser extension compatibility)
- ✅ **Python Flask** (backend)
- ✅ **Google Safe Browsing API**
- ✅ **HTML + CSS**
- ✅ **CORS-enabled API communication**

---

## 📁 Project Structure

---

## ⚙️ Setup Instructions

### 🔹 Backend (Flask)

1. Go to `phishing-backend/`
2. Create `.env` file:
    ```
    GOOGLE_API_KEY=your_google_safe_browsing_api_key
    ```
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```bash
    python app.py
    ```

---

### 🔹 Frontend (Extension)

1. Open `chrome://extensions` or `about:debugging` in Firefox
2. Enable "Developer Mode"
3. Click **Load Unpacked** → select `phishing-extension/` folder
4. Browse any webpage → suspicious links get flagged automatically

---

## 🧪 Testing Links

Use fake phishing-like URLs for testing:

```html
<a href="http://freelogin.xyz/account">Fake Login</a>
<a href="http://update-paypal-security.com/login">Fake PayPal</a>

⚠️ Security Notes

    Do NOT expose your .env file or API key in GitHub

    Always restrict your Google Safe Browsing API usage
