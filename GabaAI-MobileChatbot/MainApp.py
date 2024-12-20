from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from screen_nav import screen_helper

Window.size = (300, 500)

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class ChatbotScreen(Screen):
    pass
class LoginScreen(Screen):
    pass

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.primary_hue = '900'
        screen = Builder.load_string(screen_helper)
        return screen

    def login(self, idno, password):
        print(f'IDNO: {idno}, Password: {password}')
        if idno == 'admin' and password =='user':
            self.root.current = 'menu'

    def toggle_password_visibility(self, text_field, icon_button):
        # Toggle the password visibility
        if text_field.password:
            text_field.password = False  # Show password
            icon_button.icon = "eye"  # Change icon to "eye"
        else:
            text_field.password = True  # Hide password
            icon_button.icon = "eye-off"  # Change icon to "eye-off"

    def navigation_draw(self):
        print('Navigation')

    def account_draw(self):
        print('User Account')

DemoApp().run()
