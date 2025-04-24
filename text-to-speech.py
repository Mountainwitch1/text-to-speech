import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gtts import gTTS


def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        return
    language = 'en'  # You can change this to any language supported by gTTS

    # Create gTTS object and save it to a file
    tts = gTTS(text=text, lang=language, slow=False)

    # Ask user where to save the file
    filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if filename:
        tts.save(filename)


def preview_voice():
    text = "This is a preview of my voice."
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("preview.mp3")  # Save temporarily to preview
    # Play the file for preview (using default audio player)
    import os
    os.system("open preview.mp3")  # On macOS, use 'open' to play the file


# GUI setup
root = tk.Tk()
root.title("Offline TTS (gTTS)")
root.geometry("450x300")

# Text input
tk.Label(root, text="Enter text:").pack(anchor='w', padx=10)
text_entry = tk.Text(root, height=5)
text_entry.pack(fill="x", padx=10)

# Buttons
tk.Button(root, text="🔊 Preview Voice", command=preview_voice).pack(pady=5)
tk.Button(root, text="💾 Speak & Save", command=speak_text).pack(pady=10)

root.mainloop()
