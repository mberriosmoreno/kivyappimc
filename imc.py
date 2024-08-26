from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class IMCApp(App):
    def build(self):
        self.title = "Calculadora de IMC"
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input para la altura
        self.altura_input = TextInput(hint_text="Ingrese su altura en metros (ej. 1.75)", multiline=False, input_filter='float')
        layout.add_widget(self.altura_input)
        
        # Input para el peso
        self.peso_input = TextInput(hint_text="Ingrese su peso en kilogramos (ej. 70)", multiline=False, input_filter='float')
        layout.add_widget(self.peso_input)
        
        # Botón para calcular el IMC
        calcular_btn = Button(text="Calcular IMC", on_press=self.calcular_imc)
        layout.add_widget(calcular_btn)
        
        # Etiqueta para mostrar el resultado del IMC
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)
        
        return layout
    
    def calcular_imc(self, instance):
        try:
            altura = float(self.altura_input.text)
            peso = float(self.peso_input.text)
            
            # Calcular el IMC
            imc = peso / (altura ** 2)
            
            # Clasificar el resultado
            if imc < 18.5:
                mensaje = f"IMC: {imc:.2f} - Bajo peso. \nConsejo: Intenta aumentar tu ingesta calórica y come alimentos nutritivos."
            elif 18.5 <= imc < 24.9:
                mensaje = f"IMC: {imc:.2f} - Peso normal. \nConsejo: Mantén una dieta balanceada y continúa con actividad física regular."
            elif 25 <= imc < 29.9:
                mensaje = f"IMC: {imc:.2f} - Sobrepeso. \nConsejo: Considera mejorar tu dieta y aumentar la actividad física."
            else:
                mensaje = f"IMC: {imc:.2f} - Obesidad. \nConsejo: Consulta con un profesional de la salud para un plan de acción adecuado."
            
            # Mostrar el resultado en la etiqueta
            self.result_label.text = mensaje
            
            # Popup con el mensaje
            popup = Popup(title="Resultado IMC", content=Label(text=mensaje), size_hint=(0.8, 0.5))
            popup.open()
        
        except ValueError:
            # Manejo de error si el input no es válido
            self.result_label.text = "Por favor, ingrese valores válidos para altura y peso."
            popup = Popup(title="Error", content=Label(text="Ingrese valores numéricos válidos."), size_hint=(0.8, 0.5))
            popup.open()

if __name__ == '__main__':
    IMCApp().run()
