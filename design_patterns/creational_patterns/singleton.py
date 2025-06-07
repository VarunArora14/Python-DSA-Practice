class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Initialising singleton!") # will be called once
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

"""
Here we create a single class to be used like a logger or config class that will be used across the project with single instance created
"""