def f(a):
    return a*a

x = [1,3,4]
print(f(x[1]))

def test_f():
    assert f(5) == 25

def test_f2():
    assert f(3) == 8

class TestClass:
    def test_f3(self):
        assert f(2) == 4

    def test_f4(self):
        assert f(4) == 16