import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton('Get Weather', self)
        self.temperature_label = QLabel("35°C", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

        self.iniUI()

    def iniUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_btn)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)
        self.setLayout(layout)

        # Aligne items to center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Style the widgets
        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_btn.setObjectName('get_weather_btn')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        self.setStyleSheet("""
            QLabel, QPushButton {
                           font-family: 'Roboto';
                           font-size: 20px;
            }
            #city_label {
                font-size: 25px;
            }
            #city_input {
                font-size: 20px;
                padding: 5px;
            }
            #get_weather_btn {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            #get_weather_btn:hover {
                background-color: #2980b9;
            }
            #temperature_label {
                font-size: 50px;
            }
            #emoji_label {
                font-size: 50px;
                font-family: 'Segoe UI Emoji';
            }
            #description_label {
                font-size: 30px;
            }
                            """)

        self.setGeometry(800, 400, 400, 400)
        self.setWindowTitle('Weather App')

        self.get_weather_btn.clicked.connect(self.get_weather)
        
    def get_weather(self):
        city = self.city_input.text()
        api_key = '9ee5a1eb2c4e639323ecc63748b3493c'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data['main']['temp'] - 273.15, data['weather'][0]['description'], data['weather'][0]['id'])
                
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 401:
                    self.display_error('Invalid API key')
                case 403:
                    self.display_error('API key has exceeded requests limit')
                case 404:
                    self.display_error('City not found')
                case 500:
                    self.display_error('Server error')
                case 502:
                    self.display_error('Bad gateway')
                case 503:
                    self.display_error('Service unavailable')
                case 504:
                    self.display_error('Gateway timeout')
                case _:
                    self.display_error(f'An error occurred: {http_error}')
            
        except requests.exceptions.ConnectionError:
            self.display_error('Connection error')
        
        except requests.exceptions.Timeout:
            self.display_error('Request timed out')
        
        except requests.exceptions.TooManyRedirects:
            self.display_error('Too many redirects')     
         
        except requests.exceptions.RequestException as req_error: # Catch all other exceptions
            self.display_error(f"An error occurred: {req_error}")
    
    def display_error(self, message):
        self.temperature_label.setStyleSheet('color: red;')
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        
    def display_weather(self, temperature, description, weather_id):
        self.temperature_label.setStyleSheet('color: black;')
        self.temperature_label.setText(f'{temperature:.0f}°C')
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)
        
    @staticmethod
    def get_weather_emoji(weather_id):
        if weather_id in range(200, 233):
            return '⛈️'
        elif weather_id in range(300, 322):
            return '🌧️'
        elif weather_id in range(500, 532):
            return '☔'
        elif weather_id in range(600, 623):
            return '❄️'
        elif weather_id in range(700, 782):
            return '🌫️'
        elif weather_id == 762:
            return '🌋'
        elif weather_id == 771:
            return '💨'
        elif weather_id == 781:
            return '🌪️'
        elif weather_id == 800:
            return '☀️'
        elif weather_id in range(801, 805):
            return '☁️'
        else:
            return '🤷'
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())