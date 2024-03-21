# Every Punctuation in Python

- ### **_Backtick_** `` ` ``: Doesn't do anything in Python.

---

- ### **_Tilde_** `~`: Bitwise Not operator.

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

- ### **_Modulo_** `%`: This is the modulo operator, the remain of division. It's also used to format strings.

```python
x = 98

print(x%2, x%3, x%5, sep=" ___ ")
>> 0 ___ 2 ___ 3

print("x = %s" % x)
>> x = 98
```

---

- ### **_Caret_** `^`: Bitwise Exclusive Or (XOR).

```python
a = 0b1111000010
b = 0b0000111110

x = a ^ b

print(bin(a), bin(b), bin(x), sep=" ___ ")
print(a, b, x, sep=" ___ ")

>> 0b1111000010 ___ 0b111110 ___ 0b1111111100
>> 962 ___ 62 ___ 1020
```

---

- ### **_Ampersand_** `&`: Bitwise And operator.

```python
a = 0b00110011
b = 0b11110000

x = a & b

print(bin(x))

>> 0b110000
```

---

- ### **_Asterisk_** `*`: The uses are:

  - ### Multiplication operator

  ```python
  print(4 * 5)
  print(3 * "Hello ")

  >> 20
  >> Hello Hello Hello
  ```

  - ### Unpacking operator

  ```python
  a, b, *others = (4, 5, 12, 4, 5, -2)
  print("a = %s, b = %s, others = %s" % (a, b, others))

  >> a = 4, b = 5, others = [12, 4, 5, -2]
  ```

  - ### Allow any number of positional arguments: as a tuple

  ```python
  def say_hello(*args):
      print(args)


  say_hello("Choaib", 22, "ENSA")
  >> ('Choaib', 22, 'ENSA')

  ```

  - ### Allow any number of keyword arguments: as a dictionary

  ```python
  def say_hi(**kwargs):
      print(kwargs)


  say_hi(name="Choaib", age=22, school="ENSA")
  >> {'name': 'Choaib', 'age': 22, 'school': 'ENSA')
  ```

  - ### Import everything from a module

  ```python
  from module_name import *
  ```
