import pytest


def fib(n):
    return 1


def test_fib_pass():
    assert fib(1) == 1


def test_fib_fail():
    assert fib(6) == 8
