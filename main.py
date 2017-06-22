import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock


class ScreenOne(Screen):
    status = ObjectProperty(None)
    time = StringProperty()
    ampel_oben = ObjectProperty(None)
    ampel_mitte = ObjectProperty(None)
    ampel_unten = ObjectProperty(None)
    color = 'RED'

    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.ampel_oben = ObjectProperty(None)
        self.ampel_mitte = ObjectProperty(None)
        self.ampel_unten = ObjectProperty(None)
        with open("data/status_ampel.json") as json_data:
            d = json.load(json_data)
            self.color = d.get('phase')
            self.time = str(d.get('seconds'))

            if self.color == 'GREEN':
                self.status = "FAHR\nZUA!"
                self.ampel_oben = (0.5, 0.5, 0.5)
                self.ampel_mitte = (0.5, 0.5, 0.5)
                self.ampel_unten = (0.13, 0.545, 0.13)
            elif self.color == 'RED':
                self.status = "HALT!"
                self.ampel_oben = (0.86, 0.078, 0.23)
                self.ampel_mitte = (0.5, 0.5, 0.5)
                self.ampel_unten = (0.5, 0.5, 0.5)
            elif self.color == "YELLOW":
                self.status = "OBACHT!"
                self.ampel_oben = (0.5, 0.5, 0.5)
                self.ampel_mitte = (1, 0.84, 0)
                self.ampel_unten = (0.5, 0.5, 0.5)
            else:
                self.status = "OBACHT!"
                self.ampel_oben = (0.86, 0.078, 0.23)
                self.ampel_mitte = (1, 0.84, 0)
                self.ampel_unten = (0.5, 0.5, 0.5)

    def update(self, dt):

        with open("data/status_ampel.json") as json_data:
            d = json.load(json_data)
            color = d.get('phase')
            self.time = str(d.get('seconds'))

        if color == 'GREEN':
            self.status = "FAHR\nZUA!"
            self.ampel_oben = (0.5,0.5,0.5)
            self.ampel_mitte = (0.5,0.5,0.5)
            self.ampel_unten = (0.13, 0.545, 0.13)
        elif color == 'RED':
            self.status = "HALT!"
            self.ampel_oben = (0.86,0.078,0.23)
            self.ampel_mitte = (0.5,0.5,0.5)
            self.ampel_unten = (0.5,0.5,0.5)
        elif color == "YELLOW":
            self.status = "OBACHT!"
            self.ampel_oben = (0.5,0.5,0.5)
            self.ampel_mitte = (1,0.84,0)
            self.ampel_unten = (0.5,0.5,0.5)
        else:
            self.status = "OBACHT!"
            self.ampel_oben = (0.86, 0.078, 0.23)
            self.ampel_mitte = (1,0.84,0)
            self.ampel_unten = (0.5,0.5,0.5)




class ScreenTwo(Screen):
    speed = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        with open("data/speed_vehicle.txt", 'r') as speed_data:
            self.speed = speed_data.readline() + " km/h"

    def update(self, dt):
        with open("data/speed_vehicle.txt", 'r') as speed_data:
            self.speed = speed_data.readline() + " km/h"



class ScreenThree(Screen):
    capacity = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        with open("data/spannung_vehicle.txt", 'r') as spannung_data:
            self.capacity = spannung_data.readline() + " V"


    def update(self, dt):
        with open("data/spannung_vehicle.txt", 'r') as spannung_data:
            self.capacity = spannung_data.readline() + " V"



class My_manager(ScreenManager):

    def update(self, dt):
        self.current_screen.update(self)



class DisplayApp(App):

    def build(self):
        root = My_manager()
        Clock.schedule_interval(root.update, 1.0 / 60.0)
        return root

if __name__ == '__main__':
    DisplayApp().run()
