diasDaSemana = {"dia1": "Domingo", "dia2": "Segunda", "dia3": "Terça", "dia4": "Quarta", "dia5": "Quinta", "dia6":
                "Sexta", "dia7": "Sábado"}

diasDaSemana.popitem()
diasDaSemana.popitem()
del(diasDaSemana["dia2"])
print(diasDaSemana.keys())
print(diasDaSemana.values())
print(diasDaSemana)
