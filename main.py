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
        time = d.get('seconds')

    if color == 'GREEN':
        status = "FAHR\nZUA!"
        ampel_oben = (0.5, 0.5, 0.5)
        ampel_mitte = (0.5, 0.5, 0.5)
        ampel_unten = (0.13, 0.545, 0.13)
    elif color == 'RED':
        status = "HALT!"
        ampel_oben = (0.86, 0.078, 0.23)
        ampel_mitte = (0.5, 0.5, 0.5)
        ampel_unten = (0.5, 0.5, 0.5)
    elif color == "YELLOW":
        status = "OBACHT!"
        ampel_oben = (0.5, 0.5, 0.5)
        ampel_mitte = (1, 0.84, 0)
        ampel_unten = (0.5, 0.5, 0.5)
    else:
        status = "OBACHT!"
        ampel_oben = (0.86, 0.078, 0.23)
        ampel_mitte = (1, 0.84, 0)
        ampel_unten = (0.5, 0.5, 0.5)

    def update(self, dt):

        with open("data/status_ampel.json") as json_data:
            d = json.load(json_data)
            color = d.get('phase')
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




class ScreenTwo(Screen):
    speed = ObjectProperty(None)

    with open("data/speed_vehicle.txt", 'r') as speed_data:
        speed = speed_data.readline() + " km/h"

    #def update_speed(self, *args):
    #    with open("data/speed_vehicle.txt", 'r') as speed_data:
    #        self.speed = speed_data.readline() + " km/h"


    def update(self, dt):
        with open("data/speed_vehicle.txt", 'r') as speed_data:
            self.speed = speed_data.readline() + " km/h"


class ScreenThree(Screen):
    capacity = ObjectProperty(None)

    with open("data/spannung_vehicle.txt", 'r') as spannung_data:
        capacity = spannung_data.readline() + " V"

    #def update_spannung(self, *args):
    #    with open("data/spannung_vehicle.txt", 'r') as spannung_data:
    #        self.capacity = spannung_data.readline() + " V"


    def update(self, dt):
        #self.current_screen.update(dt)
        with open("data/spannung_vehicle.txt", 'r') as spannung_data:
            self.capacity = spannung_data.readline() + " V"

class My_manager(ScreenManager):

    #def update(self, dt):
        #self.current_screen.update(self, dt)
    pass

class DisplayApp(App):

    def build(self):
        root = My_manager()
        #self.one = ScreenOne(name='one')
        #self.two = ScreenTwo(name='two')
        #self.three = ScreenThree(name='three')
        #root.add_widget(self.one)
        #root.add_widget(self.two)
        #root.add_widget(self.three)
        Clock.schedule_interval(root.current_screen.update, 1.0 / 60.0)
        return root

if __name__ == '__main__':
    DisplayApp().run()
