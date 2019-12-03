import kivy
kivy.require("1.2.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class MyW(Widget):
    def my_callback(self):
        self.ids.label1.text = "click!  "
    def my_callback1(self,inpt):
        self.ids.label1.text= "Enter !"+ str(inpt)


class EE1App(App):
    def build(self):
        return MyW()

if __name__ =="__main__":
    EE1App().run()