# AirBnB clone - The console
Welcome to our AirBnB Clone project! This project aims to provide a command interpreter for managing AirBnB objects. In addition, we have implemented a storage engine package that allows us to store the objects using JSON to file.

The primary goal of this project is to create a collaborative learning environment. By working together, we as contributors to this project aim to enhance our skills in developer collaboration and gain a deeper understanding of the Python programming language. Through project-based implementation, we will solidify the concepts taught and apply them in a practical setting.

We hope you find this project both educational and enjoyable. Dive in with us and explore the world of AirBnB management.


### Project Organization
```
AirBnB_clone
├── AUTHORS       <- Lists all individuals who contributed content to the repository.
├── console.py    <- Entry point of the command interpreter
├── README.md     <- The top-level README for developers using this project.
│
├───models
│   ├── amenity.py      <- Defines class Amenity which inherits from BaseModel
│   ├── base_model.py   <- Defines class BaseModel which defines all common attributes/methods for other classes
│   ├── city.py         <- Defines class City which inherits from BaseModel
│   ├── place.py        <- Defines class Place which inherits from BaseModel
│   ├── review.py       <- Defines class Review which inherits from BaseModel
│   ├── state.py        <- Defines class State which inherits from BaseModel
│   ├── user.py         <- Defines class User which inherits from BaseModel
│   ├── __init__.py     <- Initialises models directory into a python package
│   │
│   └── engine                 <- Storage engine directory
│       ├── file_storage.py    <- Initialises engine directory into a python package
│       └── __init__.py        <- Defines object storage class FileStorage
│
└───tests                      <- Directory for tests
    ├── test_console.py        <- Tests for the console.py
    │
    └───test_models            <- model package tests
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        ├── test_user.py
        │
        └───test_engine        <- engine package tests
            └───test_file_storage.py

```



## Usage/Examples

interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Run Locally

Clone the project

```bash
$ git clone https://link-to-project
```

Go to the project directory

```bash
$ cd my-project
```

Install dependencies

```bash
$ pip install *requirements
```

Start the command console and input commands

```bash
$ ./console.py
(hbnb)
```


## Lessons Learned

During the development of this project, we learned several valuable lessons some of these valuable lessons include:

1. **Planning is crucial:** Before starting any project, it is essential to plan and define the project's scope, requirements, and objectives. Planning helped us to avoid scope creep and ensured that we stayed on track during development of the project.

2. **Unit testing is essential:** Writing unit tests for each feature of the console helped us catch bugs early in the development process and ensured that each feature worked as expected.

3. **Documentation is key:** Documenting the code and the project's features is crucial for both developers and users. It helps developers understand the codebase and its functionality, and it helps users understand how to use our project, or to add more features.

4. **Code reviews are important:** Code reviews by the other team member helped us catch bugs and improve the quality of our code. It also helped us learn from each other and improve our coding skills.

Overall, this project taught us valuable lessons in project planning, testing, documentation, collaboration, and version control. We hope that our experiences can help other developers in their projects and contribute to the community.
