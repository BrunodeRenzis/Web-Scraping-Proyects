import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.157 Safari/537.36"
}
url = "https://stackoverflow.com/questions"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, features='lxml')

questionsContainer = soup.find('div', id="questions")
questionsList = questionsContainer.find_all('div', class_="question-summary")

for question in questionsList:
    requestText = question.find('h3').text
    questionDesc = question.find(class_='excerpt').text
    questionDesc = questionDesc.replace('\n', '').strip()
    print(requestText)
    print(questionDesc)
