# Documentation

1. Start by cloning the project on your computer
![image](https://github.com/Me45y63/HNGx-internship/assets/66312028/6b5a4eaf-265b-4c6c-8592-ceb43220187d)

2. Cd into stage-02-django/ from there run
   ```pip install -r requirements.txt```

3. cd into network and run the following:
4. 
   i. ```python manage.py makemigrations``` to start the migration and database
   
   ii. ```python manage.py migrate``` to save migrations
   
   iii. ```python manage.py createsuperuser``` follow the prompts and create a superuser(admin).
   
   iv. ```python manage.py runserver``` to start up the server

6. We move to the testing phase to ensure everything goes smoothly.
7. Using postman make a ```get``` request to the endpoint ```127.0.0.1:8000/api-auth/```
8. 
   ![Screenshot from 2023-09-11 21-47-16](https://github.com/Me45y63/HNGx-internship/assets/66312028/6a992012-9058-4991-8678-28a23ae51204)
9. You will obtain a csrf_token to be used in the ```post``` request, copy and use it as a header in postman.
10. 
 	![Screenshot from 2023-09-11 21-46-27](https://github.com/Me45y63/HNGx-internship/assets/66312028/05d18ba5-bc63-4df5-ba4d-423521397956)

11. Make sure to fill in the username and password fields of the superuser you created as a ```post``` request
12. 
   ![Screenshot from 2023-09-11 21-47-16](https://github.com/Me45y63/HNGx-internship/assets/66312028/07f54119-4e1a-48f8-b2f7-8ed22cb503a8)

13. Make a ```post``` request to the endpoint ```127.0.0.1:8000/api-token-auth/```
    
14. You will receive a token, copy it and use it as a header for the ```DELETE```, ```PUT``` and ```POST``` requests
15. 
    ![Screenshot from 2023-09-11 22-17-29](https://github.com/Me45y63/HNGx-internship/assets/66312028/1a6f2baa-b4a5-4ec9-841c-2c49bac5742a)

For the steps you might be wondering why we had to go through all that. The answer is simple, Authentication! We provided authentication to prevent unauthorised requests

The endpoint ```127.0.0.1:8000/api/``` receives ```GET``` (to get the resource) and ```POST```(to create a new user)

The endpoint ```127.0.0.1:8000/api/{user_id}``` receives ```GET```, ```PUT```, ```PATCH``` and ```DELETE``` requests and for that you have to be authenticated
```{user_id}``` is the ```id``` of the user from any number (1..2..3..4) provided the user exists.


# Django Test Cases

The endpoints were all tested with authentication and tokens in the ```test.py``` file

The results: 

![Screenshot from 2023-09-11 21-37-30](https://github.com/Me45y63/HNGx-internship/assets/66312028/93f34071-044d-4f72-ab9c-1a754a45067c)
