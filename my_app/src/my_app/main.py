from time import sleep
from my_django.main import request

def main() -> None:
    while True:
        request(
            url="apyb.python.org.br/associados/associa-se",
            json={
                "tipo": "membro-efetivo",
                "pagamento": "pix",
                "valor_anual": "64.0",
            }
        )
        sleep(1)

if __name__ == "__main__":
    main()
    