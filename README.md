# Every Punctuation in Python

- ### **_Backtick_** `` ` ``: Doesn't do anything in Python.

---

- ### **_Tilde_** `~`: Bitwise not operator.

```python
x = 100
print(~x)
>> -101
```

---

- ### **_Exclamation_** `!`: Doesn't do anything on it's own. Combining it with `=` makes the not equality operator.

```python
x = 4
if x != 5:
    print("x is not equal to 5")
```

---

- ### **_At Sign_** `@`: Its main usage is in decorators.

```python
import time


def tictoc(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{ func.__name__ } executed in { '{:.2f}'.format(end - start) } seconds")

    return wrapper


@tictoc
def do_something_1():
    print("Doing something 1")
    time.sleep(2)
    print("Done something 1")


@tictoc
def do_something_2():
    print("Doing something 2")
    time.sleep(3.5)
    print("Done something 2")


do_something_1()
do_something_2()
```

---

- ### **_Hash_** `#`: It is primarily used for comments to annotate code.

---

- ### **_Dollar Sign_** `$`: Doesn't do anything in Python.

---

- ### **_Modulo_** `%`: This is the modulo operator, the remain of division.

```python
x = 98
print(x%2, x%3, x%5, sep=" ___ ")
>> 0 ___ 2 ___ 3
```
