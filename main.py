import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
import json
from kivy.properties import ObjectProperty
import time as sleeper
from kivy.clock import Clock


class ScreenOne(Screen):
    status = ObjectProperty(None)
    time = ObjectProperty(None)
    ampel_oben = ObjectProperty(None)
    ampel_mitte = ObjectProperty(None)
    ampel_unten = ObjectProperty(None)

    with open("data/status_ampel.json") as json_data:
        d = json.load(json_data)
        color = d.get('phase')
        # time = d.get('seconds')
        # self.time = d.get('seconds')
        time = d.get('seconds')

    if color == 'GREEN':
        status = "FAHR\nZUA!"
        ampel_oben = (0.5,0.5,0.5)
        ampel_mitte = (0.5,0.5,0.5)
        ampel_unten = (0.13, 0.545, 0.13)
    elif color == 'RED':
        status = "HALT!"
        ampel_oben = (0.86,0.078,0.23)
        ampel_mitte = (0.5,0.5,0.5)
        ampel_unten = (0.5,0.5,0.5)
    elif color == "YELLOW":
        status = "OBACHT!"
        ampel_oben = (0.5,0.5,0.5)
        ampel_mitte = (1,0.84,0)
        ampel_unten = (0.5,0.5,0.5)
    else:
        status = "OBACHT!"
        ampel_oben = (0.86, 0.078, 0.23)
        ampel_mitte = (1,0.84,0)
        ampel_unten = (0.5,0.5,0.5)



    def update(self, dt):
        #status = ObjectProperty(None)
        #time = ObjectProperty(None)
        #color = "?"


        with open("data/status_ampel.json") as json_data:
            d = json.load(json_data)
            color = d.get('phase')
            #time = d.get('seconds')
            #self.time = d.get('seconds')
            #self.time_label.text = d.get('seconds')

        if color == 'GREEN':
            #status = "GO!"
            self.status = "GO!"
        elif color == 'RED':
            #status = "STOP!"
            self.status = "STOP!"
        else:
            #status = "WAIT!"
            self.status = "WAIT!"


    #def update(self, event):
    #    self.time_label.text = time
    #    self.status_label.text = status

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class My_manager(ScreenManager):
    pass

class DisplayApp(App):

    def build(self):
        root = My_manager()
        scrone = ScreenOne()
        Clock.schedule_interval(scrone.update, 1.0 / 60.0)
        return root

if __name__ == '__main__':
    DisplayApp().run()
