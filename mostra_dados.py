from datetime import datetime

import psycopg2
from pytz import timezone

connect = psycopg2.connect(
    host='192.168.0.106',
    database='postgres',
    user='postgres',
    password='postgres'
)
cursor = connect.cursor()

sql2 = f"""SELECT * FROM dados_temp_umid"""

cursor.execute(sql2)

linhas = cursor.fetchall()

print('Os dados que temos até o momento são do dia e hosras abaixo:\n')

for linha in linhas:
    data_hora = linha[3].astimezone(timezone('America/Sao_Paulo'))
    print(
        f"""Em {datetime.strftime(data_hora, '%d-%m-%Y as %H:%M:%S')} a Temperatura estava {linha[1]:.2f}ºC e a Umidade Relativa do Ar em {linha[2]:.2f}%""")
connect.close()
