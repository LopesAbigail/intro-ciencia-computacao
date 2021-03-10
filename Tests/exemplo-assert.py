def retorna_salario(hora_semana, salario_hora = 40):
    assert hora_semana >= 0 and salario_hora >= 0
    return hora_semana * salario_hora

def testa():
    x = 10
    x += 10
    x /= 2
    x //= 3
    x %= 2
    x *= 9
    print(x)

def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s

    print(horario_em_segundos(3,0,50))

def calculo(x, y = 10, z = 5):
    return x + y * z;


