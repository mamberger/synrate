from datetime import datetime, date
import random
import time

import requests
import vk

from connector import Item, DbManager


def get_api(token):
    session = vk.Session(access_token=token)
    api = vk.API(session, v='5.81', lang='ru', timeout=10)
    return api


class VkGroup:
    def __init__(self, url, id, name, api):
        self.id = id
        self.api = api
        self.home_name = 'vk.com'
        self.url = url
        self.name = name
        self.i_count = None
        self.last_i = 1
        self.db_manager = DbManager()
        self.thats_all = False

    def check_connect(self):
        wall = self.api.wall.get(owner_id=self.id, count=1)

    def wall_info(self):
        answer = {}
        successful = 0
        while not successful:
            try:
                wall = self.api.wall.get(owner_id=self.id, count=1)
                successful = 1
            except Exception as ex:
                print(ex)
        count = wall['count']
        i = int(count) / 90
        if i > int(i):
            i = int(i) + 1
        answer['i_count'] = i
        self.i_count = i
        return answer

    def wall_items(self, offset):
        successful = 0
        while not successful:
            try:
                wall = self.api.wall.get(owner_id=self.id, count=90, offset=offset)
                successful = 1
            except Exception as ex:
                print(ex)
                time.sleep(1)
        wall_items = wall['items']
        return wall_items

    def get_offers(self, data):
        answer = []
        ids = []
        for offer in data:
            if offer['text'] is None or offer['text'] == '':
                continue
            name, text = offer['text'], offer['text']
            name = name[:120]
            start_date = datetime.utcfromtimestamp(int(offer['date'])).strftime('%Y-%m-%d')
            ids.append(offer['from_id'])
            url = self.url+f'?w=wall{self.id}_{offer["id"]}%2Fall'
            offer_obj = {"name": name, "short_cat": self.name,
                         "home_name": f"{self.home_name}",
                         "offer_start_date": start_date, "additional_data": text,
                         "url": url, "from_id": offer['id'], "owner_id": offer['from_id']
                         }
            if start_date.split('-')[0] != str(date.today().year):
                self.thats_all = True

            offer = Item(name, self.home_name, url, None, start_date, None,
                None, None, None, text, None, offer['id'],
                self.name, offer['from_id'])
            answer.append(offer)
        return answer

    def send_result(self, data):
        for offer in data:
            offer.post(self.db_manager)
        self.db_manager.task_manager()