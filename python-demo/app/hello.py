import requests
from utils import math


def main():
    result = math.add(2, 3)
    r = requests.get("https://httpbin.org/get")
    print("Hello, Bazel! 2 + 3 =", result)
    print("Fetched status code:", r.status_code)


if __name__ == "__main__":
    main()
