from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class SwitchhSlider(GridLayout):
    #Variables
    Labeltext =StringProperty("0")
    SliderEnbaled = BooleanProperty(False)

    def ReadSlider(self, SliderValues):
        self.Labeltext = str(int(SliderValues.value))
    def ReadSwitch(self, SwitchValues):
        if SwitchValues.active:
            self.SliderEnbaled = True
        else:
            self.SliderEnbaled = False


class SwitchAliderApp(App):
    pass


SwitchAliderApp().run()

