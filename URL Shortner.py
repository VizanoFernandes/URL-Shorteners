import tkinter as tk
from tkinter import messagebox
import pyshorteners
import pyperclip

def shorten_url():
    url = url_input.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL to shorten.")
        return

    try:
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(url)
        output_label.config(text=f"Shortened URL: {shortened_url}")

        # Copy to clipboard
        pyperclip.copy(shortened_url)
        messagebox.showinfo("Success", "Shortened URL copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("URL Shortener")

# Input field
tk.Label(root, text="Enter URL to shorten:", font=("Arial", 12)).pack(pady=10)
url_input = tk.Entry(root, width=50, font=("Arial", 12))
url_input.pack(pady=5)

# Shorten button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, font=("Arial", 12))
shorten_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.pack(pady=10)

# Run the GUI
root.geometry("500x300")
root.mainloop()
