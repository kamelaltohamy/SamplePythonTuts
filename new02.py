from kivy.app import App
from kivy.uix.button import Button
class MainApp(App):
    def build(self):
        button = Button(text="Hello from kivy",size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5})
        button.bind(on_press=self.on_press_button)

        return button
    def on_press_button(self, instance):
        print(' you have pressed the button ')
    

if __name__ == '__main__':
    app = MainApp()
    app.run()