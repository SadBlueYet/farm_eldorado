import httpx
import string
from random import choice


class CreateMailData:

    def create_email(self):
        """

        Метод для создания рандомной почты

        """
        characters = string.ascii_letters.lower() + string.digits
        email_name = ''.join(choice(characters) for _ in range(15))
        return f'{email_name}@desertsundesigns.com'

    def create_password(self):
        """

        Метод для создания рандомного пароля

        """
        characters = string.ascii_letters + string.digits
        password = ''.join(choice(characters) for _ in range(20))
        return password


class MailRegistration:
    headers: dict
    url: str
    data: CreateMailData
    __address: str
    __password: str

    def __init__(self):
        self.data = CreateMailData()
        self.url = 'https://api.mail.tm/accounts'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.142.86 Safari/537.36'}

    def get_mail(self) -> int:
        """

        Метод для создания почты на mail.tm

        """
        self.__address = self.data.create_email()
        self.__password = self.data.create_password()
        data = {
            'address': self.__address,
            'password': self.__password
        }
        try:
            response = httpx.post(self.url, json=data)
            return response.status_code
        except Exception as e:
            return 500

    @property
    def get_address(self):
        return self.__address

    @property
    def get_password(self):
        return self.__password




