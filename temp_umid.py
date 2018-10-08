import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import psycopg2
import requests
from decouple import config

sensor = DHT.DHT11
GPIO.setmode(GPIO.BOARD)
pino_sensor = 4
url = 'https://api.thingspeak.com/update'
api_key = config('API_KEY')

umid, temp = DHT.read_retry(sensor, pino_sensor)

connect = psycopg2.connect(
    host='192.168.0.115',
    database='postgres',
    user='postgres',
    password='postgres'
)
cursor = connect.cursor()

sql = f"""INSERT INTO dados_temp_umid (temperatura, umidade) VALUES ({temp}, {umid})"""
cursor.execute(sql)
connect.commit()
connect.close()

response = requests.get(f'{url}?api_key={api_key}&field1={temp}&field2={umid}')
