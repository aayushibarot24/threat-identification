import tkinter as tk
from tkinter import messagebox
import re
import time
import threading

# --------------------------
# Window Setup
# --------------------------
root = tk.Tk()
root.title("Cyber Threat Detection System")
root.geometry("600x600")
root.config(bg="#1e1e2f")

# --------------------------
# Title
# --------------------------
title = tk.Label(root, text="Cyber Threat Detection System",
                 font=("Helvetica", 18, "bold"),
                 bg="#1e1e2f", fg="#00ffcc")
title.pack(pady=15)

# --------------------------
# Input Section
# --------------------------
frame_input = tk.Frame(root, bg="#1e1e2f")
frame_input.pack()

label = tk.Label(frame_input, text="Enter URL or Password:",
                 bg="#1e1e2f", fg="white")
label.pack()

entry = tk.Entry(frame_input, width=50, font=("Arial", 12))
entry.pack(pady=10)

# --------------------------
# Output Box
# --------------------------
output = tk.Text(root, height=12, width=65,
                 bg="#2b2b3c", fg="#00ffcc",
                 font=("Consolas", 10))
output.pack(pady=15)

def show_output(text):
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)

# --------------------------
# Functions
# --------------------------
def check_phishing():
    url = entry.get()

    suspicious_keywords = ["login", "verify", "secure", "update"]
    
    if any(word in url.lower() for word in suspicious_keywords) or ".xyz" in url:
        show_output("⚠ WARNING: Suspicious URL detected!\nPossible phishing attempt.")
    else:
        show_output("✔ URL appears safe.")

def check_password():
    password = entry.get()

    strength = "Weak"

    if len(password) >= 8:
        if re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[@#$%^&*]", password):
            strength = "Strong"
        else:
            strength = "Medium"

    show_output(f"🔐 Password Strength: {strength}")

def malware_simulation():
    show_output("⚠ Running malware simulation...\nEncrypting files...")
    root.after(2000, lambda: show_output("⚠ Files encrypted! (Simulation only)"))

def ddos_simulation():
    def simulate():
        output.delete(1.0, tk.END)
        for i in range(15):
            output.insert(tk.END, f"Request from IP {i+1}\n")
            output.update()
            time.sleep(0.2)
        output.insert(tk.END, "\n⚠ SERVER OVERLOADED (DDoS Simulation)")

    threading.Thread(target=simulate).start()

# --------------------------
# Button Styling
# --------------------------
def create_button(text, command):
    return tk.Button(root,
                     text=text,
                     command=command,
                     width=30,
                     bg="#00ffcc",
                     fg="black",
                     font=("Arial", 10, "bold"),
                     relief="flat",
                     pady=8)

# --------------------------
# Buttons
# --------------------------
btn1 = create_button("Check Phishing URL", check_phishing)
btn1.pack(pady=5)

btn2 = create_button("Check Password Strength", check_password)
btn2.pack(pady=5)

btn3 = create_button("Run Malware Simulation", malware_simulation)
btn3.pack(pady=5)

btn4 = create_button("Run DDoS Simulation", ddos_simulation)
btn4.pack(pady=5)

# --------------------------
# Footer
# --------------------------
footer = tk.Label(root, text="Cybersecurity Awareness Project",
                  bg="#1e1e2f", fg="gray")
footer.pack(side="bottom", pady=10)

# Run app
root.mainloop()