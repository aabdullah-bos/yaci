from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import pytest
import random
import base_test_cache_storage

from yaci import dict_storage


class TestDictStorage(base_test_cache_storage.BaseTestCacheStorage):
    def create_cache_storage(self):
        return dict_storage.DictStorage()

    def cleanup_cache_storage(self, cach_storage):
        pass

    def generate_value(self):
        return random.randint(1, 42)

    def generate_key(self):
        return 'foo'


class TestNoopDictStorage(object):
    value = 8
    key = 'foo'

    def setup(self):
        self.storage = dict_storage.NoopDictStorage()
        self.storage.store(self.key, self.value)

    def teardown(self):
        pass

    def test_key_value_store(self):
        with pytest.raises(KeyError):
            self.storage.get(self.key)

    def test_cached(self):
        expected = False
        actual = self.storage.cached(self.key)
        msg = "Expected {0} got {1}. Unexpected cache size.".format(expected, actual)
        assert expected == actual, msg

    def test_clear(self):
        expected = 0
        self.storage.store(self.key, self.value)
        self.storage.clear()
        actual = self.storage.size
        msg = "Expected {0} got {1}. Unexpected cache size.".format(expected, actual)
        assert expected == actual, msg

    def test_size(self):
        expected = 0
        self.storage.store(self.key, self.value)
        actual = self.storage.size
        msg = "Expected {0} got {1}. Unexpected cache size.".format(expected, actual)
        assert expected == actual, msg

    def test_delete(self):
        with pytest.raises(KeyError):
            self.storage.store(self.key, self.value)
            self.storage.delete(self.key)
            self.storage.get(self.key)
