import asyncio


async def stopwatch():
    count = 0
    # Infinite Loop
    while True:
        await asyncio.sleep(1)
        count += 1
        print(count)


async def main():
    # Running coroutine
    task = asyncio.create_task(stopwatch())
    await asyncio.sleep(3)
    # To cancel coroutine
    task.cancel()


asyncio.run(main())
