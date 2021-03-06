from tkinter import ttk, messagebox
import tkinter as tk
import googletrans
import textblob


class TranslateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())

        self.title("TranslateApp - Clever Code")
        self.geometry("1190x370")
        self.resizable(width=False, height=False)
        self.config(bg="#1e1e1e")

        self.original_text = tk.Text(self, height=10, width=40, font=("Cascadia Code", 20), highlightthickness=1, borderwidth=0)
        self.original_text.grid(row=0, column=0, pady=20, padx=10)
        self.translate_button = tk.Button(self, text="Translate!", font=("Cascadia Code", 20), command=self.translate)
        self.translate_button.grid(row=0, column=1, padx=10)
        self.translated_text = tk.Text(self, height=10, width=40, font=("Cascadia Code", 20), highlightthickness=1, borderwidth=0)
        self.translated_text.grid(row=0, column=2, pady=20, padx=10)
        self.original_combo = ttk.Combobox(self, width=50, value=self.language_list)
        self.original_combo.current(45) # Italian
        self.original_combo.grid(row=1, column=0)
        self.translated_combo = ttk.Combobox(self, width=50, value=self.language_list)
        self.translated_combo.current(21) # English
        self.translated_combo.grid(row=1, column=2)
        self.clear_button = tk.Button(self, text="Clear", font=("Cascadia Code", 20), command=self.clear)
        self.clear_button.grid(row=2, column=1)
    
    def translate(self):
        self.translated_text.delete(1.0, tk.END)
        try:
            for key, value in self.languages.items():
                if value == self.original_combo.get():
                    from_language_key = key
            
            for key, value in self.languages.items():
                if value == self.translated_combo.get():
                    to_language_key = key
            
            words = textblob.TextBlob(self.original_text.get(1.0, tk.END))
            words = words.translate(from_lang=from_language_key, to=to_language_key)
            self.translated_text.insert(1.0, words)
        except Exception as e:
            messagebox.showerror("TranslateApp", e)
    
    def clear(self):
        self.original_text.delete(1.0, tk.END)
        self.translated_text.delete(1.0, tk.END)

if __name__ == "__main__":
    window = TranslateApp()
    window.mainloop()