# e:\Python\FirstProgram\dataehora.py
# Now, we're importing the 'date' class directly from the 'datetime' module.
# This lets us use 'date' without having to write 'datetime.date' every time.
from datetime import date
from datetime import datetime
from datetime import timedelta
import pytz

# Here, we're creating a date object using the 'date' class from 'datetime'.
# We give it the year (2025), the month (3 for March), and the day (5).
# This 'd' variable now holds the date March 5th, 2025.
d = date(2025, 3, 5)

# We're creating another date object using the 'date' class that we imported directly.
# This time, we're creating the date July 10th, 2023.
# We can write only date(2023,7,10) because we have already imported it on the "from datetime import date" line.
data = date(2023, 7, 10)

# This line will print the value of the 'd' variable to the console.
# It will show the date we created above, in the format YYYY-MM-DD.
print(d)  # Output: 2025-03-05

# This line will print the value of the 'data' variable to the console.
# It will show the date we created above, in the format YYYY-MM-DD.
print(data)  # Output: 2023-07-10

# That's all! This file shows how to create and print simple date objects.

d = d + timedelta(weeks=1)
print(d)  # Output: 2025-03-12

tipo_carro = "P"
tempo_pequeno = 12
tempo_medio = 20
tempo_grande = 30

data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)    

print("Data e hora atual: ", data_atual)
print("Data e hora estimada: ", data_estimada)

print(date.today())
print(date.today() - timedelta(days=1))

resultado = datetime(2023,7,25,10,19,20) - timedelta(hours=1)
print(resultado)
print(resultado.time())

print(resultado.date())

d= datetime.now()

print(d.strftime("%d/ %m/ %Y %H:%M:%S"))

date_string = "25/12/2023 10:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)


data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"
mascara_jpn = "%Y年%m月%d日 %H時%M分%S秒"

print(data_hora_atual.strftime(mascara_ptbr))
print(data_hora_atual.strftime(mascara_en))
print(data_hora_atual.strftime(mascara_jpn))

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))   

print(data)
print(data2)


