navdrawer = '''
MDNavigationLayout:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: 'GabAI Chatbot'      
                    right_action_items: [['menu', lambda x: nav_drawer.set_state("toggle")]]      
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
            MDList:
                OneLineListItem:
                    text: 'Item 1'
                OneLineListItem:
                    text: 'Item 2'
                OneLineListItem:
                    text: 'Item 3'
            Widget: 
'''