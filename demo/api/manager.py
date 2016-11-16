import logging
from threading import Thread

import sys

from demo.api.clients import (
    BananaClient,
    MagicClient,
    RoombaClient,
)


class ApiWorker(Thread):
    def __init__(self, client, keyword):
        super().__init__(daemon=True)
        self.client = client
        self.keyword = keyword
        self.result = None
        self.done = False

    def run(self):
        self.result = self.client.search(self.keyword)
        self.done = True


class ApiManager:
    def __init__(self, cache):
        self.logger = logging.getLogger(__name__)
        self.clients = [
            BananaClient(cache),
            MagicClient(cache),
            RoombaClient(cache)
        ]

    def search(self, keyword):
        # Get the worker threads ready
        workers = [ApiWorker(client, keyword)
                   for client in self.clients]

        # Put all the workers to work.
        results = list()
        for worker in workers:
            worker.start()

        # Periodically check up on the workers to see if they are done.  If they
        # are, get their result and kick them out of the pool.  Continue to do
        # this until all of the workers are done.
        while len(workers) > 0:
            for worker in workers:
                if worker.done:
                    results.append(worker.result)
                    workers.remove(worker)

        return results


if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    manager = ApiManager()
    r = manager.search('bats')
    print(r)
    r = manager.search('bats')
    print(r)
