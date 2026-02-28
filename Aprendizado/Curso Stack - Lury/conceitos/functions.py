from datetime import datetime

def today():
    today = datetime.now()
    return today

def vereficar_data(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception("Entrada invalida! Use: DD-MM-AAAA")

def vereficar_vencimento(date_ref):
    data_vencimento = vereficar_data(date=date_ref)
    if today() > data_vencimento:
        return "VENCIDO"
    else:
        return "SAUDAVEL"