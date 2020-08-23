import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.157 Safari/537.36"
}
url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text)

contenedorPreguntas = soup.find('div', id="questions")
listaPreguntas = contenedorPreguntas.find_all('div', class_="question-summary")

for pregunta in listaPreguntas:
    requestText=pregunta.find('h3').text
    questionDesc = pregunta.find(class_='excerpt').text
    questionDesc = questionDesc.replace('\n', '').strip()
    print(requestText)
    print(questionDesc)

    print()