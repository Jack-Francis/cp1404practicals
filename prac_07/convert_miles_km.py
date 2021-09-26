from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.609


class ConvertMilesKmApp(App):
    output_km = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KM_CONVERSION)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()
