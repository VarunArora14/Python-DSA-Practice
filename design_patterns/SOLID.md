### SOLID

- **Single Responsibility Principle** - A class must have only one responsibility - easier to understand, maintain
- **Open-Closed Principle** - Software entities (classes, methods, modules) should be open for extension but closed for modification
- **Liskov Substitution** - The derived classes of base classes must be replacable where instances of base classes are expected without breaking the application
- **Interface Segregation** - The idea is to prevent fat/bloated interfaces that include methods that are not required by all clients. Make them smaller and specific so clients depend on methods they actually need, promoting loose coupling and better code organization
- **Dependency Inversion** - It means class should not depend on another class but on abstraction of this class. Instead of creating dependency clients inside the class methods/constructors, pass them as parameters instead for better testing and loose coupling
- 
