screen_helper = '''
ScreenManager:
    id: screen_manager
    LoginScreen:
    MenuScreen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: 'GabAI Chatbot'      
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("toggle")]]      
                            elevation: 2
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                drawer_type: 'right'
                size_hint_x: None
                width: dp(250)
                radius: 0, dp(1), dp(1), 0
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'                   
                    Image:
                        source: 'profile_pic.jpg'
                        halign: 'left'
                    MDLabel:
                        text: 'Cyril John Ypil'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: 'cyrilypil@gmail.com'
                        font_style: 'Caption'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDList:
                        OneLineIconListItem:
                            on_release: screen_manager.current = 'profile'
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-man-profile'
                        OneLineIconListItem:
                            text: 'Settings'
                            IconLeftWidget:
                                icon: 'account-settings'
                        OneLineIconListItem:
                            on_release: screen_manager.current = 'login'
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
                    Widget:
    ProfileScreen:
    ChatbotScreen:

<LoginScreen>:
    name: 'login'
    Image:
        source: 'img_3.png'
        halign: "center"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    MDLabel:
        text: "GabAi"
        font_style: "H4"
        halign: "center"
        pos_hint: {'center_x': 0.5, 'center_y': 0.54}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_dark
    MDTextField:
        id: idno_field
        mode: "rectangle"
        hint_text: "IDNO"
        helper_text_mode: "persistent"
        size_hint_x: 0.69
        pos_hint: {'center_x': 0.5, 'center_y': 0.42}
        
    MDTextField:
        id: password_field
        mode: "rectangle"
        hint_text: "Password"
        helper_text_mode: "persistent"
        password: True
        size_hint_x: 0.69
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
    
    MDFillRoundFlatButton:
        style: 'elevated'
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.18}
        size_hint_x: 0.5
        on_press: app.login(idno_field.text, password_field.text)

    FloatLayout:
        MDIconButton:
            icon: "eye-off"
            pos_hint: {"x": .65, "y": .24}
            on_release: app.toggle_password_visibility(password_field, self)


<MenuScreen>:
    name: 'menu'
    MDRoundFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRoundFlatButton:
        text: 'GabaAi'
        pos_hint: {'center_x':0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'chatbot'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Cyril!'
        halign: 'center'
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<ChatbotScreen>:
    name: 'chatbot'
    MDLabel:
        text: 'Ask GabAI anything...'
        halign: 'center'
    MDTextField:
        mode: "rectangle"
        hint_text: "Ask GabAi"
        helper_text: "Say hi to Gab!"
        helper_text_mode: "persistent"
        icon_right: "send"
        pos_hint: {'center_x':0.5, 'center_y': 0.2}
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.8, 'center_y': 0.9}
        on_press: root.manager.current = 'menu'
'''
