<img src="https://github.com/kkamara/useful/raw/main/selenium-py.png" alt="selenium-py.png" />

# python-selenium

Automate web browsing with Chrome.

## Setup

```bash
cp .env.example .env
pip3 install virtualenv && \
  virtualenv env && \
  source env/bin/activate
alias compose='docker-compose -f local.yml'
compose build
compose up
```

The app runs at `http://localhost:8000`.

## Usage

Update the command at [./management/commands/crawlamazon.py](https://raw.githubusercontent.com/kkamara/selenium-py/main/seleniumpy/management/commands/crawlamazon.py)

```bash
compose up --build -d && python3 manage.py crawlamazon
```

## iPython Django Shell

```bash
python3 manage.py shell -i ipython
```

## API

```bash
python manage.py show_urls
```

View the api collection [here](https://documenter.getpostman.com/view/17125932/UVyxQYrt).

## Admin

Admin creds are set in [./compose/local/django/start](https://raw.githubusercontent.com/kkamara/django-app/develop/compose/local/django/start)

```bash
export DJANGO_SUPERUSER_PASSWORD=secret

python manage.py createsuperuser \
  --username admin_user \
  --email admin@django-app.com \
  --no-input \
  --first_name Admin \
  --last_name User
```

## Mail Server

![docker-mailhog.png](https://raw.githubusercontent.com/kkamara/useful/main/docker-mailhog.png)

Mail environment credentials are at [.env](https://raw.githubusercontent.com/kkamara/django-app/develop/.env.example).

The [mailhog](https://github.com/mailhog/MailHog) docker image runs at `http://localhost:8025`.

## Misc

[See python amazon scraper.](https://github.com/kkamara/python-amazon-scraper)

[See python react boilerplate.](https://github.com/kkamara/django-react-boilerplate)

[See amazon scraper (proven in a production environment).](https://github.com/kkamara/amazon-scraper)

[See php scraper.](https://github.com/kkamara/php-scraper)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
