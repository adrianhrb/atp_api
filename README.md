# Atp tennis API REST 🎾

A dedicated to build a simple api around some tennis information. 
<div style='width:520px'>
    <img src='img/tennis.jpeg'>
</div>
<br>
<br>

> [!NOTE]
> Original files are greater than the ones in the repo. Csv files have been reduced to test the project.

## Starting 🚀

_This section will help you to have a copy of the project in your local computer in case you want to work, change or test something_


### Installation and requirements 🔧

_You can check requirements of the project on the [requirements.txt file](requirements.txt)_

Because the project will be done with Django-Python, we will need a Python Virtual Enviroment to install all dependencies. You can run in a terminal the following commands:

```console
$ python -m venv .venv --prompt mysite
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

If something goes wrong make sure you have Python installed or or else try to launch the command indicating the version of Python:

```console
$ python3.X -m venv .venv --prompt mysite
```

> [!TIP]
> In case of doubts you can see [the documentation](https://docs.python.org/3/library/venv.html)  

Some functionalities will involve the use of sensitive information, so we will use a `.env` file for this purpose. This file must be out of version control so you will need to create one. In the project (mostly in the settings.py file) there will be calls to a config function of the prettyconf library, all these calls are the information that the `.env` file must contain.

On csv files, there are two field that we will not add to database, so we will use redis to link the csv ids with the database ones. We will need this to treat Stats.csv file for add winner and loser to a match as foreign keys.  

To install redis you can run:
```console
$ brew install redis
```
And then, to start running redis:
```console
$ redis-server
```

> [!IMPORTANT]
> This commands may not work to you beacause I´m using Mac. In case of doubt you can [see documentation](https://redis.io)

To streamline some repetitive processes on terminal we are using [Justfile](https://github.com/casey/just), a handy way to run and save commands. For example, in case of make the migrations and migrating changes of an app in django, instead of using `python manage.py makemigrations app & python manage.py migrate` we are using `just mmigrate app`

### Database 💾

The database that will be used in the project is sqlite3

The current design is:

<div style='width:620px'>
    <img src='img/atp-db.svg'>
</div>

### Data files 📑
Files with data:
- [matches.csv](atp_data/matches.csv) -> Info about tennis matches
- [players.csv](atp_data/players.csv) -> Info about tennis players
- [stats.csv](atp_data/stats.csv) -> Info to asign winner and loser to matches


## Contribution 🖇️

Feel free to contribute to the project in any way you want <3. I will be happy to receive help from experienced people to correct mistakes and learn, as I said the project will be a help to continue taking my first steps with Django. 😊

⌨️ with ❤️ by Adrián ✌️
