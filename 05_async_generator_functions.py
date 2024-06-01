import asyncio

# async generator functions are just like regular async functions , expect they have yeild keyword in them

# async generator for mimicing the dowload of couple of urls
# Without yeild keyword : This function returns coroutine object
# With yeild keyword : This function returns async_generator object
async def download(urls):
    for url in urls:
        await asyncio.sleep(1)
        response = {'status': 200, 'data': f'content of {url}'}
        yield response


async def main():
    urls = [
        'google.com',
        'bing.com',
        'duckduckgo.com',
    ]

    async for value in download(urls):
        print(value)

asyncio.run(main())
