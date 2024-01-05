from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RomanConverterApp(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical', padding=10, spacing=100,size_hint=(None, None),height=300,width=980)
        label = Label(text="Enter the Roman number:",size_hint=(None, None),height=100,width=980)
        self.roman_input = TextInput(size_hint=(None, None),height=40,width=980)
        convert_button = Button(text="Convert", on_press=self.convert_roman,size_hint=(None, None),height=300,width=980)
        layout.add_widget(label)
        layout.add_widget(self.roman_input)
        layout.add_widget(convert_button)

        return layout

    def prec(self, a, b):
        d = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
        if a.lower() in d and b.lower() in d:
            if d[a.lower()] > d[b.lower()]:
                return 1
            if d[a.lower()] < d[b.lower()]:
                return 2
        else:
            return 0

    def convert_roman(self, instance):
        roman = self.roman_input.text
        rl = list(roman)
        self.count = 0
        self.d = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

        for i in range(len(rl) - 1):
            a = self.prec(rl[i], rl[i + 1])
            if a == 0:
                self.roman_input.text = "Invalid Roman number"
                return
            elif a == 1:
                if(rl[i].lower()=="i"):
                    self.count+=1;
                if(rl[i].lower()=="v"):
                    self.count+=5;
                if(rl[i].lower()=="x"):
                    self.count+=10;
                if(rl[i].lower()=="l"):
                    self.count+=50;
                if(rl[i].lower()=="c"):
                    self.count+=100;
                if(rl[i].lower()=="d"):
                    self.count+=500;
                if(rl[i].lower()=="m"):
                    self.count+=1000;
            elif a == 2:
                if(rl[i].lower()=="i"):
                    self.count-=1
                if(rl[i].lower()=="v"):
                    self.count-=5;
                if(rl[i].lower()=="x"):
                    self.count-=10;
                if(rl[i].lower()=="l"):
                    self.count-=50;
                if(rl[i].lower()=="c"):
                    self.count-=100;
                if(rl[i].lower()=="d"):
                    self.count-=500;
                if(rl[i].lower()=="m"):
                    self.count-=1000;
                

        self.count += self.d[rl[-1].lower()]

        if self.count <= 0:
            self.roman_input.text = "Invalid Roman number"
        else:
            self.roman_input.text = f"{self.count}"

if __name__ == '__main__':
    RomanConverterApp().run()
