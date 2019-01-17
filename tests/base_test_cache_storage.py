from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import pytest


class BaseTestCacheStorage(object):
    def create_cache_storage(self):
        raise NotImplementedError("To be implemented by subclass")

    def cleanup_cache_storage(self, cache_storage):
        raise NotImplementedError("To be implemented by subclass")

    def generate_data(self):
        raise NotImplementedError("To be implemented by subclass")

    def generate_value(self):
        raise NotImplementedError("To be implemented by subclass")

    def generate_key(self):
        raise NotImplementedError("To be implemented by subclass")

    def setup(self):
        self.storage = self.create_cache_storage()
        self.key = self.generate_key()
        self.value = self.generate_value()

    def teardown(self):
        self.cleanup_cache_storage(self.storage)

    def test_key_value_store(self):
        self.storage.store(self.key, self.value)
        actual = self.storage.get(self.key)
        fail_msg = "The value {0} stored with key {1}, expected {2}".format(str(actual),
                                                                            self.key,
                                                                            str(self.value))
        assert self.value == actual, fail_msg

    def test_is_cached(self):
        expected = True
        self.storage.store(self.key, self.value)
        actual = self.storage.cached(self.key)
        fail_msg = "Expected {0}, got {1}. Eexpected {2} to be cached".format(expected,
                                                                              actual,
                                                                              self.key)
        assert expected == actual, fail_msg

    def test_not_cached(self):
        expected = False
        actual = self.storage.cached(self.key)
        fail_msg = "Expected {0}, got {1}. Did not expect {2} to be cached".format(expected,
                                                                                   actual,
                                                                                   self.key)
        assert expected == actual, fail_msg

    def test_clear(self):
        expected = 0
        self.storage.store(self.key, self.value)
        assert self.storage.size > 0, "To test clear cache cannot be empty"
        self.storage.clear()
        actual = self.storage.size
        fail_msg = "Expected {0} got {1} The cache is not empty".format(expected, actual)
        assert expected == actual, fail_msg

    def test_size(self):
        expected = 1
        self.storage.store(self.key, self.value)
        actual = self.storage.size
        fail_msg = "Expected {0} got {1}. Unexpected cache size.".format(expected, actual)
        assert expected == actual, fail_msg

    def test_delete(self):
        with pytest.raises(KeyError):
            self.storage.store(self.key, self.value)
            self.storage.delete(self.key)
            self.storage.get(self.key)
