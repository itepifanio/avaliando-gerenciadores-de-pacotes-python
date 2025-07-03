import my_requests 

def main():
    # request fantasia
    my_requests.post(
        "apyb.python.org.br/associados/associa-se", 
        json={
            "tipo": "membro-efetivo",
            "pagamento": "pix",
            "valor_anual": "64.0",
        }
    )
