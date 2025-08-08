# Day 17: Exceptions

Welcome to **Day 17** of the 30 Days of Python Challenge!

## 📚 Topics Covered
- Introduction to exceptions
- Handling exceptions with `try`, `except`, `else`, and `finally`
- Raising exceptions with `raise`
- Creating custom exception classes

## 📝 Tasks
- Practice handling different types of exceptions
- Write code that raises and catches exceptions
- Implement custom exception classes

## 🚀 Resources
- [Python Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Exceptions](https://realpython.com/python-exceptions/)

## 💡 Example

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution complete.")
```

Happy coding! 🚀