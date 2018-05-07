=====
Simple crud app with Django Rest, Vue.js, Element UI
=====

For install and run example use (for run bash files use Cmder)
-----------

## How to run:

```zsh
git clone https://github.com/skortabeast/simplecrud_djangorest_vue.git
```

```zsh
Run frontend side:
```
sh run_front.sh

```zsh
Run backend:
```
sh run_back.sh

OR

```zsh
Run frontend side:
```
cd simplecrud_djangorest_vue\frontend\simplecrud\

yarn install
yarn run dev

Frontend:  http://localhost:8080

```zsh
Run backend:
```
cd simplecrud_djangorest_vue\

pip install -r backend/requirements.txt
python backend/manage.py makemigrations listofusers
python backend/manage.py migrate
python backend/manage.py runserver

Backend: http://localhost:8000/

For good work go to http://localhost:8000/api/ and add new role(admin or user) 

![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/main_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/add_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/delete_page.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/edit.png)
