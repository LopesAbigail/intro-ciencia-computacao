segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segs // (24*3600)
horas = (segs // 3600) - (24*dias)
segs_restantes = segs % 3600
minuts = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minuts, "minutos e", segs_restantes_final,"segundos.")
