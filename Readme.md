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

##### • There is no need to manually create the database structure as it has been defined in the Supervisor.sql file. Please refer to Step .. for creating the database structure directly .

### Steps to start the program

##### 1. Download and install MySQL from https://dev.mysql.com/downloads/installer/ . This project uses MySQL 5.1.

##### 2. Use "pip install mysql" to install mysql in python.

##### 3. Use "pip install mysql-connector" to install ODBC connector for mysql.

##### 4. Modify the configuaration at line number 299 of the SuperAllocation.py file and change user='your_username',passwd="your_password".Replace your_username with the username of the configured MySQL username in step 1 and your password with the configured password in step 1.

##### 5. Open MySQL and create a database python using the command "create database python;" followed by "use python" .

##### 6. Open command prompt in administrator mode in the folder and type the following commnad : "mysqldump -u your_username -p python >Supervisor.sql" and hit enter. Now in the MySQL type "show tables". A list of three tables namely Student, Supervisor, and Temp will be visible. In case there is any error or issue kindly refer to https://www.sqlshack.com/how-to-backup-and-restore-mysql-databases-using-the-mysqldump-command/#:~:text=Mysqldump%20is%20a%20command%2Dline,delimited%20text%2C%20or%20CSV%20format .

##### 7. Now your project is ready to be executed. Run the SupervisorAllocation.py file either directly or through a code editor and you will have a tkinter page opened in the taskbar. Open that page and you will be able to navigate through the GUI.