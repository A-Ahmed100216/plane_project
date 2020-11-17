# Engineering 74: Plane Project

 # Plane Project

## People Class

* Create a class for People, and initiate it with the `tax_number`, `first_name`, and `surname` variables
```python
# create a People class. Superclass of Passengers and Staff


class People:
    # initialise the class with variable
    def __init__(self, tax_number, first_name, surname):
        self.tax_number = tax_number
        self.first_name = first_name
        self.surname = surname
```

* Create some tests in an `if __name__ == "__main__"` statement so that they only run when this file is being created
