```
pip install Django
pip install psycopg2
django-admin startproject project
cd .\project\
django-admin startapp app
python manage.py inspectdb > models.py
(python manage.py makemigrations)
python manage.py runserver 
```
(также удаляем новый models.py после перенесения данных в старый)


\copy table (columns) FROM 'path' DELIMITER ';' CSV HEADER
![image](https://github.com/user-attachments/assets/a1cb3a98-35d4-47b4-bc02-de0c742c1b01)
![image](https://github.com/user-attachments/assets/820e897b-3ed7-4cd5-ae3d-4a6e0805dd38)
![image](https://github.com/user-attachments/assets/8cc94fe2-4159-4278-a402-50c05b39f620)
![image](https://github.com/user-attachments/assets/35434df2-dc29-41a2-9085-4d8b5762fc29)
