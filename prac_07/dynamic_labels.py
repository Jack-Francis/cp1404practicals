from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {"Lindsay Ward", "Jack Francis", "Ayla Gunawan", "Joseph Hallows", "Joshua Finch"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        """Create labels from list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_label(temp_label)


DynamicLabelsApp().run()
