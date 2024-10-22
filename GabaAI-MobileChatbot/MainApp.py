from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarListItem, IconLeftWidget, ImageLeftWidget, ImageRightWidget
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

list_helper = '''
Screen:
    ScrollView:
        MDList:
            id: container
'''
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        facebook = TwoLineAvatarListItem(
                ImageLeftWidget(
                    source="img.png"
                ),
                text='Facebook',
                secondary_text = 'Account',
                pos_hint={'top': 1}
            )
        table = MDDataTable(pos_hint={'center_x':0.5, 'center_y':0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            rows_num=10,
                            column_data=[
                                ("No.", dp(18)),
                                ("Food", dp(20)),
                                ("Calories", dp(20)),
                            ],
                            row_data = [
                                (1,"Burger","300"),
                                (2,"Hotdog","150"),
                                (3,"Donut","70"),
                                (4,"French Fries","270"),
                                (1, "Burger", "300"),
                                (2, "Hotdog", "150"),
                                (3, "Donut", "70"),
                                (4, "French Fries", "270"),
                                (4, "French Fries", "270"),
                                (4, "French Fries", "270"),
                            ]
                            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)

        screen.add_widget(facebook)
        screen.add_widget(table)

        return screen


    def check_press(self, instance_table,current_row):
        print(instance_table,current_row)
    def row_press(self, instance_table,instance_row):
        print(instance_table,instance_row)


DemoApp().run()