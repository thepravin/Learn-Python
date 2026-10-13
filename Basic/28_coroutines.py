'''
Coroutine : a function that can PAUSE in the middle and RESUME later.
            While it is paused (waiting), Python can run other work.

async def -> creates a coroutine function
await     -> "pause here until this finishes, run other tasks meanwhile"
asyncio   -> built-in module that runs coroutines (the "event loop" decides who runs next)

Normal function : starts -> runs to the end -> returns.
Coroutine       : starts -> pauses at await -> others run -> resumes -> returns.
'''

import asyncio
import time


# ---------------- 1. First coroutine ----------------
async def greet():
    print("Hello")
    await asyncio.sleep(1)      # pause 1 sec, NOT blocking other tasks
    print("World")

c = greet()
print(c)                        # <coroutine object greet ...> - nothing runs yet
c.close()                       # (just to avoid a warning, since we didn't run it)

asyncio.run(greet())            # asyncio.run() actually runs it


# ---------------- 2. Without coroutines: one after another ----------------
def download_sync(name):
    print(f"start {name}")
    time.sleep(1)               # blocks the whole program
    print(f"done  {name}")

start = time.time()
download_sync("file1")
download_sync("file2")
download_sync("file3")
print(f"sync time: {time.time() - start:.1f} sec")    # ~3 sec


# ---------------- 3. With coroutines: all wait together ----------------
async def download(name):
    print(f"start {name}")
    await asyncio.sleep(1)      # while waiting, other downloads start
    print(f"done  {name}")
    return f"{name} data"

async def main():
    results = await asyncio.gather(     # run all together, wait for all
        download("file1"),
        download("file2"),
        download("file3"),
    )
    print(results)              # ['file1 data', 'file2 data', 'file3 data']

start = time.time()
asyncio.run(main())
print(f"async time: {time.time() - start:.1f} sec")   # ~1 sec


# ---------------- 4. Tasks: start now, collect result later ----------------
async def cook(dish, seconds):
    await asyncio.sleep(seconds)
    return f"{dish} ready"

async def kitchen():
    rice = asyncio.create_task(cook("rice", 1))    # starts right away
    dal = asyncio.create_task(cook("dal", 0.5))
    print("chopping salad while cooking...")       # we do other work meanwhile
    print(await dal)            # dal ready
    print(await rice)           # rice ready

asyncio.run(kitchen())


# ---------------- 5. Timeout: don't wait forever ----------------
async def slow_api():
    await asyncio.sleep(5)
    return "data"

async def call_with_timeout():
    try:
        return await asyncio.wait_for(slow_api(), timeout=0.5)
    except asyncio.TimeoutError:
        return "API too slow, using default"

print(asyncio.run(call_with_timeout()))


# ---------------- 6. Real-world example: fetch many users from an API ----------------
async def fetch_user(user_id):
    await asyncio.sleep(0.5)    # pretend network call
    return {"id": user_id, "name": f"user{user_id}"}

async def fetch_all():
    limit = asyncio.Semaphore(3)            # at most 3 requests at the same time

    async def limited(uid):
        async with limit:
            return await fetch_user(uid)

    users = await asyncio.gather(*(limited(i) for i in range(1, 7)))
    print([u["name"] for u in users])

start = time.time()
asyncio.run(fetch_all())                    # 6 users, 3 at a time -> ~1 sec, not 3 sec
print(f"fetch time: {time.time() - start:.1f} sec")


# ---------------- 7. Old style: generator-based coroutine (send) ----------------
# Before async/await, generators with send() were used as coroutines.
def running_average():
    total, count = 0, 0
    avg = None
    while True:
        value = yield avg       # pause, wait for a value from send()
        total += value
        count += 1
        avg = total / count

avg = running_average()
next(avg)                       # start the generator (run to first yield)
print(avg.send(10))             # 10.0
print(avg.send(20))             # 15.0
print(avg.send(30))             # 20.0


'''
Notes:
1. Coroutines help when the program WAITS a lot (I/O-bound work):
   network/API calls, database queries, reading files, web scraping, chat servers, bots.

2. They do NOT make CPU-heavy work faster (math, image processing).
   Only one coroutine runs at a time. For CPU work use multiprocessing.

3. Inside async code use async libraries:
   time.sleep() -> asyncio.sleep()      requests -> aiohttp / httpx
   A blocking call (time.sleep, requests.get) freezes ALL coroutines.

4. await can be used only inside async def.
   asyncio.run() is the starting point, call it once from normal code.

5. Calling a coroutine function does not run it. It must be awaited or passed to asyncio.run().

Real-world usage:
- FastAPI / aiohttp web servers -> handle thousands of users at once
- Calling many APIs together (price comparison, weather for many cities)
- Web scraping many pages
- Chat apps, Discord/Telegram bots, WebSockets
- Async database drivers (asyncpg, motor)

| Normal function     | Coroutine                          |
|---------------------|------------------------------------|
| def                 | async def                          |
| runs to the end     | can pause at await and resume      |
| blocks while waiting| lets other tasks run while waiting |
| call: f()           | run: await f() / asyncio.run(f())  |
'''
