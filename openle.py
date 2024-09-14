from openai import *
from kivy.app import App
from kivy.lang import Builder
Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    TextInput:
        id: text_input
        size_hint: 1, 0.1
    Button:
        text: 'Get Response'
        size_hint: 1, 0.1
        on_release: root.get_response()
    ScrollView:
        size_hint: 1, 0.8
        Label:
            id: response_label
            size_hint: None, None
            size: self.texture_size
            text_size: self.width, None
            halign: 'left'
            valign: 'top'
            text: ''
            markup: True
''')
import openai 

class MyApp(App):
    def get_response(self):
        message = self.ids.text_input.text
        openai = OpenAI()
        response = openai.get_response(message)
        self.ids.response_label.text = response
t=MyApp()
t.run()