import asyncio
# Import asynccontextmanager decorator from contextlib
from contextlib import asynccontextmanager

# `asynccontextmanager` are convinient to work with `Network Connections`
# Inorder to use this function in with Statement, this function should `yeild` something
@asynccontextmanager
async def connection():
    print('Setting up connection')
    # asyncio.sleep is just to mimic the network connection
    await asyncio.sleep(1)

    # In yeild retrun a `real connection object`
    yield {'driver': 'sqlite'}

    # asyncio.sleep is just to mimic the network connection
    await asyncio.sleep(1)
    print('Shutting down')


async def main():
    # Calling async function using `with` statement
    # The value of yeild will be stored in db
    async with connection() as db:
        # use yeild to run piece of code here
        print(db, 'is ready')

asyncio.run(main())
