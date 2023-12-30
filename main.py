import httpx
from pprint import pprint
from random import choice
from playwright.sync_api import sync_playwright
import fake_useragent as ua
from seleniumwire import undetected_chromedriver as uc
from undetected_chromedriver import By
import time
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
    def __init__(self, tel: str) -> None:
        self.tel = tel
        self.proxies = get_proxy_httpx()

    def wrigt_number(self):
        user_agent = ua.UserAgent().random
        cookies = {
            '__cap_p_': '1,0',
            '__cap_': '1b1037cac0a37e96b52cc7cad0d7468a',
            '__hash_': '2a928a5634f15f23d761a244093d5c8c',
            '__lhash_': '13ace2441562b2e9516d0b7f55b9d645',
            'ab_user': '59523520100',
            'ab_segment': '59',
            'iRegionSectionId': '11290',
            'GUID': 'yyomzbw2tcsxtmmkvkvmexayyv73emeuac44',
            'dt': '1',
            'grs': '15628',
            'AUTORIZZ': '0',
            'AC': '1',
            'lv_user_org': '0',
            'el_group_user_org': '0',
            'bonus_cobrand_showed': '0',
            'PHPSESSID': '3o945g7fkj4jpl5v2ltdgcufhk',
            'ABT_test': 'B',
            'BITRIX_SM_SALE_UID': '32247514673',
            'BITRIX_SM_SALE_UID_CS': 'b286003ed1612e82a2552ab6b32f25cc',
            '_slid': '658d583fb2fb3b86e401e510',
            '_sljsession': 'B21BA808-D411-44C4-ABAC-5E8108267984',
            '_userGUID': '0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh',
            '_slid': '658d583fb2fb3b86e401e510',
            '_slsession': 'F968DD65-A67C-4C29-ACE9-B7FD520CCC0C',
            '_slfreq': '646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185',
            'gsscgib-w-eldorado': '0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==',
            'cfidsgib-w-eldorado': 'u9dgdI3nR9P710aAU2XWnNbnD8s/mYtwZrxRckWNx9PhNaEsktiNqjyjW/MuJYCLSu8Kpnld2/8ne40jh5Wv30ZpirA5fxMql3qpqChM/G4EgqEHsNzkL+B+omCFcp0/iNogCpZIORhIXayZKEkT4uWud1Ql36/PtscR',
            'dSesn': 'ed5a3516-ca5b-0eec-7581-9bfd397426bc',
            '_dvs': '0:lqp3w9ea:zfeGx7_C77zyiMsWr7rCikxHP6DabjNC',
            '_gcl_au': '1.1.1868773873.1703761986',
            'utm_campaign': 'yandex',
            'gsscgib-w-eldorado': '0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==',
            'gsscgib-w-eldorado': '0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==',
            'advcake_session_id': '5cdbc545-296f-b70c-03e8-cd33ba2c11dd',
            'advcake_track_url': 'https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex',
            'advcake_utm_partner': 'yandex',
            'advcake_utm_webmaster': '',
            'advcake_click_id': '',
            '_sp_ses.f3a5': '*',
            '_gid': 'GA1.2.317307565.1703761987',
            'tmr_lvid': '09d7e6028a2efd1279043978fd086e3b',
            'tmr_lvidTS': '1703761986952',
            'flocktory-uuid': '4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0',
            'uxs_uid': '146c4a00-a572-11ee-8376-83af42e8e52d',
            'advcake_trackid': 'f356efbb-9e47-cb7b-d699-8ace99003133',
            'advcake_hold': '7d146507-75e2-ab87-401e-812d80384b4d',
            'gdeslon.ru.__arc_domain': 'gdeslon.ru',
            'gdeslon.ru.user_id': 'e664f4d1-128a-46e8-86b6-2745f7464431',
            '_ym_uid': '1703761989738062326',
            '_ym_d': '1703761989',
            '_ga_4P3TZK55KZ': 'GS1.1.1703761988.1.0.1703761988.0.0.0',
            '_ga': 'GA1.1.1326932195.1703761987',
            'adid': '170376198893082',
            '_ym_isad': '2',
            '_gp100025D5': '{"utm":"1386938c","hits":1,"vc":1}',
            '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
            '_ym_visorc': 'w',
            'adrdel': '1',
            'adrcid': 'AMFrEf3V7Mgfrr4PQ72EH4g',
            '_gat': '1',
            '_ga_Y956M1PRK1': 'GS1.2.1703761991.1.0.1703761991.60.0.0',
            'tmr_detect': '0%7C1703761992601',
            '_sp_id.f3a5': '34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703762002..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.8',
            'fgsscgib-w-eldorado': 'IO5I5da2f8719e008b477826980ea074e68d1a5a',
            'fgsscgib-w-eldorado': 'IO5I5da2f8719e008b477826980ea074e68d1a5a',
        }

        headers = {
            'authority': 'www.eldorado.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlNJRCI6IjNvOTQ1Zzdma2o0anBsNXYybHRkZ2N1ZmhrIn0sImV4cCI6MTcwMzc2Mzc4Mn0.HAJtvolLLuOgzLBsOJXi1Thc0FoFioCYOwfV9ossM_priqVTzce4tRMDwpyWE4Yj-Th9jK8pPaENiR_70JNAkA',
            'content-type': 'application/json',
            # 'cookie': '__cap_p_=1,0; __cap_=1b1037cac0a37e96b52cc7cad0d7468a; __hash_=2a928a5634f15f23d761a244093d5c8c; __lhash_=13ace2441562b2e9516d0b7f55b9d645; ab_user=59523520100; ab_segment=59; iRegionSectionId=11290; GUID=yyomzbw2tcsxtmmkvkvmexayyv73emeuac44; dt=1; grs=15628; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; PHPSESSID=3o945g7fkj4jpl5v2ltdgcufhk; ABT_test=B; BITRIX_SM_SALE_UID=32247514673; BITRIX_SM_SALE_UID_CS=b286003ed1612e82a2552ab6b32f25cc; _slid=658d583fb2fb3b86e401e510; _sljsession=B21BA808-D411-44C4-ABAC-5E8108267984; _userGUID=0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh; _slid=658d583fb2fb3b86e401e510; _slsession=F968DD65-A67C-4C29-ACE9-B7FD520CCC0C; _slfreq=646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185; gsscgib-w-eldorado=0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==; cfidsgib-w-eldorado=u9dgdI3nR9P710aAU2XWnNbnD8s/mYtwZrxRckWNx9PhNaEsktiNqjyjW/MuJYCLSu8Kpnld2/8ne40jh5Wv30ZpirA5fxMql3qpqChM/G4EgqEHsNzkL+B+omCFcp0/iNogCpZIORhIXayZKEkT4uWud1Ql36/PtscR; dSesn=ed5a3516-ca5b-0eec-7581-9bfd397426bc; _dvs=0:lqp3w9ea:zfeGx7_C77zyiMsWr7rCikxHP6DabjNC; _gcl_au=1.1.1868773873.1703761986; utm_campaign=yandex; gsscgib-w-eldorado=0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==; gsscgib-w-eldorado=0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==; advcake_session_id=5cdbc545-296f-b70c-03e8-cd33ba2c11dd; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; _sp_ses.f3a5=*; _gid=GA1.2.317307565.1703761987; tmr_lvid=09d7e6028a2efd1279043978fd086e3b; tmr_lvidTS=1703761986952; flocktory-uuid=4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0; uxs_uid=146c4a00-a572-11ee-8376-83af42e8e52d; advcake_trackid=f356efbb-9e47-cb7b-d699-8ace99003133; advcake_hold=7d146507-75e2-ab87-401e-812d80384b4d; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e664f4d1-128a-46e8-86b6-2745f7464431; _ym_uid=1703761989738062326; _ym_d=1703761989; _ga_4P3TZK55KZ=GS1.1.1703761988.1.0.1703761988.0.0.0; _ga=GA1.1.1326932195.1703761987; adid=170376198893082; _ym_isad=2; _gp100025D5={"utm":"1386938c","hits":1,"vc":1}; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; _ym_visorc=w; adrdel=1; adrcid=AMFrEf3V7Mgfrr4PQ72EH4g; _gat=1; _ga_Y956M1PRK1=GS1.2.1703761991.1.0.1703761991.60.0.0; tmr_detect=0%7C1703761992601; _sp_id.f3a5=34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703762002..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.8; fgsscgib-w-eldorado=IO5I5da2f8719e008b477826980ea074e68d1a5a; fgsscgib-w-eldorado=IO5I5da2f8719e008b477826980ea074e68d1a5a',
            'origin': 'https://www.eldorado.ru',
            'referer': 'https://www.eldorado.ru/?utm_source=yandex&utm_medium=organic&utm_campaign=yandex&utm_referrer=yandex',
            'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23.11", "Not=A?Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-gib-fgsscgib-w-eldorado': 'IO5I5da2f8719e008b477826980ea074e68d1a5a',
            'x-gib-gsscgib-w-eldorado': '0aQlrUzoaNNJqy3eCcxAs6oENO7sWPIIpWU4c1VCi3bLexureFq6vNiBMQ3gXbnuZ9IS3+kUhWnxvUC/02Qo8dYZ6x2TmLayJbxcs2WKWrc3sG+EWRyVai90r2JKreZLQSfX+WlZbGK2b0JBm3Px0vk7eg5rUZ1H11K4qAJItUwUUpq9ih9thIvstSGE5eb+vFJsJo0inYF8cPaXqTEmT5JczBJmcTvHXIf98GTytR9Y+pn7M7H/4SGLW4jI8Q==',
            'x-source-frontend': 'SPA',
        }

        json_data = {
            'user_login': f'+{self.tel}',
            'reregistration': '0',
            'organization': '0',
        }

        response = httpx.post(
            'https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php',
            cookies=cookies,
            headers=headers,
            json=json_data,
            proxies=self.proxies
        )
        pprint(response)
        pprint(response.json())
    
    def wright_code(self, code: str):
        user_agent = ua.UserAgent().random
        cookies = {
            '__hash_': '2a928a5634f15f23d761a244093d5c8c',
            '__lhash_': '13ace2441562b2e9516d0b7f55b9d645',
            'ab_user': '59523520100',
            'ab_segment': '59',
            'iRegionSectionId': '11290',
            'GUID': 'yyomzbw2tcsxtmmkvkvmexayyv73emeuac44',
            'dt': '1',
            'grs': '15628',
            'AUTORIZZ': '0',
            'AC': '1',
            'lv_user_org': '0',
            'el_group_user_org': '0',
            'bonus_cobrand_showed': '0',
            'PHPSESSID': '3o945g7fkj4jpl5v2ltdgcufhk',
            'ABT_test': 'B',
            'BITRIX_SM_SALE_UID': '32247514673',
            'BITRIX_SM_SALE_UID_CS': 'b286003ed1612e82a2552ab6b32f25cc',
            '_slid': '658d583fb2fb3b86e401e510',
            '_sljsession': 'B21BA808-D411-44C4-ABAC-5E8108267984',
            '_userGUID': '0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh',
            '_slid': '658d583fb2fb3b86e401e510',
            '_slsession': 'F968DD65-A67C-4C29-ACE9-B7FD520CCC0C',
            '_slfreq': '646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185',
            'dSesn': 'ed5a3516-ca5b-0eec-7581-9bfd397426bc',
            '_dvs': '0:lqp3w9ea:zfeGx7_C77zyiMsWr7rCikxHP6DabjNC',
            '_gcl_au': '1.1.1868773873.1703761986',
            'utm_campaign': 'yandex',
            'advcake_session_id': '5cdbc545-296f-b70c-03e8-cd33ba2c11dd',
            'advcake_track_url': 'https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex',
            'advcake_utm_partner': 'yandex',
            'advcake_utm_webmaster': '',
            'advcake_click_id': '',
            '_sp_ses.f3a5': '*',
            '_gid': 'GA1.2.317307565.1703761987',
            'tmr_lvid': '09d7e6028a2efd1279043978fd086e3b',
            'tmr_lvidTS': '1703761986952',
            'flocktory-uuid': '4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0',
            'uxs_uid': '146c4a00-a572-11ee-8376-83af42e8e52d',
            'advcake_trackid': 'f356efbb-9e47-cb7b-d699-8ace99003133',
            'advcake_hold': '7d146507-75e2-ab87-401e-812d80384b4d',
            'gdeslon.ru.__arc_domain': 'gdeslon.ru',
            'gdeslon.ru.user_id': 'e664f4d1-128a-46e8-86b6-2745f7464431',
            '_ym_uid': '1703761989738062326',
            '_ym_d': '1703761989',
            '_ga_4P3TZK55KZ': 'GS1.1.1703761988.1.0.1703761988.0.0.0',
            '_ga': 'GA1.1.1326932195.1703761987',
            'adid': '170376198893082',
            '_ym_isad': '2',
            '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
            '_ym_visorc': 'w',
            'adrdel': '1',
            'adrcid': 'AMFrEf3V7Mgfrr4PQ72EH4g',
            '_ga_Y956M1PRK1': 'GS1.2.1703761991.1.0.1703761991.60.0.0',
            'tmr_detect': '0%7C1703761992601',
            '_gp100025D5': '{"utm":"1386938c","hits":1,"vc":1,"ac":1}',
            '_sp_id.f3a5': '34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703762638..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.14',
            'gsscgib-w-eldorado': 'mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==',
            'cfidsgib-w-eldorado': 'hCVZulpGC+ifefXjyETuGTILLam64y4h4xHe2usFKIPtm8BaO00Tk9jqZczspXS/oCJfSIfwnvEFRc0bqXNNHwukOKZF1nQ1BZNmPv0/vP4rHTre6jGvrilz1IeM2Sx0YXZt9ub78m5IfoFj9Mf3B0wbvuFMcZeNJVwpLg==',
            'gsscgib-w-eldorado': 'mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==',
            'gsscgib-w-eldorado': 'mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==',
            'fgsscgib-w-eldorado': 't7kM5772ca42187e97c03c6ba3a899b31faad5f9',
            'fgsscgib-w-eldorado': 't7kM5772ca42187e97c03c6ba3a899b31faad5f9',
        }

        headers = {
            'authority': 'www.eldorado.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlNJRCI6IjNvOTQ1Zzdma2o0anBsNXYybHRkZ2N1ZmhrIn0sImV4cCI6MTcwMzc2Mzc4Mn0.HAJtvolLLuOgzLBsOJXi1Thc0FoFioCYOwfV9ossM_priqVTzce4tRMDwpyWE4Yj-Th9jK8pPaENiR_70JNAkA',
            'content-type': 'application/json',
            # 'cookie': '__hash_=2a928a5634f15f23d761a244093d5c8c; __lhash_=13ace2441562b2e9516d0b7f55b9d645; ab_user=59523520100; ab_segment=59; iRegionSectionId=11290; GUID=yyomzbw2tcsxtmmkvkvmexayyv73emeuac44; dt=1; grs=15628; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; PHPSESSID=3o945g7fkj4jpl5v2ltdgcufhk; ABT_test=B; BITRIX_SM_SALE_UID=32247514673; BITRIX_SM_SALE_UID_CS=b286003ed1612e82a2552ab6b32f25cc; _slid=658d583fb2fb3b86e401e510; _sljsession=B21BA808-D411-44C4-ABAC-5E8108267984; _userGUID=0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh; _slid=658d583fb2fb3b86e401e510; _slsession=F968DD65-A67C-4C29-ACE9-B7FD520CCC0C; _slfreq=646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185; dSesn=ed5a3516-ca5b-0eec-7581-9bfd397426bc; _dvs=0:lqp3w9ea:zfeGx7_C77zyiMsWr7rCikxHP6DabjNC; _gcl_au=1.1.1868773873.1703761986; utm_campaign=yandex; advcake_session_id=5cdbc545-296f-b70c-03e8-cd33ba2c11dd; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; _sp_ses.f3a5=*; _gid=GA1.2.317307565.1703761987; tmr_lvid=09d7e6028a2efd1279043978fd086e3b; tmr_lvidTS=1703761986952; flocktory-uuid=4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0; uxs_uid=146c4a00-a572-11ee-8376-83af42e8e52d; advcake_trackid=f356efbb-9e47-cb7b-d699-8ace99003133; advcake_hold=7d146507-75e2-ab87-401e-812d80384b4d; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e664f4d1-128a-46e8-86b6-2745f7464431; _ym_uid=1703761989738062326; _ym_d=1703761989; _ga_4P3TZK55KZ=GS1.1.1703761988.1.0.1703761988.0.0.0; _ga=GA1.1.1326932195.1703761987; adid=170376198893082; _ym_isad=2; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; _ym_visorc=w; adrdel=1; adrcid=AMFrEf3V7Mgfrr4PQ72EH4g; _ga_Y956M1PRK1=GS1.2.1703761991.1.0.1703761991.60.0.0; tmr_detect=0%7C1703761992601; _gp100025D5={"utm":"1386938c","hits":1,"vc":1,"ac":1}; _sp_id.f3a5=34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703762638..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.14; gsscgib-w-eldorado=mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==; cfidsgib-w-eldorado=hCVZulpGC+ifefXjyETuGTILLam64y4h4xHe2usFKIPtm8BaO00Tk9jqZczspXS/oCJfSIfwnvEFRc0bqXNNHwukOKZF1nQ1BZNmPv0/vP4rHTre6jGvrilz1IeM2Sx0YXZt9ub78m5IfoFj9Mf3B0wbvuFMcZeNJVwpLg==; gsscgib-w-eldorado=mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==; gsscgib-w-eldorado=mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==; fgsscgib-w-eldorado=t7kM5772ca42187e97c03c6ba3a899b31faad5f9; fgsscgib-w-eldorado=t7kM5772ca42187e97c03c6ba3a899b31faad5f9',
            'origin': 'https://www.eldorado.ru',
            'referer': 'https://www.eldorado.ru/?utm_source=yandex&utm_medium=organic&utm_campaign=yandex&utm_referrer=yandex',
            'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23.11", "Not=A?Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-gib-fgsscgib-w-eldorado': 't7kM5772ca42187e97c03c6ba3a899b31faad5f9',
            'x-gib-gsscgib-w-eldorado': 'mD0QeAzQxjLdHNOt+SJZfw3P94Fut5evmqqSO3U/D1I9YvGagcwF1ORLjKLKos5CFqJ9JLcDJHvChW597I4GB9Z6MAYKyv+8NyK/rsRe+XREYRBIyeBL36UL1z6PBhehcwunAhP1bQ1fVSWvbVPZ8DFhnDrt3JYUkIs0gdsPMYR53b/X3wkLkfyp4qggWpYAVJxDsR0IlmEJr/U+qSo0Z+jS4LZSUE03gqyAGP7eQbbYfswwdIJeNHGt4/wAOQ==',
            'x-source-frontend': 'SPA',
        }

        json_data = {
            'code': code,
            'phone': f'+{self.tel}',
            'organization': '0',
            'reregistration': '0',
            'g-recaptcha-response': '03AFcWeA4EtBSICCJE9rjJ6_SCgYXj8MPH6I4uD7LJzm9XGOCz8l888sk82qkUUBtJ_LRcAQEOrWgldoCBQWCGRkSMk4sGQVzfrTIf0u5ZN9OAJjgfwd5FBmOrIJNT-8GZG3ionCEJKOc8JJQMZBwlzf0rw1cziLcfR1Rh_fi_kNSXqJY_4BcNFUOjtFh5jnUdGp9zpoc7AhqazXYJgQVH8-DKLXg_74CVnC8ITUaWw0s8XYQKSDAHVN8k9rtzb3ztXLqNWFWBD-ZGA_GtW9HzGHZjKXB-SnBSLtZOLoKs6L3rvnlJB6f4nnqoVcwibRdnyTCRDsiJ2DZhbFARw9BqaVjvndr9aTvydWLhskxGesy1Kh0cKwkY6aVjtAfNs84rOSoCrxUjAPP1fnOUl1Xi6XreOMDgRofKPFNIBNsm3vCHoCmLbGmRQNuYQAQ8ok8syP4ZyD2hT5WxTqeJWUr-H9i12QGZ0RZ3noEhFDMjrZn7LtuZHcn89BzBSSihXjXJLPtgIZy78JBr9dPR81PvXeWlMqUlKO0mOVqqgC8zhp9dG0xpthlkcGDpM0nyrmw0wvFsves2RIATZ63Vz5Sk0-ad4zgO-qo1ow',
        }

        response = httpx.post(
            'https://www.eldorado.ru/_ajax/spa/auth/v2/check_sms_code.php',
            cookies=cookies,
            headers=headers,
            json=json_data,
            proxies=self.proxies,
        )
        pprint(response)
        pprint(response.json())
    
    def write_all_data(self):
        user_agent = ua.UserAgent().random
        cookies = {
            '__hash_': '2a928a5634f15f23d761a244093d5c8c',
            '__lhash_': '13ace2441562b2e9516d0b7f55b9d645',
            'ab_user': '59523520100',
            'ab_segment': '59',
            'GUID': 'yyomzbw2tcsxtmmkvkvmexayyv73emeuac44',
            'dt': '1',
            'grs': '15628',
            'AC': '1',
            'lv_user_org': '0',
            'el_group_user_org': '0',
            'bonus_cobrand_showed': '0',
            'ABT_test': 'B',
            '_slid': '658d583fb2fb3b86e401e510',
            '_sljsession': 'B21BA808-D411-44C4-ABAC-5E8108267984',
            '_userGUID': '0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh',
            '_slid': '658d583fb2fb3b86e401e510',
            '_slsession': 'F968DD65-A67C-4C29-ACE9-B7FD520CCC0C',
            '_slfreq': '646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185',
            '_gcl_au': '1.1.1868773873.1703761986',
            'utm_campaign': 'yandex',
            'advcake_session_id': '5cdbc545-296f-b70c-03e8-cd33ba2c11dd',
            'advcake_track_url': 'https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex',
            'advcake_utm_partner': 'yandex',
            'advcake_utm_webmaster': '',
            'advcake_click_id': '',
            '_sp_ses.f3a5': '*',
            '_gid': 'GA1.2.317307565.1703761987',
            'tmr_lvid': '09d7e6028a2efd1279043978fd086e3b',
            'tmr_lvidTS': '1703761986952',
            'flocktory-uuid': '4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0',
            'uxs_uid': '146c4a00-a572-11ee-8376-83af42e8e52d',
            'advcake_trackid': 'f356efbb-9e47-cb7b-d699-8ace99003133',
            'gdeslon.ru.__arc_domain': 'gdeslon.ru',
            'gdeslon.ru.user_id': 'e664f4d1-128a-46e8-86b6-2745f7464431',
            '_ym_uid': '1703761989738062326',
            '_ym_d': '1703761989',
            '_ga': 'GA1.1.1326932195.1703761987',
            'adid': '170376198893082',
            '_ym_isad': '2',
            '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
            'adrdel': '1',
            'adrcid': 'AMFrEf3V7Mgfrr4PQ72EH4g',
            '_ga_Y956M1PRK1': 'GS1.2.1703761991.1.0.1703761991.60.0.0',
            'BITRIX_SM_LOGIN': 'gjs8j4l4swmibag%40wireconnected.com',
            'ADV_GID': '91929468',
            'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
            'iRegionSectionId': '11290',
            '_slid_server': '658d583fb2fb3b86e401e510',
            'BITRIX_SM_ELD_TZ_OFFSET': '-420',
            'mindboxDeviceUUID': 'f18e989e-cb71-4685-9181-941ca6d9e7f6',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22f18e989e-cb71-4685-9181-941ca6d9e7f6%22%7D',
            'rrpvid': '279460685044768',
            'cookieUID': '0897172908',
            'cookieUserID': '91929468',
            'rcuid': '658d5f420c51b04ed17379a8',
            'AUTORIZZ': '0',
            'USER_AUTH_GTM': '0',
            'bCNT': '0%3A0',
            '_ym_visorc': 'w',
            'digi-SearchVisitor': '10%3A8',
            'PHPSESSID': '3o945g7fkj4jpl5v2ltdgcufhk',
            'BITRIX_SM_SALE_UID': '32247567627',
            'BITRIX_SM_SALE_UID_CS': '1546febc63b2efae62b58a6d0c21cc7a',
            '_ga_4P3TZK55KZ': 'GS1.1.1703761988.1.1.1703764124.0.0.0',
            'advcake_hold': '66541e6c-b907-7ea6-3dbe-94178dcdffa1',
            '_gp100025D5': '{"utm":"1386938c","hits":6,"vc":1,"ac":1,"a6":1}',
            'tmr_detect': '0%7C1703764128558',
            '_sp_id.f3a5': '34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703764176..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.37',
            'gsscgib-w-eldorado': 'FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau',
            'cfidsgib-w-eldorado': 'fLv3yRGMVHFfKXktf3nrFDur0chmUrbbWQVk04zM7OQzTN7sv10Ti1kOqZP+eTsKiOq4Uv1PBgyuILh6zvM8agdtc3N6MN+s5bGW0ZqiPtKgs+LnKCyBTLUpDWlD8xwVT1nkC2Jws5dMu5U2C0482XdtHN1L3CbQWX97Hw==',
            'gsscgib-w-eldorado': 'FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau',
            'gsscgib-w-eldorado': 'FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau',
            'fgsscgib-w-eldorado': 'pRA6f95063923ee704a86ddcac69222411358487',
            'fgsscgib-w-eldorado': 'pRA6f95063923ee704a86ddcac69222411358487',
        }

        headers = {
            'authority': 'www.eldorado.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlNJRCI6IjNvOTQ1Zzdma2o0anBsNXYybHRkZ2N1ZmhrIn0sImV4cCI6MTcwMzc2NTAxNX0.g7IuifSqSu2HPNA5IoopUnmpjvMLKqH2vrG0aqGaTIIASBxtFA0legrjo-VVu9m9X4feN6Y6wYoeu-vQcttitw',
            'content-type': 'application/json',
            # 'cookie': '__hash_=2a928a5634f15f23d761a244093d5c8c; __lhash_=13ace2441562b2e9516d0b7f55b9d645; ab_user=59523520100; ab_segment=59; GUID=yyomzbw2tcsxtmmkvkvmexayyv73emeuac44; dt=1; grs=15628; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; ABT_test=B; _slid=658d583fb2fb3b86e401e510; _sljsession=B21BA808-D411-44C4-ABAC-5E8108267984; _userGUID=0:lqp3w9ea:fsk1ZkXrgrItD~gQ8XPNgDC~PxCLe0yh; _slid=658d583fb2fb3b86e401e510; _slsession=F968DD65-A67C-4C29-ACE9-B7FD520CCC0C; _slfreq=646f4a3ad9b723086101fbec%3A646f4a3ad9b723086101fbf0%3A1703769185; _gcl_au=1.1.1868773873.1703761986; utm_campaign=yandex; advcake_session_id=5cdbc545-296f-b70c-03e8-cd33ba2c11dd; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; _sp_ses.f3a5=*; _gid=GA1.2.317307565.1703761987; tmr_lvid=09d7e6028a2efd1279043978fd086e3b; tmr_lvidTS=1703761986952; flocktory-uuid=4ff7ef51-7fef-414b-a923-7fbd7800dbfe-0; uxs_uid=146c4a00-a572-11ee-8376-83af42e8e52d; advcake_trackid=f356efbb-9e47-cb7b-d699-8ace99003133; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e664f4d1-128a-46e8-86b6-2745f7464431; _ym_uid=1703761989738062326; _ym_d=1703761989; _ga=GA1.1.1326932195.1703761987; adid=170376198893082; _ym_isad=2; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; adrdel=1; adrcid=AMFrEf3V7Mgfrr4PQ72EH4g; _ga_Y956M1PRK1=GS1.2.1703761991.1.0.1703761991.60.0.0; BITRIX_SM_LOGIN=gjs8j4l4swmibag%40wireconnected.com; ADV_GID=91929468; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; iRegionSectionId=11290; _slid_server=658d583fb2fb3b86e401e510; BITRIX_SM_ELD_TZ_OFFSET=-420; mindboxDeviceUUID=f18e989e-cb71-4685-9181-941ca6d9e7f6; directCrm-session=%7B%22deviceGuid%22%3A%22f18e989e-cb71-4685-9181-941ca6d9e7f6%22%7D; rrpvid=279460685044768; cookieUID=0897172908; cookieUserID=91929468; rcuid=658d5f420c51b04ed17379a8; AUTORIZZ=0; USER_AUTH_GTM=0; bCNT=0%3A0; _ym_visorc=w; digi-SearchVisitor=10%3A8; PHPSESSID=3o945g7fkj4jpl5v2ltdgcufhk; BITRIX_SM_SALE_UID=32247567627; BITRIX_SM_SALE_UID_CS=1546febc63b2efae62b58a6d0c21cc7a; _ga_4P3TZK55KZ=GS1.1.1703761988.1.1.1703764124.0.0.0; advcake_hold=66541e6c-b907-7ea6-3dbe-94178dcdffa1; _gp100025D5={"utm":"1386938c","hits":6,"vc":1,"ac":1,"a6":1}; tmr_detect=0%7C1703764128558; _sp_id.f3a5=34fc8a2e-1169-4cbb-b929-3320832e9ec5.1703761987.1.1703764176..6156185a-b943-47b7-ad18-8f8fa07f8821..ea363fa5-98f3-490f-9f93-30d129fcb50f.1703761987302.37; gsscgib-w-eldorado=FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau; cfidsgib-w-eldorado=fLv3yRGMVHFfKXktf3nrFDur0chmUrbbWQVk04zM7OQzTN7sv10Ti1kOqZP+eTsKiOq4Uv1PBgyuILh6zvM8agdtc3N6MN+s5bGW0ZqiPtKgs+LnKCyBTLUpDWlD8xwVT1nkC2Jws5dMu5U2C0482XdtHN1L3CbQWX97Hw==; gsscgib-w-eldorado=FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau; gsscgib-w-eldorado=FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau; fgsscgib-w-eldorado=pRA6f95063923ee704a86ddcac69222411358487; fgsscgib-w-eldorado=pRA6f95063923ee704a86ddcac69222411358487',
            'origin': 'https://www.eldorado.ru',
            'referer': 'https://www.eldorado.ru/auth/?withoutToken=1&withClose=1&backUrl=/personal/club/operations/',
            'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23.11", "Not=A?Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-gib-fgsscgib-w-eldorado': 'pRA6f95063923ee704a86ddcac69222411358487',
            'x-gib-gsscgib-w-eldorado': 'FQ2Xz6wL/bOhcOgDlPwxEpL3e0Ef5SlBxJgQhxoYq1KQB2SHF41MoviBiosh88jmd78JUiMZ7uz8q2dFf+xvtRYfzTHu/YXJ0jyGgz0d5JSUnzQ/YxJ+vt183c8N5da8wY7TDBzzdj6W/0An2mQMOjRUsoO/hdaHvZ3M2k+3ONtzHs5xxBBwluaPV6fYjEHApTcZA9Sih0K0la5b1Bj1ZADGaaCJs5CnYFbQ1GcjEDiFm/i90qP/atBVeXjipVo8r/pQfvy2jUau',
            'x-source-frontend': 'SPA',
        }

        json_data = {
            'organization': '0',
            'birthday': '11.10.2001',
            'cardNumber': '',
            'cardPin': '',
            'email': 'dargdsrgresggesgg@desertsundesigns.com',
            'hasBonusCard': '0',
            'lastName': 'Климин',
            'name': 'Максим',
            'password': '5003115148Aa',
            'phone': f'+{self.tel}',
            'passwordConfirm': '5003115148Aa',
            'mailingAgreement': '0',
        }

        response = httpx.post(
            'https://www.eldorado.ru/_ajax/spa/auth/v2/registration.php',
            cookies=cookies,
            headers=headers,
            json=json_data,
            proxies=self.proxies
        )
        pprint(response)
        self.cookies = str(response.cookies)
        pprint(cookies)
        self.head = str(response.headers)
        pprint(self.head)
        cookies = cookies.replace("<Cookies[", "").replace("]>", "")
        cookie_list = cookies.split(", ")
        values = [cookie[8:-23] for cookie in cookie_list]
        self.cookies = values

        self.headers = response.json()
        pprint(response.json())
    
    def confirm_email(self):
        pr = get_proxy_wright()
        user_agent = ua.UserAgent().random
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            context = browser.new_context(user_agent=user_agent)
            page = context.new_page()
            page.goto('https://www.eldorado.ru')
            page.wait_for_timeout(3000)
      
def main():
    vac = VacSms()
    vac.get_balance()
    tel = vac.get_telephone_number()
    reg = Registry(tel)
    reg.wrigt_number()
    while True:
        code = vac.get_message()
        time.sleep(3)
        if code:
            break 
    reg.wright_code(code)
    reg.write_all_data()
    reg.confirm_email()

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