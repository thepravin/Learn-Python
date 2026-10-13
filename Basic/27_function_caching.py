'''
Function caching : save the result of a function call. If the function is called again
                   with the SAME arguments, return the saved result instead of running it again.

Why  : makes slow / repeated work fast (heavy calculations, API calls, database queries).
How  : functools.lru_cache or functools.cache (built-in decorators).
'''

import time
from functools import lru_cache, cache


# ---------------- 1. Problem: slow repeated work ----------------
def slow_fib(n):
    if n < 2:
        return n
    return slow_fib(n - 1) + slow_fib(n - 2)   # same values are calculated again and again

start = time.time()
print(slow_fib(30))                     # 832040
print(f"without cache: {time.time() - start:.2f} sec")   # ~0.1 - 0.3 sec


# ---------------- 2. Manual cache using a dict ----------------
memo = {}

def fib_manual(n):
    if n in memo:                       # already calculated -> return saved value
        return memo[n]
    if n < 2:
        result = n
    else:
        result = fib_manual(n - 1) + fib_manual(n - 2)
    memo[n] = result                    # save for next time
    return result

print(fib_manual(30))                   # 832040 - very fast


# ---------------- 3. lru_cache (built-in) ----------------
# LRU = Least Recently Used. When the cache is full, the oldest unused result is removed.
@lru_cache(maxsize=128)                 # keep at most 128 results
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

start = time.time()
print(fib(30))                          # 832040
print(f"with cache: {time.time() - start:.5f} sec")      # almost 0 sec

print(fib.cache_info())                 # CacheInfo(hits=28, misses=31, maxsize=128, currsize=31)
# hits    -> answer found in cache
# misses  -> function had to run
# currsize-> how many results are saved now

fib.cache_clear()                       # empty the cache
print(fib.cache_info())                 # hits=0, misses=0, currsize=0


# ---------------- 4. cache (Python 3.9+) ----------------
# Same as lru_cache(maxsize=None) -> no limit, never removes anything.
@cache
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(10))                    # 3628800


# ---------------- 5. Real-world example: slow API call ----------------
@lru_cache(maxsize=100)
def get_weather(city):
    print(f"Calling API for {city}...")  # prints only when the function really runs
    time.sleep(1)                        # pretend the API takes 1 second
    return f"{city}: 30°C"

start = time.time()
print(get_weather("Pune"))              # Calling API for Pune... -> waits 1 sec
print(get_weather("Pune"))              # from cache, no API call, instant
print(get_weather("Mumbai"))            # new city -> API call again
print(f"total time: {time.time() - start:.1f} sec")     # ~2 sec instead of 3


# ---------------- 6. Real-world example: user details from database ----------------
fake_db = {1: "Pravin", 2: "Aditya"}

@lru_cache(maxsize=1000)
def get_user(user_id):
    print(f"DB query for user {user_id}")
    return fake_db.get(user_id)

get_user(1)                             # DB query for user 1
get_user(1)                             # cached, no query
get_user(2)                             # DB query for user 2

fake_db[1] = "Pravin Nalawade"             # data changed in DB
print(get_user(1))                      # Pravin  <- OLD value (stale cache!)
get_user.cache_clear()                  # clear cache when data changes
print(get_user(1))                      # Pravin Nalawade


# ---------------- 7. Arguments must be hashable ----------------
# Cache uses arguments as dict keys -> int, str, tuple OK. list, dict, set NOT OK.
@lru_cache
def total(nums):
    return sum(nums)

print(total((1, 2, 3)))                 # 6  - tuple works
# total([1, 2, 3])                      # TypeError: unhashable type: 'list'


'''
Notes:
1. Use caching only for PURE functions -> same input always gives same output, no side effects.
   Good : math calculations, parsing, reading config, data that rarely changes.
   Bad  : random values, current time, functions that print/write/send emails.

2. Cache can become STALE -> if the real data changes, the cache still returns the old value.
   Use cache_clear() when data changes.

3. Arguments must be hashable (int, str, tuple). Lists and dicts give TypeError.

4. f(1, 2) and f(a=1, b=2) are saved as different cache entries.

5. Cache uses memory. Use maxsize to limit it. @cache has no limit -> can grow forever.

6. Don't return mutable objects (list/dict) from cached functions.
   If the caller changes the returned list, the cached copy also changes.

7. Cache lives only while the program runs. Restart = empty cache.

| Decorator               | Limit      | Use when                          |
|-------------------------|------------|-----------------------------------|
| @lru_cache(maxsize=128) | 128 items  | many different inputs, save memory|
| @lru_cache(maxsize=None)| no limit   | small, fixed set of inputs        |
| @cache                  | no limit   | same as above, shorter to write   |
'''
