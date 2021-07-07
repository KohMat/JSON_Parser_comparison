import json
import time

import cysimdjson
import hyperjson
import numpy as np
import orjson
import rapidjson
import simdjson
import simplejson
import ujson
import os

print("# JSON Parser comparison", end="\n\n")

data = {
    "timestamp": 1556283673.1523004,
    "images": np.random.rand(5, 3, 224, 224).tolist(),
    "trajectories": np.random.rand(30, 5, 3, 8).tolist(),
}

test_times = 20

file_path = "./test.json"
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

file_size = os.path.getsize(file_path) / (1024 * 1024)

print(
    f"The elapsed durations for {test_times} operations (dump, load, loads) on a {file_size:.2f}MB json file or equivalent data.",
    end="\n\n",
)


def dump_benchmark(name, dumps):
    start = time.time()
    for _ in range(test_times):
        dumps(data)
    print(f"{name}: {time.time() - start:5f}[s]")


print("```text")
print("> Dump")
dump_benchmark("json", json.dumps)
# orjson only outputs bytes, but often we need unicode:
dump_benchmark("orjson", lambda s: str(orjson.dumps(s), "utf-8"))
dump_benchmark("rapidjson", rapidjson.dumps)
dump_benchmark("hyperjson", hyperjson.dumps)
dump_benchmark("simdjson", simdjson.dumps)
dump_benchmark("simplejson", simplejson.dumps)
dump_benchmark("ujson", ujson.dumps)

small_json = json.dumps(data)


def loads_benchmark(name, loads):
    start = time.time()
    for i in range(test_times):
        loads(small_json)
    print(f"{name}: {time.time() - start:5f}[s]")


print("> Loads")
loads_benchmark("json", json.loads)
loads_benchmark("orjson", orjson.loads)
loads_benchmark("rapidjson", rapidjson.loads)
loads_benchmark("hyperjson", hyperjson.loads)
loads_benchmark(
    "cysimdjson", lambda s: cysimdjson.JSONParser().parse(s.encode("utf-8"))
)
loads_benchmark("simdjson", simdjson.loads)
loads_benchmark("simplejson", simplejson.loads)
loads_benchmark("ujson", ujson.loads)


def load_benchmark(name, load, use_loads=False):
    start = time.time()
    for i in range(test_times):
        f = open(file_path, "r")
        if not use_loads:
            load(f)
        else:
            load(f.read())
    print(f"{name}: {time.time() - start:5f}[s]")


print("> Load")
load_benchmark("json", json.load)
load_benchmark("rapidjson", rapidjson.load)
load_benchmark("hyperjson", hyperjson.load)
load_benchmark("orjson", orjson.loads, use_loads=True)
load_benchmark(
    "cysimdjson",
    lambda s: cysimdjson.JSONParser().parse(s.encode("utf-8")),
    use_loads=True,
)
load_benchmark("simdjson", simdjson.load)
load_benchmark("simplejson", simplejson.load)
load_benchmark("ujson", ujson.load)

print("```")
