from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import mock

from yaci import cache_manager


class TestCacheManager(object):

    def setup(self):
        self.test_storage = {'foo': 'bar', 'baz': 'boo'}
        self.mock_storage = mock.MagicMock()
        self.mock_storage.get.side_effect = self.getitem
        self.mock_storage.store.side_effect = self.setitem
        self.mock_storage.cached.side_effect = lambda x: x in self.test_storage
        self.cache_manager = cache_manager.CacheManager(self.mock_storage)

    def getitem(self, key):
        return self.test_storage[key]

    def setitem(self, key, value):
        self.test_storage[key] = value

    def teardown(self):
        pass

    def test_init(self):
        cm = self.cache_manager
        msg = "Unexpected value for storage."
        assert cm.storage == self.mock_storage, msg

    def test_get(self):
        cm = self.cache_manager

        for key, value in self.test_storage.items():
            expected = self.test_storage[key]
            actual = cm[key]
            msg = "Expected %s got {0}, for key {1}".format(expected, actual)
            assert expected == actual, msg

    def test_store(self):
        cm = self.cache_manager
        key = 'boob'
        value = 'food'

        cm[key] = value
        actual = cm[key]
        msg = "Expected {0} got {1}, for key {2}".format(value, actual, key)
        assert value == actual, msg

    def test_default_get(self):
        cm = self.cache_manager
        key = 'braut'
        value = 'vurst'

        def do_something(x):
            return x

        actual = cm.default_get(key, do_something, value)
        msg = "Expected {0} got {1}, for key {2}".format(value,
                                                         actual,
                                                         key)

        assert value == actual, msg
