# interpreter_billing

1. Go to a folder where you normally store your projects
2. Clone the project:
```shell
git clone https://github.com/jumasheff/interpreter_billing.git
```
3. After cloning, you will see a folder named `interpreter_billing`. `cd` there

4. Inside `interpreter_billing` directory create a virtual environment:
```shell
python3 -m venv env
```

5. ... and activate environemnt:
```shell
source env/bin/activate
```

6. ... and (optionally) upgrade pip:
```shell
pip install --upgrade pip
```

7. ... and install Django
```shell
pip install django
```

8. ... and create migrations
```shell
./manage.py makemigrations
```

9. ... and apply migrations
```shell
./manage.py migrate
```

10. ... and run dev server:
```shell
./manage.py runserver
```