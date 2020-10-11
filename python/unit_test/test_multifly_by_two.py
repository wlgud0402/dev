def multifly_by_two(x):
    return x * 2


def test_multifly_by_two():
    assert multifly_by_two(4) == 7
    #값이 False일시 assertError 를 일으킨다

def test_multifly_by_two():
    assert multifly_by_two(4) == 8
    #값이 True 이므로 정상적으로 작동한다.