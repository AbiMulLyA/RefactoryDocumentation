import asyncio
import time

# def hello(delay, name):
#     time.sleep(delay)
#     print(name)

# def main():
#     print(f"started at {time.strftime('%X')}")
#     hello(2, "budi")
#     hello(3, "aminah")
#     hello(1, "jaya")
#     print(f"started at {time.strftime('%X')}")

# main()

# convert to coroutine way of python
# async def hello(delay, name):
#     await asyncio.sleep(delay)
#     print(name)

# async def main():
#     print(f"started at {time.strftime('%X')}")
#     await hello(2, "budi")
#     await hello(3, "aminah")
#     await hello(1, "jaya")
#     print(f"started at {time.strftime('%X')}")

# asyncio.run((main()))

async def hello(delay, name):
    await asyncio.sleep(delay)
    print(name)

# asyncio.create_task()
async def main():
    print(f"started at {time.strftime('%X')}")
    # Task1 = asyncio.create_task(hello(2,"budi"))
    # Task2 = asyncio.create_task(hello(3,"aminah"))
    # Task3 = asyncio.create_task(hello(1,"jaya"))
    # await Task1
    # await Task2
    # await Task3
    # TaskFuture = asyncio.ensure_future(hello(2,"budi"))
    # await TaskFuture
    # print(type(TaskFuture))
    TaskGather = asyncio.gather(hello(1,"budi"),hello(2,"amin"),hello(3,"aminah"))
    await TaskGather
    print(type(TaskGather))
    # print(type(Task1))
    # print(type(Task2))
    # print(type(Task3))
    print(f"started at {time.strftime('%X')}")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
asyncio.run((main()))


# aiohttp

# https://dev.to/matteo/async-request-with-python-1hpo
