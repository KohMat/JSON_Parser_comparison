# JSON Parser comparison

The elapsed durations for 20 operations (dump, load, loads) on a 29.18MB json file or equivalent data.

```text
> Dump
json: 7.031142[s]
orjson: 0.503097[s]
rapidjson: 7.423390[s]
hyperjson: 1.107033[s]
simdjson: 6.821450[s]
simplejson: 7.220219[s]
ujson: 1.675329[s]
> Loads
json: 3.104644[s]
orjson: 0.884602[s]
rapidjson: 3.353113[s]
hyperjson: 1.338105[s]
cysimdjson: 0.631090[s]
simdjson: 0.879798[s]
simplejson: 3.221970[s]
ujson: 1.736441[s]
> Load
json: 3.762387[s]
rapidjson: 6.340086[s]
hyperjson: 2.019569[s]
orjson: 1.551531[s]
cysimdjson: 1.044431[s]
simdjson: 1.395589[s]
simplejson: 3.876986[s]
ujson: 2.389583[s]
```
