# std
from time import sleep
from random import randint


def SayHello(name: str, max_delay_sec: int) -> str:
    sleep(randint(0, max_delay_sec))
    return f"Hello {name}"
