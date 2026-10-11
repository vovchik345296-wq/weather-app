from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import requests

class WeatherRoot(BoxLayout):
    city = StringProperty("Moscow")
    result = StringProperty("Введите город и нажмите кнопку")

    def get_weather(self):
        city = self.city.strip() or "Moscow"
        self.result = "Загрузка..."
        try:
            url = f"https://wttr.in/{city}?format=4&m&lang=ru"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            self.result = response.text.strip()
        except Exception as e:
            self.result = f"Ошибка: {e}"

class WeatherApp(App):
    def build(self):
        return WeatherRoot()

if __name__ == "__main__":
    WeatherApp().run()
