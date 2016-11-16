import logging


class ApiClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def search(self, keyword):
        raise NotImplementedError('Subclass must implement this method.')
