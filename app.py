from deep_translator import GoogleTranslator

# Supported languages
languages = {
    "1": ("English", "en"),
    "2": ("Telugu", "te"),
    "3": ("Hindi", "hi"),
    "4": ("Tamil", "ta"),
    "5": ("Kannada", "kn"),
    "6": ("Malayalam", "ml"),
    "7": ("French", "fr"),
    "8": ("Spanish", "es"),
    "9": ("German", "de"),
    "10": ("Japanese", "ja")
}

print("====== Language Translation Tool ======")
print("Choose the language to translate into:\n")

for key, value in languages.items():
    print(f"{key}. {value[0]}")

text = input("\nEnter the text to translate: ")
choice = input("Enter your choice (1-10): ")

if choice in languages:
    target_language = languages[choice][1]

    translated = GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    print("\nTranslated Text:")
    print(translated)
else:
    print("Invalid choice! Please run the program again.")