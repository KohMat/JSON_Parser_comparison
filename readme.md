# JSON Parser comparison

```text
$ python main.py
> Dump
Python : 3.5569474697113037 [s]
orjson : 0.5837197303771973 [s]
rapidjson : 1.767397165298462 [s]
hyperjson : 1.4463107585906982 [s]
simdjson : 3.543241024017334 [s]
simplejson : 5.110836744308472 [s]
> Load
Python : 2.6852424144744873 [s]
orjson : 0.8452510833740234 [s]
rapidjson : 1.6857824325561523 [s]
hyperjson : 1.8773798942565918 [s]
cysimdjson : 0.6071622371673584 [s]
simdjson : 1.3136658668518066 [s]
simplejson : 3.1306400299072266 [s]
```