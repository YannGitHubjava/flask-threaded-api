from random import randint
from time import sleep

from .base import ApiClient, cached


class RoombaClient(ApiClient):
    def __init__(self, cache):
        super().__init__('roomba', cache)

    @cached
    def search(self, keyword):
        self.logger.warning('Roomba client started search for: ' + keyword)
        # Pretend to wait for the request
        for i in range(1, 6):
            time = randint(50, 100) / 100
            sleep(time)
            self.logger.warning('Roomba client progress: {}%'.format(i * 20))
        self.logger.warning('Roomba client finished search for : ' + keyword)
        return 'Cat on a Roomba'
