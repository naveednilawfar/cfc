#author = Naveed Nilawfar
#version = 1.6.5
#name = CFC

from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<CFCLayout>
	BoxLayout:
		orientation:'vertical'
		size: root.width, root.height
		MDToolbar:
			title: 'CFConverter'
			md_bg_color: .2,.2,.2,1
			specific_text_color: 1, 1, 1, 1

		MDBottomNavigation:
					
			MDBottomNavigationItem:
				name: 'c2fc'
				text: 'C2F'
				icon: 'temperature-celsius'
				
				MDTextField:
					id: scelsius
					hint_text: 'Enter Celsius to convert:'
					input_filter: 'float'
					halign: 'center'
					font_name:'fonts/digital.ttf'
					size_hint_x: None
					mode: "rectangle"
					max_text_length: 15
					helper_text_mode: "on_focus"
					helper_text: "Maximum lenght is 15"
					width: 500
					pos_hint: {"center_x": 0.5, "center_y": 0.6}
					
				MDLabel:
					id: afarenheit
					text: ""
					halign: 'center'
					font_name:'fonts/digital.ttf'
					size_hint_x: None
					width: root.width
					pos_hint: {"center_x": 0.5, "center_y": 0.5}
					
				MDRaisedButton:
					text: "Caculate"
					font_name:'fonts/drawflygo.otf'
					size_hint_x: None
					width: 100
					pos_hint: {"center_x": 0.5, "center_y": 0.4}
					on_release: root.c2f_cal()
			
			MDBottomNavigationItem:
				name: 'f2cc'
				text: 'F2C'
				icon: 'temperature-fahrenheit'
					
				MDTextField:
					id: sfarenheit
					hint_text: 'Enter Farenheit to convert:'
					input_filter: 'float'
					halign: 'center'
					font_name:'fonts/digital.ttf'
					size_hint_x: None
					mode: "rectangle"
					max_text_length: 16
					helper_text_mode: "on_focus"
					helper_text: "Maximum lenght is 15"
					width: 500
					pos_hint: {"center_x": 0.5, "center_y": 0.6}
					
				MDLabel:
					id: acelsius
					text: ""
					halign: 'center'
					font_name:'fonts/digital.ttf'
					size_hint_x: None
					width: root.width
					pos_hint: {"center_x": 0.5, "center_y": 0.5}
				
				MDRaisedButton:
					text: "Caculate"
					font_name:'fonts/drawflygo.otf'
					size_hint_x: None
					width: 100
					pos_hint: {"center_x": 0.5, "center_y": 0.4}
					on_release: root.f2c_cal()
			
			MDBottomNavigationItem:
				name: 'abt'
				text: 'HELP'
				icon: 'help'

				MDLabel:
					text: "Celsius and Farenheit Converter version 1.0"
					font_name: 'fonts/stixtwotext.ttf'
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.6}
				
				MDLabel:
					text: "This program was created in kivy language by Naveed"
					font_name: 'fonts/stixtwotext.ttf'
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.5}
					
				MDLabel:
					text: "You can find the source code of this at"
					font_name: 'fonts/stixtwotext.ttf'
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.4}
					
				MDLabel:
					text: "https://github.com/naveednilawfar/cfc"
					multiline: "true"
					halign: 'center'
					pos_hint: {"center_x": 0.5, "center_y": 0.3}
""")

class CFCLayout(Widget):
    
    def c2f_cal(self):
        self.ids.afarenheit.text = ""
        if (self.ids.scelsius.text == ""):
            cpopupl = BoxLayout(orientation='vertical', size=(self.width, self.height))
            cpopuplbl = Label(text="You haven't entered any value to convert into farenheit")
            cpopupbtn = Button(text="OK")
            cpopup = Popup(title='Value Error', title_align='center', content=cpopupl, auto_dismiss=True, size_hint=(1.0,0.2), pos_hint={"center_x": 0.5, "center_y": 0.5})
            cpopupbtn.bind(on_release=cpopup.dismiss)
            cpopupl.add_widget(cpopuplbl)
            cpopupl.add_widget(cpopupbtn)
            cpopup.open()
        else:
            answer = ""
            self.ids.afarenheit.text = ""
            c = self.ids.scelsius.text
            answer = (float(c)*1.8)+32
            self.ids.afarenheit.text = f'{answer}'
            
    def f2c_cal(self):
        self.ids.acelsius.text = ""
        if (self.ids.sfarenheit.text == ""):
            fpopupl = BoxLayout(orientation='vertical', size=(self.width, self.height))
            fpopuplbl = Label(text="You haven't entered any value to convert into celsius")
            fpopupbtn = Button(text="OK")
            fpopup = Popup(title='Value Error', title_align='center', content=fpopupl, auto_dismiss=True, size_hint=(1.0,0.2), pos_hint={"center_x": 0.5, "center_y": 0.5})
            fpopupbtn.bind(on_release=fpopup.dismiss)
            fpopupl.add_widget(fpopuplbl)
            fpopupl.add_widget(fpopupbtn)
            fpopup.open()
        else:
            answer = ""
            self.ids.acelsius.text = ""
            f = self.ids.sfarenheit.text
            answer = (float(f)-32)*5/9
            self.ids.acelsius.text = f'{answer}'

class CFCApp(MDApp):
    def build(self):
        self.title = 'CFConverter'
        self.icon = 'images/icon9.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return CFCLayout()
        

CFCApp().run()