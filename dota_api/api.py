import logging
import time

import requests

from config import config
from crud_mongo.matches import mathes
from shems.Profile import PlayerData


class GetPlayerMatch:
    '''
        Класс для получения информации по игроку, принимает айдишник игрока
    '''

    def __init__(self, player_id):
        self.response = None
        self.player_id = player_id

    def get_information_about_player(self, url):
        '''
        Url принимает F строку в которой указывается урл откуда брать данные,
        айдишник пользователя чьи данные берем.
        :param url:
        :return:
        '''
        logging.info("Получение информации об игроке")
        self.response = requests.get(f'{config.DOTA_API}{url}')
        if self.response.status_code == 200:
            logging.info(f"Информация об от игроке {self.player_id} получена")
            self.__write_mongo(self.response.json())
            return self.response.json()
        else:
            logging.warning(f"Информация об игроке {self.player_id} не получена")
            return False

    def text(self, url):
        self.response = requests.post(f'{config.DOTA_API}{url}')

    async def __write_mongo(self, resp):
        result = await mathes.write_matches_user(resp)
        if result:
            return True
        else:
            return False


# 137129583
# yatoro 321580662

# a = GetPlayerMatch(63070626)
# start = time.time()
# b = PlayerData(**a.get_information_about_player(f"/players/{a.player_id}"))
# print(b)
# b = a.get_information_about_player(f"/players/{a.player_id}/recentMatches")
# print(a.get_information_about_player(f"/players/{a.player_id}/wl"))
# print(b)
# print(a.get_information_about_player(f"/players/{a.player_id}/matches"))
# print(a.get_information_about_player(f"/players/{a.player_id}/peers"))
# print(a.get_information_about_player(f"/players/{a.player_id}/pros"))
# print(a.get_information_about_player(f"/players/{a.player_id}/totals"))
# print(a.get_information_about_player(f"/players/{a.player_id}/counts"))
# print(a.get_information_about_player(f"/players/{a.player_id}/histograms"))
# print(a.get_information_about_player(f"/players/{a.player_id}/wardmap"))
# print(a.get_information_about_player(f"/players/{a.player_id}/wordcloud"))
# print(a.get_information_about_player(f"/players/{a.player_id}/ratings"))
# print(a.get_information_about_player(f"/players/{a.player_id}/rankings"))
# print(a.get_information_about_player(f"/players/{a.player_id}/rankings"))
#
# #post
#
# print(a.text(f"/players/{a.player_id}/refresh"))
# print(time.time() - start)
