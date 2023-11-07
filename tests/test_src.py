from hello import SayHello
import pytest


def test_SayHello_one_fast():
    assert SayHello("Datadog", 1) == "Hello Datadog"


def test_SayHello_one_slow():
    assert SayHello("Datadog", 5) == "Hello Datadog"


@pytest.mark.parametrize(
    "name,delay,expected",
    [
        ("Datadog", 1, "Hello Datadog"),
        ("Datadog", 1, "Hello Datadog"),
        ("Datadog", 1, "Hello Datadog"),
    ],
)
def test_SayHello_three_fast(name: str, delay: int, expected: str):
    assert SayHello(name, delay) == expected


@pytest.mark.parametrize(
    "name,delay,expected",
    [
        ("Datadog", 5, "Hello Datadog"),
        ("Datadog", 5, "Hello Datadog"),
        ("Datadog", 5, "Hello Datadog"),
    ],
)
def test_SayHello_three_slow(name: str, delay: int, expected: str):
    assert SayHello(name, delay) == expected
