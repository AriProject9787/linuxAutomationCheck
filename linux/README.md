🔧 Terminal Tool Manager – Linux & Termux

A cross-platform interactive Python CLI for updating the system and selectively installing or upgrading useful tools on Linux and Termux environments.
📌 Overview

This project offers an elegant command-line interface that allows users to:

    🚀 Update their Linux or Termux system.

    🛠️ Install essential and fun tools interactively.

    ♻️ Update specific tools from a curated list.

    📋 Get descriptions and select tools easily by number.

    Developed with attention to usability and compatibility for both traditional Linux users and Android (Termux) enthusiasts.

📸 Preview

==================== Developed by Arirama Selvam ====================
GitHub:  https://github.com/ByteMasterArirama
LinkedIn: https://linkedin.com/in/ariramaselvam

========= Main Menu =========
1. Update System
2. Install Tools (Selective)
3. Update Tools (Selective)
4. About Developer
00. Exit Program
==============================

⚙️ Features

    ✅ Environment-Aware: Detects Termux vs. traditional Linux systems.

    📥 Selective Installation: Choose tools by number from an intuitive list.

    🔄 Tool-Specific Upgrades: Avoid unnecessary updates; pick exactly what to upgrade.

    🖼️ Built-in Descriptions: Tool functionality is clearly displayed.

    🔐 Safe Execution: Handles installation and update errors gracefully.

🛠️ Tools Supported

The installer provides a variety of categories:
🔹 Common Utilities

    cmatrix – Matrix-style animation

    sl – Steam locomotive

    cowsay – ASCII bubble speech

    toilet – ASCII banners

    git – Version control

    apache2 – Web server

🔹 Developer & Admin Tools

    curl, wget, python, nodejs

    vim, nano, gcc, make, openjdk-17-jdk

🔹 Terminal Fun

    figlet, lolcat, neofetch, htop, btop

    asciiquarium, boxes, fortune, ponysay

🔹 Cybersecurity

    nmap, hydra, sqlmap, whois, dnsutils, aircrack-ng, tcpdump

📦 Installation
🐧 On Linux:

git clone https://github.com/ByteMasterArirama/terminal-tool-manager.git
cd terminal-tool-manager
python3 tool_manager.py

📱 On Termux (Android):

pkg install git python -y
git clone https://github.com/ByteMasterArirama/terminal-tool-manager.git
cd terminal-tool-manager
python tool_manager.py

📖 Usage

After running the script:

    Use the numbered options to navigate.

    Select multiple tools by entering comma-separated numbers (e.g., 1,3,5).

    Use 00 to return or exit.

👨‍💻 About the Developer

Arirama Selvam M
🛡️ Cybersecurity & Automation Enthusiast
🎓 BE CSE, Dr. G.U. Pope College of Engineering
🔗 LinkedIn: @ariramaselvam
🐙 GitHub: @ByteMasterArirama

    Passionate about open-source, security, and making tools that simplify digital life.

📃 License

This project is licensed under the MIT License. See the LICENSE file for more details.
🙌 Contributions

Pull requests and suggestions are welcome. Please open an issue first to discuss what you would like to change.
