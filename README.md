# flask-heroku-helloworld
A "hello world" starter project for flask/heroku in python

Run locally with:
```
python app.py
```
Once you're ready to run on heroku your git repo needs to be associated with an app in Heroku

Resouces:
- [The python toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

To create/deploy on heroku: 
```
heroku create <your app name>
```
The app will then be created (if you don't give it a name one will be assigned)

Next git needs to know the new remote (you will have two remotes, github and heroku)

```
heroku git:remote -a <your app name>
```

To not expose any keys in a public repo you use the the [heroku config](https://devcenter.heroku.com/articles/config-vars)

```
heroku config:set my_env_var="secret api key"
```

in the python app you get the config var using:

```
os.environ['my_env_var']
```
Once started the app exposes two endpoints, one example of a template based [jinja2](http://jinja.pocoo.org/docs/dev/) html 
page, the other a json REST api.

REST API: http://localhost:5000/api/hello
Web Page: http://localhost:5000/ (http://localhost:5000/index.html)

Once deployed the url will become: http://<your app name>.herokuapp.com/api/hello

```
git push heroku master
```

or if you're working on a remote branch

```
git push heroku <branch>:master
```

![screenshot](https://cloud.githubusercontent.com/assets/5496117/18763190/100f359a-80c1-11e6-9635-fd39f9ec68dc.png)

