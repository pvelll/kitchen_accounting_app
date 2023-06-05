from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class KitchenApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.clean_kitchens = []
        self.dirty_kitchens = []
        for i in range(2, 14):
            for j in range(1, 3):
                kitchen_number = f'{i}.{j}'
                btn = Button(text=kitchen_number)
                btn.bind(on_press=self.mark_kitchen)
                layout.add_widget(btn)
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        return layout

    def mark_kitchen(self, instance):
        kitchen_number = instance.text
        if kitchen_number in self.clean_kitchens:
            self.clean_kitchens.remove(kitchen_number)
            self.dirty_kitchens.append(kitchen_number)
            instance.background_color = (1, 0, 0, 1)
        else:
            if kitchen_number in self.dirty_kitchens:
                self.dirty_kitchens.remove(kitchen_number)
            self.clean_kitchens.append(kitchen_number)
            instance.background_color = (0, 1, 0, 1)
        self.result_label.text = f'Чистые кухни : {self.clean_kitchens}\nГрязные кухни: {self.dirty_kitchens}'

KitchenApp().run()