import asyncio

# Inorder to make this class work with async context manager
# two methods needs to be added __aenter__ and __aexit__
# Both of these methods needs to return awaitable (meaning -> Both of them should be async functions)
class Connection:
    async def __aenter__(self):
        print('Setting up a connection')
        # asyncio.sleep is just to mimic the network connection is enabled
        await asyncio.sleep(1)
        return {'driver': 'sqlite'}

    # __aexit__ has three params : exception_type, exception, traceback
    async def __aexit__(self, exc_type, exc, tb):
        # asyncio.sleep is just to mimic the network connection is disabled
        await asyncio.sleep(1)
        print('Connection is closed')


async def main():
    # Calling class object using `with` statement
    # Instance of the class will be stored in `db`
    async with Connection() as db:
        print(db, 'is ready')

asyncio.run(main())
