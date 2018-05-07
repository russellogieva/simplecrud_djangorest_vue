Simple crud app with Django Rest, Vue.js, Element UI

For install and run example use (forrun bash files use Cmder)

git clone https://github.com/skortabeast/simplecrud_djangorest_vue.git

Run frontend side:
sh run_front.sh

Run backend:
sh run_back.sh

OR

Run frontend side:
cd simplecrud_djangorest_vue\frontend\simplecrud\

yarn install
yarn run dev

open http://localhost:8080

Run backend:

cd simplecrud_djangorest_vue\

pip install -r backend/requirements.txt
python backend/manage.py makemigrations listofusers
python backend/manage.py migrate
python backend/manage.py runserver

For work with backend side open http://localhost:8000/api/ in your browser

![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/main_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/add_form.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/delete_page.png)
![alt text](https://github.com/skortabeast/simplecrud_djangorest_vue/blob/master/edit.png)
