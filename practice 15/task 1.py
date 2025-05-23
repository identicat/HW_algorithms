import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Погода")
        self.root.geometry("420x680")
        self.api_key = "2fc5ef54be1e73cd01230fb93bc08b44"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Погода", font=("Verdana", 22, "bold"), bg='#416aaf', fg="white")
        self.title_label.pack(pady=30)
        self.city_label = tk.Label(self.root, text="Введите город:", font=("Verdana", 14), bg='#416aaf', fg="white")
        self.city_label.pack(pady=10)
        self.city_entry = tk.Entry(self.root, font=("Verdana", 12), width=22)
        self.city_entry.pack()
        self.search_button = tk.Button(self.root, text="Узнать погоду", font=("Verdana", 12), command=self.get_weather, bg="#FFFCFC", fg="#0f3676")
        self.search_button.pack(pady=15)
        self.weather_frame = tk.Frame(self.root, bg='#416aaf')
        self.weather_frame.pack(pady=20)
        self.location_label = tk.Label(self.weather_frame, text="", font=("Verdana", 16), bg='#416aaf', fg="white")
        self.location_label.pack()
        self.temp_label = tk.Label(self.weather_frame, text="", font=("Verdana", 22), bg='#416aaf', fg="white")
        self.temp_label.pack()
        self.weather_desc = tk.Label(self.weather_frame, text="", font=("Verdana", 14), bg='#416aaf', fg="white")
        self.weather_desc.pack()
        self.weather_icon = tk.Label(self.weather_frame, bg='#416aaf')
        self.weather_icon.pack()
        self.details_label = tk.Label(self.weather_frame, text="", font=("Verdana", 12), bg='#416aaf', fg="white")
        self.details_label.pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите название города")
            return
        try:
            params = {'APPID': self.api_key, 'q': city, 'units': 'metric', 'lang': 'ru'}
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if data["cod"] != 200:
                messagebox.showerror("Ошибка", "Город не найден")
                return
            main_data = data["main"]
            weather_data = data["weather"][0]
            sys_data = data["sys"]
            self.location_label.config(text=f"{data['name']}, {sys_data['country']}")
            self.temp_label.config(text=f"{main_data['temp']}°C")
            self.weather_desc.config(text=weather_data["description"].capitalize())
            icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = Image.open(BytesIO(icon_response.content))
            icon = ImageTk.PhotoImage(icon_data)
            self.weather_icon.config(image=icon)
            self.weather_icon.image = icon
            details = (f"Ощущается как: {main_data['feels_like']}°C\n"
                       f"Влажность: {main_data['humidity']}%\n"
                       f"Давление: {main_data['pressure']} hPa\n"
                       f"Ветер: {data['wind']['speed']} м/с")
            self.details_label.config(text=details)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось получить данные о погоде: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#416aaf')
    app = WeatherApp(root)
    root.mainloop()
