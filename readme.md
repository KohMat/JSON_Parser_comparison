# JSON Parser comparison

```text
$ python main.py
> Dump
Python : 3.3386030197143555 [s]
orjson : 0.5364115238189697 [s]
rapidjson : 1.6950547695159912 [s]
hyperjson : 1.400244951248169 [s]
simdjson : 3.365732431411743 [s]
> Load
Python : 2.6741044521331787 [s]
orjson : 0.8196470737457275 [s]
rapidjson : 1.6570849418640137 [s]
hyperjson : 1.8646414279937744 [s]
cysimdjson : 0.6584076881408691 [s]
simdjson : 1.3319969177246094 [s]
```