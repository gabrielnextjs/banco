from datetime import date, datetime, timedelta

agora = datetime.now()
hoje = date.today()

print(agora)
print(hoje)

print(f"Dia:      {agora.day}")
print(f"Mês:      {agora.month}")
print(f"Ano:      {agora.year}")
print(f"Hora:     {agora.hour}")
print(f"Minutos:  {agora.minute}")
print(f"Segundos: {agora.second}")

data_br = agora.strftime("%d/%m/%Y")
hora_br = agora.strftime("%H:%M:%S")
completo = agora.strftime("%d/%m/%Y às %H:%M")
nome_log = agora.strftime("log_%Y%m%d_%H%M%S.txt")

print(f"Relatório gerado em: {completo}")

data_string = "15/03/2026"
data_objeto = datetime.strptime(data_string, "%d/%m/%Y")
print(type(data_objeto))
print(data_objeto.year)

data_api = "2026-07-04T18:30:00"
data_api_obj = datetime.strptime(data_api, "%Y-%m-%dT%H:%M:%S")
print(data_api_obj.strftime("%d/%m/%Y %H:%M"))

vencimento_boleto = date(2026, 3, 10)
dias_restantes = vencimento_boleto - hoje
print(f"Faltam {dias_restantes.days} dias para o vencimento.")

amanha = agora + timedelta(days=1)
semana_passada = agora - timedelta(weeks=1)
daqui_1_mes = agora + timedelta(days=30)
em_2_horas = agora + timedelta(hours=2, minutes=30)

print(f"Amanhã:              {amanha.strftime('%d/%m/%Y')}")
print(f"Semana passada:      {semana_passada.strftime('%d/%m/%Y')}")
print(f"Daqui a 1 mês (30d): {daqui_1_mes.strftime('%d/%m/%Y')}")

inicio_processo = datetime.now()
fim_processo = datetime.now()
duracao = (fim_processo - inicio_processo).total_seconds()
print(f"Processo concluído em {duracao:.3f} segundos.")
