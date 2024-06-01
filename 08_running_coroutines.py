import asyncio

# There are 3 different ways of running coroutines
# 1. asyncio.run() -> This can be used to run coroutine `outside` async function
# 2. await -> This can be used to run coroutine `inside` async function
# 3. asyncio.create_task() -> 


async def download():
    print('dowload document')


async def log():
    print('log to file')


async def main():
    print('in the main function')

    # 2. using await
    await download()

    # 3. create_task
    asyncio.create_task(log())


# 1. using asyncio
asyncio.run(main())
