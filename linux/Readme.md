Linux & Termux Automation Toolkit

By Arirama Selvam M



A powerful automation toolkit for Linux and Android Termux that simplifies system updates, package installations, and cybersecurity workflows — now enhanced with wake word detection for hands-free operation.
🚀 Features

    System Update Automation – Update your OS and packages with a single command or wake word.

    Tool Installation & Upgrade – Install and update selected tools directly from a JSON list.

    Tool Status Checker – View installed tools and their status.

    Voice Feedback – Real-time spoken responses using Google Text-to-Speech (gTTS).

    Wake Word Detection – Activate the toolkit hands-free by saying "Hello Echo" (powered by Picovoice Porcupine SDK).

    Activity Logging – Tracks all actions for auditing and debugging.

    Extra Modules – Includes:

        Metasploit Automation Tool

        WiFi Deauthentication Attack Tool

    Cross-Platform Support – Runs on:

        Linux Desktop (APT-based distros)

        Android Termux (pkg-based)

📦 Tech Stack

    Language: Python 3.x

    Libraries:

        gTTS – Text-to-speech feedback

        subprocess, platform, shutil, json – System automation

        Picovoice Porcupine – Wake word detection

    Package Managers: apt & pkg

📂 Project Structure

📦 linux-termux-toolkit
 ┣ 📜 main.py              # Main script with toolkit features
 ┣ 📜 tools.json           # JSON file with available tools
 ┣ 📜 metasploit.py        # Metasploit automation script
 ┣ 📜 deauthAttack.py      # WiFi deauthentication tool
 ┣ 📜 update_tool_log.txt  # Log file for activity tracking
 ┗ 📜 README.md            # Documentation

⚙️ Installation & Usage
1️⃣ Clone Repository

git clone https://github.com/YourUsername/linux-termux-toolkit.git
cd linux-termux-toolkit

2️⃣ Install Dependencies

pip install gtts
pip install pvporcupine

3️⃣ Run the Toolkit

python3 main.py

🎤 Wake Word Activation

The toolkit can be launched with a wake word using Picovoice Porcupine SDK.

Setup:

    Get a free Picovoice Access Key from https://picovoice.ai/

    Train or download your custom .ppn wake word model.

    Update the script to include:

porcupine = pvporcupine.create(
    access_key="YOUR_ACCESS_KEY",
    keyword_paths=["path/to/hello-echo.ppn"]
)

    Speak "Hello Echo" to activate.

📜 Logging

All actions are stored in:

update_tool_log.txt

Including:

    Installation logs

    Updates

    Wake word activations

    Errors

👨‍💻 Developer Information

Name: Arirama Selvam M
About: Cybersecurity | Automation | SaaS Developer
GitHub: https://github.com/AriProject9787
LinkedIn: https://www.linkedin.com/in/ariramaselvam
Email: ariofficial9787@gmail.com
📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.
⭐ Contributing

Pull requests are welcome. If you have ideas for new features or improvements, feel free to open an issue.