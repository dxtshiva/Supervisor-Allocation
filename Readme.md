## Supervisor Allocation System using Python and MySQL

##### This project is an imitation of how supervisor is allocated to a student. This project has been developed using tkinter as the GUI interface and mysql as the backend database.

### Home Page

##### The home page provides three options : 

##### a) To login for the the registered students

##### b) To register as a new student

##### c) To request for supervisor if a registered student is not assigned a supervisor

### Login Page

##### It asks for the username, password and type i.e. whether a student is logging in or a supervisor is logging in and based on that it check for the credentials and redirects to their respective pages.

### Registration Page

##### It asks for the details of the user and register him/her to the database.

### Request Page

##### It takes registration  number and username of the student as input and assigns him/her the supervisor based on the specialization 

### Student Page

##### It displays the details of the supervisor allocated to the student

### Supervisor Page

##### It displays a list of all the studdents that have been assigned to the supervisor

### Points to remember

##### • You need to install mysql and configure it beforehand.

##### • The configuaration of mysql needs to be specified in the Supervisor.py file line number 299 in order to run the project properly.

##### • You also need to create the database sturcture in MySQL in order to ensure proper execution of the project. 

##### • There is no need to manually create the database structure as it has been defined in the Supervisor.sql file. Please refer to Step .. for creating the database structure properly.