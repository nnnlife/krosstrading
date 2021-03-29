import krosstrading


def test_say():
    assert krosstrading.say_hello() == 'Hello World'


def test_hello_sum():
    a = [1,2,3]
    assert krosstrading.hello_sum(a) == 6
