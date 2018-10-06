import Adafruit_DHT as dht
import RPi.GPIO as gpio
import psycopg2
import requests

sensor = dht.DHT11
gpio.setmode(gpio.BOARD)
pino_sensor = 4
url = 'https://api.thingspeak.com/update'
api_key = 'UUOSB2RRTG29Q0J1'

connect = psycopg2.connect(
    host='192.168.0.106',
    database='postgres',
    user='postgres',
    password='postgres'
)
cursor = connect.cursor()

umid, temp = dht.read_retry(sensor, pino_sensor)

sql = f"""
    INSERT INTO dados_temp_umid (temperatura, umidade)
    VALUES ({temp:.2f}, {umid:.2f})"""
cursor.execute(sql)
connect.commit()
connect.close()

response = requests.get(f'{url}?api_key={api_key}&field1={temp}&field2={umid}')
