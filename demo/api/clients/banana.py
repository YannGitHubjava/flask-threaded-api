from random import randint
from time import sleep

from .base import ApiClient, cached


class BananaClient(ApiClient):
    def __init__(self, cache):
        super().__init__('banana', cache)

    @cached
    def search(self, keyword):
        self.logger.warning('Banana client started search for: ' + keyword)
        # Pretend to wait for the request
        for i in range(1, 6):
            time = randint(50, 100) / 100
            sleep(time)
            self.logger.warning('Banana client progress: {}%'.format(i * 20))
        self.logger.warning('Banana client finished search for : ' + keyword)
        return 'Banana Results'
