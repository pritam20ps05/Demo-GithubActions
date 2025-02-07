# app.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

if __name__=='__main__':
    a, b = map(int, input('Enter two numbers: ').split(' '))
    print(f'{a} + {b} = { add(a, b) }')