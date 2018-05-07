Simple crud app with Django Rest, Vue.js, Element UI
=====

For install and run example use (for run bash files use Cmder)
-----------

## How to run:

```zsh
git clone https://github.com/skortabeast/simplecrud_djangorest_vue.git
```


Run frontend side:
```zsh
sh run_front.sh
```

Run backend:

```zsh
sh run_back.sh
```

OR

Run frontend side:

```zsh
cd simplecrud_djangorest_vue\frontend\simplecrud\
yarn install
yarn run dev
```

Run backend:

```zsh
cd simplecrud_djangorest_vue\
pip install -r backend/requirements.txt
python backend/manage.py makemigrations listofusers
python backend/manage.py migrate
python backend/manage.py runserver
```

Frontend:  http://localhost:8080
Backend: http://localhost:8000/

For good work go to http://localhost:8000/api/ and add new role(admin or user) 

![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/main_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/add_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/delete_page.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/edit.png)
