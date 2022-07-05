import timeit
import asyncio


def time(func):
    async def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        await func(*args, **kwargs)
        print(f"\n\nExecution time: {timeit.default_timer() - start}")
    return wrapper


async def send_request(number: int):
    print(f"Sending request No.{number}...")
    await asyncio.sleep(1) # имитируем задержку
    print(f"Request No.{number} is send successfully!")
        

@time
async def main():
    request_count = 1
    request1 = asyncio.create_task(send_request(request_count))
    request_count += 1
    request2 = asyncio.create_task(send_request(request_count))

    await request1
    await request2


if __name__ == '__main__':
    asyncio.run(main())
