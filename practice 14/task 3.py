from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class IceCreamApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Кафе-мороженое")
        window_width = 650
        window_height = 460
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        style = ttk.Style()
        style.configure("Blue.TFrame", background="#fde8f0")
        style.configure("Blue.TLabel", background="#fde8f0")
        style.configure("Blue.TButton", background="#fde8f0")

        image = Image.open("ice cream shop.jpg")
        image = image.resize((650, 460))
        self.bg_image = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.flavors_by_type = {
            "в стаканчике": ["пломбир", "шоколад"],
            "на палочке": ["ваниль", "шоколад"],
            "мягкое": ["пломбир", "клубника"]
        }

        self.setup()
        self.root.mainloop()

    def setup(self):
        text_frame = ttk.Frame(self.root)
        text_frame.place(x=210, y=150, width=180, height=254)

        text_scroll = ttk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.flavors_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set,
                                    font=('Verdana', 10), bg="#fde8f0", padx=10, pady=10)
        self.flavors_text.pack(fill=tk.BOTH, expand=True)
        text_scroll.config(command=self.flavors_text.yview)

        self.flavors_text.config(state="disabled")

        self.update_flavors()

        input_frame = ttk.Frame(self.root, style="Blue.TFrame")
        input_frame.place(x=390, y=150, width=199, height=254)

        self.type_label = ttk.Label(input_frame, text="Тип:", style="Blue.TLabel")
        self.type_label.place(x=10, y=10)
        self.type_entry = ttk.Entry(input_frame)
        self.type_entry.place(x=50, y=10, width=140)

        self.flavor_label = ttk.Label(input_frame, text="Вкус:", style="Blue.TLabel")
        self.flavor_label.place(x=10, y=45)
        self.flavor_entry = ttk.Entry(input_frame)
        self.flavor_entry.place(x=50, y=45, width=140)

        self.add_button = ttk.Button(input_frame, text="Добавить", command=self.add_flavor, style="Blue.TButton")
        self.add_button.place(x=10, y=85, width=85)

        self.del_button = ttk.Button(input_frame, text="Удалить", command=self.delete_flavor, style="Blue.TButton")
        self.del_button.place(x=104, y=85, width=85)

    def update_flavors(self):
        self.flavors_text.config(state="normal")
        self.flavors_text.delete(1.0, tk.END)

        text = ""
        for ice_type, flavors in self.flavors_by_type.items():
            text += f"{ice_type}: \n"
            for flavor in flavors:
                text += f" - {flavor}\n"
            text += "\n"
        self.flavors_text.insert(tk.END, text)

        self.flavors_text.config(state="disabled")

    def add_flavor(self):
        ice_type = self.type_entry.get().strip().lower()
        flavor = self.flavor_entry.get().strip().lower()
        if ice_type and flavor:
            if ice_type not in self.flavors_by_type:
                self.flavors_by_type[ice_type] = []
            if flavor not in self.flavors_by_type[ice_type]:
                self.flavors_by_type[ice_type].append(flavor)
            self.update_flavors()
        self.type_entry.delete(0, tk.END)
        self.flavor_entry.delete(0, tk.END)

    def delete_flavor(self):
        ice_type = self.type_entry.get().strip().lower()
        flavor = self.flavor_entry.get().strip().lower()
        if ice_type in self.flavors_by_type:
            if flavor in self.flavors_by_type[ice_type]:
                self.flavors_by_type[ice_type].remove(flavor)
                if not self.flavors_by_type[ice_type]:
                    del self.flavors_by_type[ice_type]
                self.update_flavors()
        self.type_entry.delete(0, tk.END)
        self.flavor_entry.delete(0, tk.END)


IceCreamApp()
