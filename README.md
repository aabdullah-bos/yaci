# Yet Another Cache Implementation

So you may be asking "Is there really a need for yet another cache
implementation?" I mean we already have:
- the [memoize pattern](https://dbader.org/blog/python-memoization)
- [pymemcache](https://github.com/pinterest/pymemcache) - A comprehensive, fast, pure-Python memcached client
- [DiskCache](http://www.grantjenks.com/docs/diskcache/) - An Apache2 licensed disk and file backed cache library, written in pure-Python
- [minicache](https://github.com/duboviy/minicache) - Python memory caching utilities for Python 2 and 3 versions, also PyPy.
- [pylibmc](https://github.com/lericson/pylibmc) - A Python wrapper around the libmemcached interface from TangentOrg.
- the [memento pattern](http://code.activestate.com/recipes/286132-memento-design-pattern-in-python/) - a way of saving state

The answer is no, there are plenty of caching libraries and patterns out
there and yet another one isn't necessary, so with that being said,
here is **Y**et **A**nother **C**aching **I**nterface.

## Motivation

I needed a caching interface that allowed me to change or implement
different storage backends as needed. I also wanted a caching implementation whose interface closely resembled the Python `collections.MutableMapping` interface, so that I could easily switch between dictionaries and other storage backends.

## Installing

To install the package run: `pip install yaci`
