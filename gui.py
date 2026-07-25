import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Available languages
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

# Function to translate
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source_language = source_language_var.get()
    target_language = target_language_var.get()

    translated = GoogleTranslator(
        source=languages[source_language],
        target=languages[target_language]
    ).translate(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)


# Function to clear text
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# Function to copy translated text
def copy_text():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Copied", "Translated text copied successfully!")


# Create window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("550x500")
root.configure(bg="#EAF4FC")

# Heading
heading = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold"),
    bg="#EAF4FC"
)
heading.pack(pady=10)

# Input label
tk.Label(root, text="Enter Text:", bg="#EAF4FC", font=("Arial", 11)).pack()

# Input text box
input_text = tk.Text(root, height=5, width=55)
input_text.pack(pady=5)

# Source Language
source_language_var = tk.StringVar()
source_language_var.set("English")

tk.Label(root, text="Source Language:", bg="#EAF4FC", font=("Arial", 11)).pack()

source_combo = ttk.Combobox(
    root,
    textvariable=source_language_var,
    values=list(languages.keys()),
    state="readonly"
)
source_combo.pack(pady=5)

# Target Language
target_language_var = tk.StringVar()
target_language_var.set("Telugu")

tk.Label(root, text="Target Language:", bg="#EAF4FC", font=("Arial", 11)).pack()

target_combo = ttk.Combobox(
    root,
    textvariable=target_language_var,
    values=list(languages.keys()),
    state="readonly"
)
target_combo.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=10)

translate_btn = tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    width=12
)
translate_btn.grid(row=0, column=0, padx=5)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_text,
    width=12
)
copy_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=12
)
clear_btn.grid(row=0, column=2, padx=5)

# Output label
tk.Label(root, text="Translated Text:", bg="#EAF4FC", font=("Arial", 11)).pack()

# Output text box
output_text = tk.Text(root, height=5, width=55)
output_text.pack(pady=5)

# Run application
root.mainloop()