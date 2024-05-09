import openpyxl
import locale
import glob
import datetime
def monedaAFlotante(valor):
    if isinstance(valor, (int, float)):
        return valor
    try:
        return locale.atof(valor.strip("$"))
    except ValueError:
        return 0

inicio  = datetime.datetime.now()
print('Fecha y hora de inicio de la exportacion: ', inicio) 

        
        
        