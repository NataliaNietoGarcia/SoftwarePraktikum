
from kivymd.app import MDApp
from gpshelper import GpsHelper

class MainApp(MDApp):
    
    def on_start(self):
        
        GpsHelper().run()
        
MainApp().run()

