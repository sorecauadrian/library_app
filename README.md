# 📚 library 📚

## requirements
- provide a menu-driven console-based user interface. implementation details are up to you
- employ layered architecture and classes
- have at least 20 procedurally generated items in your application at startup
- provide specifications and **pyunit test cases** for all non-UI classes and methods for the first functionality
- implement and use your own exception classes.

## problem statement
write an application for a book library. the application will store:
- **book**: `book_id`, `title`, `author`
- **client**: `client_id`, `name`
- **rental**: `rental_id`, `book_id`, `client_id`, `rented_date`, `returned_date`

![Screenshot from 2023-12-04 10-15-37](https://github.com/sorecauadrian/python_library/assets/79454929/891c8378-e70d-490e-9066-1411a68866ac)

create an application to:
1. manage clients and books. the user can add, remove, update, and list both clients and books.

![Screenshot from 2023-12-04 10-16-03](https://github.com/sorecauadrian/python_library/assets/79454929/9bea7e87-d5c6-4674-a3c3-81641b64c7a0)
   
2. rent or return a book. a client can rent an available book. a client can return a rented book at any time. only available books (those which are not currently rented) can be rented.

![Screenshot from 2023-12-04 10-16-17](https://github.com/sorecauadrian/python_library/assets/79454929/5fceadaf-4a40-4344-8645-df93aab7f9f0)
   
3. search for clients or books using any one of their fields (e.g. books can be searched for using id, title or author). the search must work using case-insensitive, partial string matching, and must return all matching items.

![Screenshot from 2023-12-04 10-16-36](https://github.com/sorecauadrian/python_library/assets/79454929/31749e51-62b2-4d01-acda-e5b12bc0bb62)
   
4. create statistics:
    - most rented books. this will provide the list of books, sorted in descending order of the number of times they were rented.
    - most active clients. this will provide the list of clients, sorted in descending order of the number of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
    - most rented author. this provides the list of book authors, sorted in descending order of the number of rentals their books have.

![Screenshot from 2023-12-04 10-16-54](https://github.com/sorecauadrian/python_library/assets/79454929/ed6981bf-1591-4073-8307-9ac6a7a9dd31)
