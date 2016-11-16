import logging
from functools import wraps
from datetime import (
    datetime,
    timedelta,
)


class CachedResponse:
    def __init__(self, content, max_age):
        self.content = content
        self.max_age = max_age
        self.timestamp = datetime.now()


class DumbCache:
    def __init__(self):
        self.storage = dict()
        self.logger = logging.getLogger('demo.api.clients.base.DumbCache')

    def put(self, request, content, max_age=(60 * 5)):
        self.logger.debug('Cache PUT: {} - {}'.format(*request))
        max_age = timedelta(seconds=max_age)
        response = CachedResponse(content, max_age)
        self.storage[request] = response

    def get(self, request):
        self.logger.debug('Cache GET: {} - {}'.format(*request))
        response = self.storage.get(request, None)
        if response is None:
            self.logger.debug('Cache MISS: {} - {}'.format(*request))
            return

        age = datetime.now() - response.timestamp
        if age > response.max_age:
            self.logger.debug('Cache EXPIRED: {} - {}'.format(*request))
            del self.storage[response]
            return

        self.logger.debug('Cache HIT: {} - {}'.format(*request))
        return response.content


def cached(f):
    @wraps(f)
    def wrapped(self, keyword):
        content = self.cache.get((self.name, keyword))
        if content is None:
            content = f(self, keyword)
            self.cache.put((self.name, keyword), content)
        return content

    return wrapped


class ApiClient:
    def __init__(self, name, cache):
        self.logger = logging.getLogger(__name__)
        self.cache = cache
        self.name = name

    def search(self, keyword):
        raise NotImplementedError('Subclass must implement this method.')
