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

- ### **_Exclamation Mark_** `!`: Doesn't do anything on it's own. Combining it with `=` makes the not equality operator.

```python
x = 4
if x != 5:
    print("x is not equal to 5")
```

---

- ### **_Question Mark_** `?`: Doesn't do anything in Python.

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

---

- ### **_Brackets_** `( )`: Mainly used in functions, create tuples and packing.

---

- ### **_Curly Brackets_** `{ }`: Mainly used to create dictionaries or sets, and in f-strings.

---

- ### **_Square Brackets_** `[ ]`: Mainly used to create lists, access dictionary and tuple items.

---

- ### **_Plus Sign_** `+`: The plus operator.

---

- ### **_Minus Sign_** `-`: The minus operator.

---

- ### **_Underscore_** `_`: The only character that can be inside a variable name.

---

- ### **_Equal Sign_** `=`: Assignment operator. It can be combined with other punctuations to create combined assignment operators like: `+=`, `-=`, `*=`, `/=`, `%=` and `==`.

---

- ### **_Slash_** `/`: Mainly used for true division `/` and floor division `//`.

---

- ### **_Backslash_** `\`: Mainly used as an escape character. Used also to split a long line of code into multiple lines.

---

- ### **_Pipe Sign_** `|`: Bitwise Or operator.

```python
a = 0b01010101
b = 0b10101010

x = a | b

print(bin(x))

>> 0b11111111
```

---

- ### **_Semicolon_** `;`: Used to squeeze multiple lines of code into one.

---

- ### **_Colon_** `:`: Used in control structures (if else, loops, ...), function definition, try except blocks.

---

- ### **_Single/Double Quotes_** `' "`: Mainly used with strings.

---

- ### **_Less/More than_** `< >`: Comparison operators, they can be combined with `=` to create `<=` and `>=`. They are also used as a left/right shifts operators.

```python
a = 0b110011

print(bin(a))
print(a)

# Left Shift === Multiplication by 2
print(bin(a << 1))
print(a << 1)

# Right Shift === Division by 2
print(bin(a >> 1))
print(a >> 1)
```

---

- ### **_Comma_** `,`: Used to separate the arguments/parameters for a function. It separates the elements in lists, dictionaries, sets and tuples.

---

- ### **_Full Stop_** `.`: Used to access either the methods or the attributes of an object.
