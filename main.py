import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty

class My_manager(ScreenManager):
    pass

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

#class ScreenThree(Screen):
#    pass

class DisplayApp(App):

    def build(self):
        root = My_manager()
        #root.add_widget(ScreenOne(name="screen_one"))
        #root.add_widget(ScreenTwo(name="screen_two"))
        #root.add_widget(ScreenThree(name="screen_three"))
        #for x in range(4):
        #    root.add_widget(CustomScreen(name="Screen %d" % x))
        return root

if __name__ == '__main__':
    DisplayApp().run()