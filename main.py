import requests
import re

class Checker:

    def __init__(self, nickname, region):
        available_regions = ['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oc', 'tr', 'ru']
        self.nickname = nickname
        self.region = region
        if (self.region in available_regions):
            self.url = f"https://lols.gg/en/name/checker/{self.region}/{self.nickname}/"
        else:
            print("Você inseriu uma região inválida!")
            exit()

    def send_request(self):
        r = requests.get(self.url)
        r = r.text
        return r

    def check_nickname_availability(self):
        r = self.send_request()
        if "is available</h4>" in r:
            return f"O nickname {self.nickname} está disponível!"
        else:
            return f"O nickname {self.nickname} estará disponível em " + str(self.get_time_left()) + "dias!"  

    def get_time_left(self):
        r = self.send_request()
        result = re.search("is available in ([^.]*)days", r)
        days_left = result.group(1)
        return days_left

if __name__ == "__main__":
    nickname = input("Digite o nickname: ")
    region = input("Digite a região: ")
    checker = Checker(nickname, region)
    print(checker.check_nickname_availability())
    input("Pressione qualquer tecla para sair...")
    
