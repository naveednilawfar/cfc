#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.widget import MDAdaptiveWidget
from kivymd.uix.snackbar import Snackbar

# CFC is a python program with kivy as the frontend GUI which
# converts celsius to fahrenheit or fahrenheit to celsius.

__version__ = "1.6.5"
__author__ = "Naveed Nilawfar"


Builder.load_file('main.kv')


class CFCLayout(MDAdaptiveWidget):
    """The root Widget of CFC"""

    def c2f_cal(self):
        """Converts celsius into farenheit"""
        self.ids.afarenheit.text = ""
        if self.ids.scelsius.text == "":
            c2f_error = Snackbar(
                text="You haven't entered any value to convert into farenheit"
                )
            c2f_error.open()
        else:
            answer = ""
            self.ids.afarenheit.text = ""
            c = self.ids.scelsius.text
            answer = (float(c)*1.8)+32
            self.ids.afarenheit.text = f'{answer}'

    def f2c_cal(self):
        """Converts farenheit into celsius"""
        self.ids.acelsius.text = ""
        if self.ids.sfarenheit.text == "":
            f2c_error = Snackbar(
                text="You haven't entered any value to convert into celsius"
                )
            f2c_error.open()
        else:
            answer = ""
            self.ids.acelsius.text = ""
            f = self.ids.sfarenheit.text
            answer = (float(f)-32)*5/9
            self.ids.acelsius.text = f'{answer}'


class CFCApp(MDApp):
    """The app instance of CFC"""

    def build(self):
        """build the app"""
        self.title = 'CFConverter'
        self.icon = 'images/icon9.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return CFCLayout()


if __name__ == '__main__':
    CFCApp().run()
