# JSON Parser comparison

```text
$ python main.py
> Dump
json : 3.2870473861694336 [s]
orjson : 0.5628752708435059 [s]
rapidjson : 1.7613952159881592 [s]
hyperjson : 1.381042718887329 [s]
simdjson : 3.28767728805542 [s]
simplejson : 4.896097183227539 [s]
ujson : 1.1491625308990479 [s]
> Load
json : 2.565263032913208 [s]
orjson : 0.8250467777252197 [s]
rapidjson : 1.7073149681091309 [s]
hyperjson : 1.9152252674102783 [s]
cysimdjson : 0.5973670482635498 [s]
simdjson : 1.3114981651306152 [s]
simplejson : 3.0985052585601807 [s]
ujson : 1.136885166168213 [s]
```
