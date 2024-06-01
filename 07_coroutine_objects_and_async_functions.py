import asyncio
import inspect

# coroutines are the objects that have the ability to resume underlying function that has been suspended before completion 
# This makes coroutine objects awaitable (meaning -> use them in await expressions)
async def main():
    pass


print(type(main)) # <class 'function'>

# to differentiate function with coroutinefunction
print(inspect.iscoroutinefunction(main)) # True

print(type(main())) # <class 'coroutine'>

print(dir(main()))

# ['__await__', '__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__le__', '__lt__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'cr_await', 'cr_code', 
# 'cr_frame', 'cr_origin', 'cr_running', 'cr_suspended', 'send', 'throw']
