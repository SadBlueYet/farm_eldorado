import httpx
from pprint import pprint
from random import choice
from playwright.sync_api import sync_playwright
import fake_useragent as ua
from mail import WaitMessage
import time
from mailtm_reg import MailRegistration
class VacSms:
    api_key = ""
    proxies = {}
    def __init__(self) -> None:
        self.api_key = '77920d37b40d4b208c4f666c1d10faa9'
        self.proxies = get_proxy_httpx()
    
    def get_balance(self):
        response = httpx.get(f'https://vak-sms.com/api/getBalance/?apiKey={self.api_key}', proxies=self.proxies)
        print(response.json())

    def get_telephone_number(self):
        """

        Метод для получения номера телефона с vak-sms

        """
        try:
            response = httpx.get(f"""https://vak-sms.ru/api/getNumber/?apiKey={self.api_key}&service=mv""").json()
            self.id = response.get("idNum")
            return response.get("tel")
        except Exception as e:
            print(e)
            return {"tel": None}
        
    def get_message(self):
        """

        Метод для получения секретного кода

        """
        try:
            response = httpx.get(
                f"https://vak-sms.ru/api/getSmsCode/?apiKey={self.api_key}&idNum={self.id}&all").json()
            return response.get("smsCode")[-1]
        except Exception as e:
            return None

    def set_state(self):
        try:
            response = httpx.get(f"https://vak-sms.ru/api/setStatus/?apiKey={self.api_key}&status=send&idNum={self.id}")
            print(response.get("status"))
        except Exception as e:
            print(e)

class Registry:
    tel: str
    proxies: dict
    cookies: str
    headers: dict
    page: object
    def __init__(self, tel: str, page) -> None:
        self.tel = tel
        self.proxies = get_proxy_httpx()
        self.page = page
        

    def wrigt_number(self):
        try:
            self.page.goto("https://www.eldorado.ru/")
            time.sleep(10)
            self.page.get_by_role("banner").get_by_role("button", name="Вход или регистрация").click()
            self.page.locator("#modalPortal").get_by_role("textbox").click()
            self.page.locator("#modalPortal").get_by_role("textbox").fill(str(self.tel)[1:])
            self.page.get_by_role("button", name="Получить код").click()
            self.page.wait_for_timeout(1000)
            self.page.get_by_role("button", name="Получить код").click()
        except Exception as e:
            print(e)

    
    def wright_code(self, code: str):
        try:
            inputs = self.page.query_selector_all('input.id')
            for i in range(len(inputs)):
                inputs[i].fill(str(code[i]))
            self.page.keyboard.press('Enter')
            input()
        except Exception as e:
            print(e)
    
    def write_all_data(self, mail: str):
        name = "Максим"
        last_name = "Максимов"
        birthday = "01012000"
        time.sleep(10)
        try:
            self.page.query_selector('input[name="email"]')
            self.page.keyboard.insert_text(mail)
            self.page.query_selector('input[name="name"]').fill(name)
            self.page.query_selector('input[name="lastName"]').fill(last_name)
            self.page.query_selector('input[inputmode="numeric"]').fill(birthday)
            #self.page.query_selector('input[name="email"]').fill(mail)
            time.sleep(2)
            self.page.query_selector('button.rc').click()
            self.page.wait_for_timeout(10000)
        except Exception as e:
            print(e)
    def get_confirm_message(self):
        self.page.goto("https://www.eldorado.ru/personal/club/user_profile/")
        time.sleep(5)
        self.page.query_selector('div.verify-btn.js-send-confirm-message').click()


    def confirm_email(self, link: str):
        try:
            self.page.goto(link)
            time.sleep(10)
        except Exception as e:
            print(e)
    
    def save_password(self, password: str):
        try:
            self.page.goto("https://www.eldorado.ru/personal/club/user_profile/")
            self.page.query_selector('input[name="CLUB_USER_FORM_NAMEMIDDLE"]').fill("Русланович")
            self.page.query_selector('input[name="CLUB_USER_FORM_NEW_PASSWORD"]').click()
            self.page.keyboard.insert_text(password)
            self.page.query_selector('input[name="CLUB_USER_FORM_NEW_PASSWORD_CONFIRM"]').click()
            self.page.keyboard.insert_text(password)
            self.page.query_selector('input.profile__save_button').click()
            time.sleep(1000)
        except Exception as e:
            print(e)


