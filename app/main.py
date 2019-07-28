from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ListProperty

from plyer import tts

from random import random

class MyApp(App):
    text_input = StringProperty()
    label_color = ListProperty()

    def build(self):
        pass

    def update_text(self, text_str):
        self.text_input = text_str
        self.label_color = [random() for i in range(3)] + [1]

    def speak(self):
        tts.speak(self.text_input)

if __name__ == "__main__":
    MyApp(title='Speak').run()
