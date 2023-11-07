import pytest
from ddtrace import tracer
from hello import SayHello


def test_SayHello_one_fast(ddspan):
    delay = 1

    # Adding custom metric
    ddspan.set_tag("artificial_delay", delay)

    # Adding custom tags
    ddspan.set_tag("test_type", "one_fast")

    assert SayHello("Datadog", delay) == "Hello Datadog"


def test_SayHello_one_slow(ddspan):
    delay = 5

    # Adding custom metric
    ddspan.set_tag("artificial_delay", delay)

    # Adding custom tags
    ddspan.set_tag("test_type", "one_fast")

    assert SayHello("Datadog", delay) == "Hello Datadog"


@pytest.mark.parametrize(
    "name,delay,expected",
    [
        ("Datadog", 1, "Hello Datadog"),
        ("Datadog", 1, "Hello Datadog"),
        ("Datadog", 1, "Hello Datadog"),
    ],
)
def test_SayHello_three_fast(name: str, delay: int, expected: str, ddspan):
    # Adding custom metric
    ddspan.set_tag("artificial_delay", delay)

    # Adding custom tags
    ddspan.set_tag("test_type", "three_fast")
    assert SayHello(name, delay) == expected


@pytest.mark.parametrize(
    "name,delay,expected",
    [
        ("Datadog", 5, "Hello Datadog"),
        ("Datadog", 5, "Hello Datadog"),
        ("Datadog", 5, "Hello Datadog"),
    ],
)
def test_SayHello_three_slow(name: str, delay: int, expected: str, ddspan):
    # Adding custom metric
    ddspan.set_tag("artificial_delay", delay)

    # Adding custom tags
    ddspan.set_tag("test_type", "ten_slow")
    assert SayHello(name, delay) == expected
