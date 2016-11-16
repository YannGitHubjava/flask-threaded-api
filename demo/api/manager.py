import logging
from threading import Thread

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
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.clients = [
            BananaClient(),
            MagicClient(),
            RoombaClient()
        ]

    def search(self, keyword):
        # Get the worker threads ready
        workers = [ApiWorker(client, keyword) for client in self.clients]

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
    manager = ApiManager()
    r = manager.search('bats')
    print(r)
