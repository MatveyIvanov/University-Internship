import timeit
from time import sleep


request_count = 0


def time(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        print(f"\n\nExecution time: {timeit.default_timer() - start}")
    return wrapper


def send_request():
    global request_count 
    request_count += 1
    print(f"Sending request No.{request_count}...")
    sleep(1) # имитируем задержку
    print(f"Request No.{request_count} is send successfully!")
        


@time
def main():
    send_request()
    send_request()


if __name__ == '__main__':
    main()
