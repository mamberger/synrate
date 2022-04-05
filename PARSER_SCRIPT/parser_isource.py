import time
from datetime import datetime

import requests

from connector import change_parser_status
from ENGINE import Parser


class ParserSource(Parser):
    def __init__(self, end):
        super().__init__()
        self.api_get_info_url = "https://reserve.isource.ru/api/auction/get-info"
        self.api_get_categories_url = "https://reserve.isource.ru/api/category/list/full"
        self.api_get_auction_url = "https://reserve.isource.ru/api/auction/list"
        self.response_item = None
        self.response_items = None
        self.response_categories = None
        self.count = 0
        self.last_page = end

    def get_last_page(self):
        response = requests.post(self.api_get_auction_url, headers={
            'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},
                                            data={
                                                # "category_name": category["transliteration_name"],
                                                "page": 1,
                                                "per_page": 100}).json()
        last_page = response['pagination']['page_count']
        return int(last_page)

    def parse(self):
        last_page = self.get_last_page()
        if self.last_page:
            last_page = int(self.last_page)
        for i in range(1, last_page+1):
            i += 1
            time.sleep(15)
            print('next PAGE')
            counter = 0
            self.response_items = requests.post(self.api_get_auction_url, headers={'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},
                                                data={
                                                    #"category_name": category["transliteration_name"],
                                                    "page": i,
                                                    "per_page": 100,

                                                }).json()
            for z in self.response_items["data"]:
                print('next item')
                self.response_item = requests.post(self.api_get_info_url, headers={'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},
                                                   data={"auction_transliteration_name": z["auction_transliteration_name"]}).json()["data"]

                offer = {"name": self.response_item["name"],
                                        "location": self.response_item["region"][0]["name"],
                                        "home_name": "isource",
                                        "offer_type": "Продажа",
                                        "offer_start_date": self.response_item["date_begin"].split(" ")[0],
                                        "offer_end_date": self.response_item["date_end"].split(" ")[0],
                                        "owner": self.response_item["author_full_name"],
                                        "ownercontact": self.response_item["author_phone"],
                                        "offer_price": round(float(self.response_item["current_fix_price_without_nds"]))
                                      , "additional_data": "не указано",
                                        "organisation": self.response_item["contragent_host_name"],
                                        "url": "https://reserve.isource.ru/trades/item/"
                                               + self.response_item["auction_transliteration_name"]
                                        }

                z = requests.post("https://synrate.ru/api/offers/create",
                                  json=offer)
                today = datetime.today().strftime('%d-%m %H:%M')
                try:
                    print(f'[isource] {z.json()}\n{offer}')
                    # with open('/var/www/synrate_dir/isource.txt', 'r+') as f:
                    #     # ...
                    #     f.seek(0, 2)
                    #     f.write(f'[{today}] {z.json()}\n{offer}')
                    #     f.close()
                except:
                    print(f'[isource] {z}\n{offer}')
                    # with open('/var/www/synrate_dir/isource.txt', 'r+') as f:
                    #     # ...
                    #     f.seek(0, 2)
                    #     f.write(f'[{today}] {z}\n{offer}')
                    #     f.close()
        change_parser_status('isource', 'Выкл')
                # try:
                #     if z.json()["name"][0].find("already exists") != -1:
                #         counter += 1
                #
                #         if counter == 150:
                #             break
                # except:
                #     counter = 0
                #     z = None


if __name__ == '__main__':
    parser = ParserSource()
    parser.parse()