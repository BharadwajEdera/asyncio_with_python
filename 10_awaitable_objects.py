import asyncio

# await expression only works with awaitables
# 3 different type of objects that are awaitable in python
# 1. coroutine, 2.task, 3.future

# Creating custom awaitable by implementing custom await
# make sure that __await__ is in iterable
class Stopwatch:
    async def __await__(self):
        yield


async def main():
    # using Stopwatch() class as awaitable 
    await Stopwatch()


asyncio.run(main())
