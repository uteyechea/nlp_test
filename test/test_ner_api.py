import requests

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/"
    data = {"sentences": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
    }

    response = requests.post(url, json=data)

    print(response.json())