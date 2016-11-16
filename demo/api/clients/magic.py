from time import sleep
from random import randint

from .base import ApiClient, cached


class MagicClient(ApiClient):
    def __init__(self, cache):
        super().__init__('magic', cache)

    @cached
    def search(self, keyword):
        self.logger.warning('Magic client started search for: ' + keyword)
        # Pretend to wait for the request
        for i in range(1, 6):
            time = randint(50, 100) / 100
            sleep(time)
            self.logger.warning('Magic client progress: {}%'.format(i * 20))
        self.logger.warning('Magic client finished search for : ' + keyword)
        return 'Magic Results'