def intercept_requests(route, request):
    print(f"Intercepted request: {request.url} - {request}")
"""
    page.goto("https://eldorado.ru/")
    page.goto("https://www.eldorado.ru/")
    page.get_by_role("banner").get_by_role("button", name="Вход или регистрация").click()
    page.locator("#modalPortal").get_by_role("textbox").click()
    page.locator("#modalPortal").get_by_role("textbox").fill("+7 999 999 9999_")
    page.get_by_role("button", name="Получить код").click()
    page.locator("#modalPortal").get_by_role("textbox").first.click()
    page.locator("#modalPortal").get_by_role("textbox").first.fill("5")
    page.locator("#modalPortal").get_by_role("textbox").nth(1).fill("4")
    page.locator("#modalPortal").get_by_role("textbox").nth(2).fill("3")
    page.locator("#modalPortal").get_by_role("textbox").nth(3).fill("2")

"""

def main():
    mail = MailRegistration()
    status_code = mail.get_mail()
    email = ""
    if 200 <= status_code <= 204:
        email = mail.get_address
        password = mail.get_password
        print(email, password)

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(user_agent=ua.UserAgent().random, proxy=get_proxy_wright())
        page = context.new_page()
        #page.route("**/*", intercept_requests)
        vac = VacSms()
        vac.get_balance()
        tel = vac.get_telephone_number()

        reg = Registry(tel, page)
        reg.wrigt_number()

        while True:
            code = vac.get_message()
            time.sleep(7)
            print(code)
            if code:
                break   

        reg.wright_code(code)
        reg.write_all_data(email)
        reg.get_confirm_message()
        time.sleep(5)

        message = WaitMessage(email, password)
        message.get_message_id()
        confirm_link = message.get_html_message()
        if not confirm_link:
            print("Ссылка не получена")

        reg.confirm_email(confirm_link)
        reg.save_password(password)
        with open('accounts.txt', 'a') as f:
            f.write(f"{email}:{password}\n")


        

def get_proxy_wright():
    """

    Метод для получения прокси из файла

    """
    proxie = []
    with open('proxy.txt', 'r') as f:
        while True:
            proxy = f.readline().strip()
            if not proxy:
                break
            proxie.append(proxy)

    proxy = choice(proxie)

    proxy_url = f'http://{proxy.split(":")[0]}'
    proxy_url += f':{proxy.split(":")[1]}'
    proxy_log = proxy.split(':')[2]
    proxy_pass = proxy.split(':')[3]
    proxy = {
        "server": proxy_url,
        "username": proxy_log,
        "password": proxy_pass
    }
    return proxy



def get_proxy_httpx():
    """

    Метод для получения прокси из файла

    """
    proxie = []
    with open('proxy.txt', 'r') as f:
        while True:
            proxy = f.readline().strip()
            if not proxy:
                break
            proxie.append(proxy)

    proxy = choice(proxie)

    proxy_url = f'http://{proxy.split(":")[0]}'
    proxy_url += f':{proxy.split(":")[1]}'
    proxy_auth = (proxy.split(':')[2], proxy.split(':')[3])

    proxy = httpx.Proxy(url=proxy_url, auth=proxy_auth)
    proxies = {
        'http://': proxy,
        'https://': proxy
    }
    return proxies

if __name__ == "__main__":
    main()
    """
    vac = VacSms()
    print(vac.get_telephone_number())
    time.sleep(10)
    while True:
        code = vac.get_message()
        time.sleep(3)
        if code:
            break
    print(code)

    """