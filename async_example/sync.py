import timeit
from time import sleep


def time(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        print(f"\n\nExecution time: {timeit.default_timer() - start}")
    return wrapper


def send_request(number: int):
    print(f"Sending request No.{number}...")
    sleep(1) # имитируем задержку
    print(f"Request No.{number} is send successfully!")
        


@time
def main():
    request_count = 1
    send_request(request_count)
    request_count += 1
    send_request(request_count)


if __name__ == '__main__':
    main()
