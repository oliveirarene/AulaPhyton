import datetime
from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = str(agora.year)[2:4]
print("{}/{:02d}/{}".format(dia,mes,ano))

hora = agora.hour
minuto = agora.minute
segundo = agora.second
print("\t{:02d}h \t{:02d}' \t{:02d}\" ".format(hora, minuto, segundo)) #usar barra invertida para escapar o caracter
