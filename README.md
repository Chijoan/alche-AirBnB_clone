# AirBnB Clone Project

## Description
The AirBnB Clone project is the first step in building a full web application similar to AirBnB.  
This project focuses on creating the command interpreter, managing objects, and storing data using JSON serialization.

The command interpreter allows users to create, view, update, and delete objects from different classes such as User, State, City, Amenity, Place, and Review.

---

## Project Components

The project includes:

- A **BaseModel** class that defines common attributes and methods.
- A **FileStorage** engine that serializes objects to a JSON file.
- Several classes inherited from BaseModel:
  - User
  - State
  - City
  - Amenity
  - Place
  - Review
- A command interpreter (`console.py`) for interacting with the objects.

---

## Command Interpreter

### Start the console

```bash
./console.py
