from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import kivy
import kivymd

class CFC(Widget):
    
    def c2f_cal(self):
        if (self.celsius.text() == ""):
            popup = Popup(title='Value Error', content=Label(text="You haven't entered any value to convert into farenheit"), auto_dismiss=False)
            popup.open()
        else:
            c = self.celsius.text()
            answer = (float(c)*1.8)+32
            self.afarenheit.text(answer)
            
    def f2c_cal(self):
        if (self.scelsius.text() == ""):
            popup = Popup(title='Value Error', content=Label(text="You haven't entered any value to convert into celsius"), auto_dismiss=False)
            popup.open()
        else:
            f = self.celsius.text()
            answer = (float(f)-32)*5/9
            self.acelsius.text(answer)

class CFCApp(MDApp):
    
    def build(self):
        self.title = 'CFConverter'
        self.icon = 'images/c2f.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("main.kv")
        
if __name__ == "__main__":
    CFCApp().run()