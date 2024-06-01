import asyncio


async def main():
    print('hello...')
    await asyncio.sleep(2)
    print('...world')


# main()
# Output -> RuntimeWarning: coroutine 'main' was never awaited

# print(main())
# Output -> <coroutine object main at 0x00000287FC2F19C0>

# await main()
# Output -> SyntaxError: 'await' outside function : await function is used only in async function

### TO run this main() coroutine we should use asyncio.run()
asyncio.run(main())
