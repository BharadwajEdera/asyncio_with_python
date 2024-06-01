import asyncio

# Future is awaitable
# Task is a subclass of Future
# Therefore lot of methods that are used on task are available in Future


async def stopwatch():
    count = 0
    while count < 1:
        await asyncio.sleep(1)
        count += 1
        print(count)


def callb(task):
    print('task is done', task)


async def main():
    task = asyncio.create_task(stopwatch())
    task.add_done_callback(callb)
    print(asyncio.isfuture(task)) # This returns True for futures and subclasses of Futures

    await task

asyncio.run(main())
