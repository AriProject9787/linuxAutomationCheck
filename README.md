# Linux & Termux Automation Toolkit

**Author:** Arirama Selvam M

A powerful automation toolkit for **Linux** and **Android Termux** that simplifies system updates, package installations, and cybersecurity workflows. The toolkit is enhanced with **wake word detection** for hands-free operation, enabling efficient and interactive system management.

---

## 🚀 Features

* **System Update Automation**
  Perform operating system and package updates using a single command or wake word activation.

* **Tool Installation & Upgrade**
  Install and upgrade selected tools directly from a centralized JSON configuration file.

* **Tool Status Checker**
  Display installed tools along with their current installation status.

* **Voice Feedback**
  Real-time spoken responses using Google Text-to-Speech (gTTS).

* **Wake Word Detection**
  Hands-free activation using the phrase **"Hello Echo"**, powered by the Picovoice Porcupine SDK.

* **Activity Logging**
  Comprehensive logging of actions for auditing, troubleshooting, and monitoring.

* **Extra Modules**

  * Metasploit Automation Tool
  * WiFi Deauthentication Attack Tool

* **Cross-Platform Support**

  * Linux Desktop (APT-based distributions)
  * Android Termux (PKG-based)

---

## 📦 Tech Stack

* **Programming Language:** Python 3.x
* **Libraries:**

  * gTTS – Text-to-speech functionality
  * subprocess, platform, shutil, json – System automation utilities
  * Picovoice Porcupine – Wake word detection engine
* **Package Managers:** apt, pkg

---

## 📂 Project Structure

```
📦 linux-termux-toolkit
 ┣ 📜 main.py              # Main toolkit controller
 ┣ 📜 tools.json           # Tool definitions and configuration
 ┣ 📜 metasploit.py        # Metasploit automation module
 ┣ 📜 deauthAttack.py      # WiFi deauthentication module
 ┣ 📜 update_tool_log.txt  # Activity and error logs
 ┗ 📜 README.md            # Project documentation
```

---

## ⚙️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/AriProject9787/linuxAutomationCheck
cd linuxAutomationCheck
```

### 2. Install Required Dependencies

```bash
pip install gtts
pip install pvporcupine
```

### 3. Run the Toolkit

```bash
python3 main.py
```

---

## 🎤 Wake Word Activation

This toolkit supports hands-free execution using the Picovoice Porcupine SDK.

### Setup Instructions

1. Obtain a free **Picovoice Access Key** from:
   [https://picovoice.ai/](https://picovoice.ai/)

2. Train or download a custom `.ppn` wake word model.

3. Update the wake word configuration in the script:

```python
porcupine = pvporcupine.create(
    access_key="YOUR_ACCESS_KEY",
    keyword_paths=["path/to/hello-echo.ppn"]
)
```

4. Speak **"Hello Echo"** to activate the toolkit.

---

## 📜 Logging

All system actions and events are stored in the following file:

```
update_tool_log.txt
```

### Logged Details Include

* Tool installations and upgrades
* System update operations
* Wake word activations
* Runtime errors and exceptions

---

## 👨‍💻 Developer Information

* **Name:** Arirama Selvam M
* **Specialization:** Cybersecurity | Automation | SaaS Development
* **GitHub:** [https://github.com/AriProject9787](https://github.com/AriProject9787)
* **LinkedIn:** [https://www.linkedin.com/in/ariramaselvam](https://www.linkedin.com/in/ariramaselvam)
* **Email:** [ariofficial9787@gmail.com](mailto:ariofficial9787@gmail.com)

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software in compliance with the license terms.

---

## ⭐ Contributing

Contributions are welcome. If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.
