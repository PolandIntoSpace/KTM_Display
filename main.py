import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock

#Dieses Skript dient dazu live Daten aus Sensoren auszulesen. Im Moment können die folgenden Daten geladen werden;

pfad_ampel = "data/status_ampel.json"
pfad_geschwindigkeit = "data/speed_vehicle.txt"
pfad_spannung = "data/spannung_vehicle.txt"

# Das Skript ist einfach zu erweitern und wurde mit Hilfe der Python-Bibliothek Kivy (https://kivy.org/) verfasst.
# Zum Python-Skript gehört noch die Datei display.kv, in welcher die Oberflächenelemente erstellt/verwaltet werden.
# Stand: 26.06.2017, KTM, Gruppe Display


# Anzeige auf dem ersten Bild
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

        # Lade Informationen aus der JSON-Datei:
        with open(pfad_ampel) as json_data:
            d = json.load(json_data)
            self.color = d.get('phase')
            self.time = str(d.get('seconds')) # Setze die Zeit

            # Setze die Ampel mit Text und Farbe:
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


    # Für live Darstellung aktuallisiere das Vorgehen:
    def update(self, dt):

        with open(pfad_ampel) as json_data:
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
        with open(pfad_geschwindigkeit, 'r') as geschw_data:
            self.speed = geschw_data.readline() + " km/h"

    # Für live Darstellung aktuallisiere das Vorgehen:
    def update(self, dt):
        with open(pfad_geschwindigkeit, 'r') as geschw_data:
            self.speed = geschw_data.readline() + " km/h"



class ScreenThree(Screen):
    capacity = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        with open(pfad_spannung, 'r') as spannung_data:
            self.capacity = spannung_data.readline() + " V"

    # Für live Darstellung aktuallisiere das Vorgehen:
    def update(self, dt):
        with open(pfad_spannung, 'r') as spannung_data:
            self.capacity = spannung_data.readline() + " V"



class My_manager(ScreenManager):

    # Aktualisiere das Bild auf dem gerade aktiven Screen:
    def update(self, dt):
        self.current_screen.update(self)



class DisplayApp(App):
    # Erstelle die App
    def build(self):
        root = My_manager()

        # Timer, wie oft das aktuelle Bild aktualisiert werden soll:
        Clock.schedule_interval(root.update, 1.0 / 60.0)
        return root

if __name__ == '__main__':
    DisplayApp().run()
