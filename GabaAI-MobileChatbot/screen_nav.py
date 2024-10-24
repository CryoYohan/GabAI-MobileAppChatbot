screen_helper = '''
ScreenManager:
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
                drawer_type: 'right'  # This ensures the drawer opens from the right side
                size_hint_x: None
                width: dp(250)  # Set the desired width here
                radius: 0, dp(1), dp(1), 0
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'                   
                    Image:
                        source: 'profile_pic.jpg'
                        halign:'left'
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
                            text: 'Profile'
                            IconLeftWidget:
                                icon:'face-man-profile'
                        OneLineIconListItem:
                            text: 'Settings'
                            IconLeftWidget:
                                icon:'account-settings'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon:'logout'
                                
                    Widget: 
    ProfileScreen:
    ChatbotScreen:
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

<ProfileScreen>
    name: 'profile'
    MDLabel:
        text: 'Welcome Cyril!'
        halign: 'center'
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<ChatbotScreen>
    name: 'chatbot'
    MDLabel:
        text: 'Ask GabAI anything...'
        halign: 'center'
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'


'''