# JSON Parser comparison

```text
$ python main.py
> Dump
Python : 3.387415885925293 [s]
orjson : 0.6207790374755859 [s]
rapidjson : 1.7927534580230713 [s]
hyperjson : 1.437938928604126 [s]
simdjson : 3.363544464111328 [s]
simplejson : 4.946911573410034 [s]
ujson : 1.190354347229004 [s]
> Load
Python : 2.6382312774658203 [s]
orjson : 0.8240087032318115 [s]
rapidjson : 1.7273948192596436 [s]
hyperjson : 1.9811418056488037 [s]
cysimdjson : 0.6006309986114502 [s]
simdjson : 1.3929476737976074 [s]
simplejson : 3.139932870864868 [s]
ujson : 1.1072125434875488 [s]
```