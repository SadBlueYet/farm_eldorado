import httpx
from pprint import pprint
import time


class WaitMessage:
    token: str
    login: str
    password: str
    id: str
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        try:
            response = httpx.post("https://api.mail.tm/token",
                                  json={"address": self.login, "password": self.password})
            self.token = response.json().get("token")
        except Exception as e:
            print(e)
    
    def get_message_id(self):
        while True:
            try:
                response = httpx.get("https://api.mail.tm/messages",
                                headers={"Authorization": f"Bearer {self.token}"}).json()
                message = next(
                            item for item in response.get('hydra:member') if item.get('subject') == 'Подтвердите свою электронную почту ✅')
                self.id = message.get('@id')
                time.sleep(3)
                return
            except Exception as e:
                time.sleep(3)
                self.message = None
                print(e)
    
    def get_html_message(self):
        try:
            response = httpx.get(f"https://api.mail.tm{self.id}",
                        headers={"Authorization": f"Bearer {self.token}"}).json()
            text = response.get('text')
            for line in text.split('\n'):
                if 'confirm_email.php' in line:
                    print(line)
                    return line[1:-1]
        except Exception as e:
            print(e)


