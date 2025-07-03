import my_requests 

def request(url: str, json: dict):
    my_requests.post(
        url,
        json=json,
    )
