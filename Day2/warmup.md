# Types of data 

* Int
* Float
* String

## = is *not* "equal to"
= means assignment!
- Variables are assigned their value by using an assignment statement, aka an `=`. 
- Any values on the right side are calculated before it is assigned.
- i.e. `time = 3 + 4 + int(input("Time))` 

## Variables are an identifier that stores a value

`number = 20` is a variable. 

```py
numberOne = 4
numberTwo = 10
numberOne = numberTwo
print(numberTwo)
```

The answer is 10, because of the rule stated above. 

```python
numberOne = 4
numberTwo = 10
numberOne = numberTwo
numberTwo = 7
print(numberOne)
```
The answer is 10, because numberOne is passed to numberTwo at line 3, but the number is not reassigned after.

## Naming rules
* No white space
* Cannot start with a number
* Numbers have to be within name
* Only _ is allowed
* No reserved words
### Industry Standard
* ALL CAPS for CONSTANT variables.
* Name variables about what they respresent.
  * these do not affect the code running but it is a bad practice. 

 