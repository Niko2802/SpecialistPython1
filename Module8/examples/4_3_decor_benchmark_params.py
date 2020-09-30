def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


# DEMO
if __name__ == "__main__":
    @benchmark(iters=10)
    def fetch_webpage(url):
        import requests
        webpage = requests.get(url)
        return webpage.text


    webpage = fetch_webpage('https://google.com')
    # print(webpage)
