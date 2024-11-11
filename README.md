# User registration using PostManAPI and MySQL DB

## **Step by step guide to use this project** 

1)	Download this project by clicking “<>code” -> Download zip then save on local machine and extract the project.

2)	Open VSCode and Go to file Open folder And Click on Project and go inside that folder and select “User Registration Using Postman API and MySQL DB”(If you saved it in download folder your path will be like 
    this- “D:\Downloads\User-Registration-Using-Postman-API-and-MySQL-DB-main”) Click Select Folder

3)	Open MySQL and paste below things as it is -

    CREATE DATABASE registration_db;

    USE registration_db;

    CREATE TABLE Registration ( ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(50) NOT NULL, Email VARCHAR(50) UNIQUE NOT NULL, DateOfBirth DATE, PhoneNumber VARCHAR(15), Address VARCHAR(100));

4)	Download the postman from “postman.com” open and minimize.

5)	After creating the registration table go to vscode and Paste all the below things in vscode terminal  –

    Cd Backend
    pip install flask-cors
    pip install Flask mysql-connector-python

6)	In vscode -> Backend -> app.py –
   
    Replace the password of your Mysql db and rest same
    After that in vscode terminal type as below to start the server
    
    python app.py 

7)	After server starts You will see http://127.0.0.1:5000 this in the terminal
   
8)	Open postman and click on + and Paste http://127.0.0.1:5000/register this in the url input container because we have to check the endpoints from the register and below container click on Body -> raw and           change it too JSON.
    Set request to POST and paste below thing in the Space below and perform Various CRUD operations.
    
    {
      "name": "Vishwa",
      "email": "Vishwa@example.com",
      "date_of_birth": "2004-03-07",
      "phone_number": "8529865322",
      "address": "Bengaluru"
    }
    
    Then Click on Send And youll see the message 
    {
        "message": "Registration created successfully!"
    }
    And if it shows like this on postman terminal its Connected!

9)	Go to mysql and write as below to check if the data being stored in the Mysql database.

    select *from registration;
    
    If You want to perform CRUD operations Using FrontEnd Coninue..
  	
11)	Open the project folder
     
    D:\Downloads\User-Registration-Using-Postman-API-and-MySQL-DB-main\User-Registration-Using-Postman-API-and-MySQL-DB-main\FrontEnd
    
    Open index.html In browser to see the frontend and You can fill the details in the html form and Click on submit. 
    
    And Do fill form with 2-3 user details and refresh the page you will see the all the registration details with edit and delete working buttons and if you want to confirm if the data is being stored in Mysql       Db then go to Mysql and Paste below query to see all the registrations.
    
    select *from registration;


Everystep is mandatory and if you find any Error or facing any problem feel free to reachout at vishwamadari2@gmail.com Anytime!

### THANK YOU! 






