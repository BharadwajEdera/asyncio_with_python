import asyncio


async def stopwatch():
    count = 0
    while count < 1:
        await asyncio.sleep(1)
        count += 1
        print(count)


def callb(task):
    print('task is done', task)


async def main():
    # As long as the code is running on the same Thread , the object returned by the get_running_loop() is always same
    # Each operating system thread gets it's own event loop
    print(asyncio.get_running_loop())
    task = asyncio.create_task(stopwatch())
    task.add_done_callback(callb)

    await task

asyncio.run(main())
