import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES  # type: ignore # Google Translate library for translation

# Initialize the Translator
translator = Translator()

def translate_text():
    try:
        # Get text from the input Text widget
        text = text_input.get("1.0", tk.END).strip()
        # Get selected source and destination languages from comboboxes
        src_language = src_lang_combobox.get()
        dest_language = dest_lang_combobox.get()
        
        # Check if input text is empty
        if not text:
            messagebox.showerror("Input Error", "Please enter text to translate.")
            return
        
        # Translate the text
        translation = translator.translate(text, src=src_language, dest=dest_language)
        # Clear the output Text widget
        text_output.delete("1.0", tk.END)
        # Insert the translated text into the output Text widget
        text_output.insert(tk.END, translation.text)
    except Exception as e:
        # Show error message if translation fails
        messagebox.showerror("Translation Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Mini Google Translator")

# Set window size
root.geometry("850x700")
root.configure(bg='#2E3B4E')  # Dark gray-blue background

# Configure the grid
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(6, weight=1)

# Create and apply styles for the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14, "bold"), background='#2E3B4E', foreground='#F0F0F0')  # Bold font for better visibility
style.configure("TButton", font=("Arial", 14, "bold"), background='#007BFF', foreground='white')  # Bold font and blue button with white text
style.configure("TCombobox", font=("Arial", 14), foreground='#495057')

# Create widgets

# Label for text input
text_input_label = ttk.Label(root, text="Enter text:")
text_input_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

# Text widget for entering text to be translated with a scrollbar
text_input_frame = ttk.Frame(root)
text_input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

text_input = tk.Text(text_input_frame, height=10, width=80, font=("Arial", 14), bg='#F8F9FA', fg='#212529', wrap=tk.WORD)
text_input.grid(row=0, column=0, sticky="nsew")

text_input_scrollbar = ttk.Scrollbar(text_input_frame, command=text_input.yview)
text_input_scrollbar.grid(row=0, column=1, sticky='ns')
text_input.config(yscrollcommand=text_input_scrollbar.set)

# Configure the grid in the text_input_frame
text_input_frame.grid_rowconfigure(0, weight=1)
text_input_frame.grid_columnconfigure(0, weight=1)

# Label for source language combobox
src_lang_label = ttk.Label(root, text="Source Language:")
src_lang_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

# Combobox for selecting the source language
src_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Arial", 14), background='#F8F9FA', foreground='#212529')
src_lang_combobox.set('English')
src_lang_combobox.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

# Label for destination language combobox
dest_lang_label = ttk.Label(root, text="Destination Language:")
dest_lang_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")

# Combobox for selecting the destination language
dest_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Arial", 14), background='#F8F9FA', foreground='#212529')
dest_lang_combobox.set('French')
dest_lang_combobox.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

# Button to trigger translation
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Label for translated text output
text_output_label = ttk.Label(root, text="Translated text:")
text_output_label.grid(row=5, column=0, pady=10, padx=10, sticky="w")

# Text widget for displaying the translated text with a scrollbar
text_output_frame = ttk.Frame(root)
text_output_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

text_output = tk.Text(text_output_frame, height=10, width=80, font=("Arial", 14), bg='#F8F9FA', fg='#212529', wrap=tk.WORD)
text_output.grid(row=0, column=0, sticky="nsew")

text_output_scrollbar = ttk.Scrollbar(text_output_frame, command=text_output.yview)
text_output_scrollbar.grid(row=0, column=1, sticky='ns')
text_output.config(yscrollcommand=text_output_scrollbar.set)

# Configure the grid in the text_output_frame
text_output_frame.grid_rowconfigure(0, weight=1)
text_output_frame.grid_columnconfigure(0, weight=1)

# Start the main event loop
root.mainloop()