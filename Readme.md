# Using this template

## Installation

```shell
pipenv install
cd webiste/frontend
yarn install
```

## sqlite

To dump data from current DB

```shell
python manage.py dumpdata > db.json
```

if you want indented, then use

```shell
python manage.py dumpdata --indent 2 > db.json
```

To load data

```shell
python manage.py loaddata db.json
```

sometimes it may cause issues if the db is not fresh or some authentication permissions has changed, in that case first dump data using

```shell
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

and then load data.
