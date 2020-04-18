import pyRofex

pyRofex.initialize(user="matiasrivera364",
                   password="ePMoRh7@",
                   account="matiasrivera364",
                   environment=pyRofex.Environment.REMARKET)

print(pyRofex.get_all_instruments())