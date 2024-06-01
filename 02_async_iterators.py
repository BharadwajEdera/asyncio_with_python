import asyncio
import random


class EggBoiler:
    def __init__(self, amount):
        # Input (list, tuple etc..) Should be converted into Iterable object
        self.eggs = iter(range(1, amount + 1))

    # async iterables needs to implement a special method called __aiter__()
    # This method returns an object that implements __anext__()
    def __aiter__(self):
        return self

    # __anext__() needs to return awaitable object
    # return the coroutine object [Function that is used to read files / requests etc asynchronusly] 
    async def __anext__(self):
        try:
            egg = next(self.eggs)
        except StopIteration:
            raise StopAsyncIteration
        # return the coroutine object [Function that is used to read files / requests etc asynchronusly] 
        return self.boil(egg)

    # Function that is used to read files / requests etc asynchronusly
    async def boil(self, egg):
        # Here -> Code to read the files / requests (asyncio.sleep is just to replicate and can be ignore once we have original code) 
        await asyncio.sleep(random.randint(2, 5))
        print(f'Egg #{egg} is boiling')


# Here is the async main function which has async for loop
async def main():
    eggs = []
    # async for loop 
    # async iterables needs to implement a special method called __aiter__()
    # append coroutine into a list (This doesn't run the functions, just create coroutine objects)
    async for egg in EggBoiler(4):
        eggs.append(egg)
    print('We wait for the eggs to boil...')
    # asyncio.gather : TO gather all coroutine objects 
    # await : To run the coroutine objects with in async function
    await asyncio.gather(*eggs)

# asyncio.run : # await : To run the coroutine objects outside async function
asyncio.run(main())
