import datetime

def calcular_dias_de_vida(data):
    if data is None:
        error = 'ops'
        return error
    hoje = datetime.date.today()
    dias_de_vida = hoje - dia_de_nasc
    return dias_de_vida

dia_de_nasc = datetime.date(day=2, year=1935, month=2)

print(calcular_dias_de_vida(dia_de_nasc))

