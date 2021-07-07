import json
import time

import cysimdjson
import hyperjson
import orjson
import rapidjson
import simdjson
import simplejson
import ujson

m = {
    "timestamp": 1556283673.1523004,
    "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
    "task_level": [1, 2, 1],
    "action_status": "started",
    "action_type": "main",
    "key": "value",
    "another_key": 123,
    "and_another": ["a", "b"],
}


def dump_benchmark(name, dumps):
    start = time.time()
    for _ in range(1000000):
        dumps(m)
    print(name, ":", time.time() - start, "[s]")


print("> Dump")
dump_benchmark("json", json.dumps)
# orjson only outputs bytes, but often we need unicode:
dump_benchmark("orjson", lambda s: str(orjson.dumps(s), "utf-8"))
dump_benchmark("rapidjson", rapidjson.dumps)
dump_benchmark("hyperjson", hyperjson.dumps)
dump_benchmark("simdjson", simdjson.dumps)
dump_benchmark("simplejson", simplejson.dumps)
dump_benchmark("ujson", ujson.dumps)

n = json.dumps(m)


def load_benchmark(name, load):
    start = time.time()
    for i in range(1000000):
        load(n)
    print(name, ":", time.time() - start, "[s]")


print("> Load")
load_benchmark("json", json.loads)
load_benchmark("orjson", orjson.loads)
load_benchmark("rapidjson", rapidjson.loads)
load_benchmark("hyperjson", hyperjson.loads)
load_benchmark(
    "cysimdjson", lambda s: cysimdjson.JSONParser().parse(s.encode("utf-8"))
)
load_benchmark("simdjson", simdjson.loads)
load_benchmark("simplejson", simplejson.loads)
load_benchmark("ujson", ujson.loads)
