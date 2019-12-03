import kivy.app
from kivy.uix.button import Button
import plyer

class PushNotificationApp(kivy.app.App):


    def show_notification(self):
        plyer.notification.notify(title='test', message="Notification using plyer")
    def build(self):
       return Button(text=" press",on_press=self.show_notification())


if __name__ == "__main__":
    PushNotificationApp().run()