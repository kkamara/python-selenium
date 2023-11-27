<img src="https://github.com/kkamara/useful/raw/main/selenium-py.png" alt="selenium-py.png" />

# python-selenium

(2021) See your Python code do web browsing on your screen with GUI.

* [Important note:](#note)

* [Installation](#installation)

* [Usage](#usage)

* [Using Docker](#using-docker)

* [iPython Django Shell](#ipython-django-shell)

* [API](#api)

* [Admin](#admin)

* [Cache react app & view templates](#cache-templates)

* [Mail Server](#mail-server)

* [Misc](#misc)

* [Contributing](#contributing)

* [License](#license)

## Important note: <a name="note"></a>

Before you try to scrape any website, go through its robots.txt file. You can access it via `domainname/robots.txt`. There, you will see a list of pages allowed and disallowed for scraping. You should not violate any terms of service of any website you scrape.

With selenium we're limited to 10 max ongoing sessions ([reference](https://forum.katalon.com/t/what-is-the-relationship-between-the-setting-max-concurrent-instances-and-selenium-grid-settings-maxinstances-and-maxsessions/48082/2)).

I've successfully tested 1000 site crawls in a single process (3 hours, 44 minutes, and 47 seconds).

(4 hours x 1000 sites) * 2 = 2000 sites x 8 hours

2000 sites * 10 parallel sessions = 20, 000 sites

We're able to cover 20, 000 sites / night / machine. 

## Installation

```bash
cp .env.example .env
pip install virtualenv && \
  virtualenv env && \
  source env/bin/activate
python3 manage.py migrate
```

```bash
# chromedriver_mac64
# chromedriver_win32
# See https://chromedriver.storage.googleapis.com
# for drivers list.
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
chromedriver --version
```

## Usage

[XPath cheat sheet](https://devhints.io/xpath).

Update the command at [crawl.py](https://github.com/kkamara/python-selenium/blob/main/seleniumpy/management/commands/crawl.py)

```bash
alias py="python3"
py manage.py crawl
```

If you still need help installing and running the app check out the readme at https://github.com/kkamara/python-react-boilerplate which is the base system for this python-selenium app.

## Using Docker?

```bash
alias compose='docker-compose -f local.yml'
compose build
compose up
# Automated runs with Docker:
# compose up --build -d && python3 manage.py crawl
```

## iPython Django Shell

```bash
py manage.py shell -i ipython
```

## API

```bash
py manage.py show_urls
```

View the api collection [here](https://documenter.getpostman.com/view/17125932/UVyxQYrt).

## Admin

Admin creds are set in [./compose/local/django/start](https://raw.githubusercontent.com/kkamara/python-selenium/main/compose/local/django/start)

```bash
export DJANGO_SUPERUSER_PASSWORD=secret

py manage.py createsuperuser \
  --username admin_user \
  --email admin@django-app.com \
  --no-input \
  --first_name Admin \
  --last_name User
```

## Cache react app & view templates <a name="cache-templates"></a>

```bash
py manage.py collectstatic
```

## Mail Server

![docker-mailhog.png](https://raw.githubusercontent.com/kkamara/useful/main/docker-mailhog.png)

Mail environment credentials are at [.env](https://raw.githubusercontent.com/kkamara/python-selenium/main/.env.example).

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
