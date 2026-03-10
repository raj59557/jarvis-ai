from kivy.app import App
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        return Label(text="Jarvis AI Started")

JarvisApp().run()
