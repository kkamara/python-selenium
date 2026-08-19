<img src="https://raw.githubusercontent.com/kkamara/useful/main/python-selenium.gif" alt="python-selenium.gif" />

# python-selenium

💻 (30-Mar-2021) See your Python code do web browsing on your screen with GUI.

* [Important note](#important-note)

* [Requirements](#requirements)

* [Installation](#installation)

    * [Configure This Project](#configure-this-project)

    * [Run Your Selenium Server Jar File](#run-your-selenium-server-jar-file)

* [Usage](#usage)

* [Using Docker?](#using-docker)

    * [Existing Admin User When Using Docker](#existing-admin-user-when-using-docker)

    * [Using Docker's Mail Server](#using-dockers-mail-server)

* [iPython Django Shell](#ipython-django-shell)

* [API](#api)

* [Cache View Templates](#cache-view-templates)

* [Contributing](#contributing)

* [License](#license)

## Important note:

Before you try to scrape any website, go through its robots.txt file. You can access it via `domainname/robots.txt`. There, you will see a list of pages allowed and disallowed for scraping. You should not violate any terms of service of any website you scrape.

## Requirements

* [Tested using Python 3.13](https://www.python.org)
* [Java](https://www.oracle.com/uk/java/technologies/downloads)
* [Chromedriver](https://developer.chrome.com/docs/chromedriver) (optional)
* [Selenium Server JAR file](https://www.selenium.dev/documentation/grid/getting_started)

## Installation

#### Configure This Project

```bash
cp .env.example .env
python -m venv env && \
  source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
```

#### Run Your Selenium Server JAR File

Locate where you downloaded your Selenium Server JAR file in the [requirements](#requirements) step and run the following.

```bash
java -jar selenium-server-[version].jar standalone --override-max-sessions true --max-sessions 10
```

[CLI options in the Selenium Grid](https://www.selenium.dev/documentation/grid/configuration/cli_options/).

## Usage

Update the command at [crawl.py](./seleniumpy/management/commands/crawl.py) to perform your instructions in web scraping.

```bash
python manage.py crawl
```

[XPath element selector cheat sheet](https://devhints.io/xpath).

## Using Docker?

```bash
alias compose='docker-compose -f local.yml'
compose build
compose up
# Automated runs with Docker:
# compose up --build -d && python manage.py crawl
```

#### Existing Admin User When Using Docker

The admin user details are set in [./compose/local/django/start](./compose/local/django/start).

```bash
export DJANGO_SUPERUSER_PASSWORD="${DJANGO_SUPERUSER_PASSWORD:-secret}"

python manage.py createsuperuser \
  --no-input \
  --username admin_user \
  --email admin@django-app.com
```

#### Using Docker's Mail Server

<img src="https://raw.githubusercontent.com/kkamara/useful/main/docker-mailhog.png" alt="docker-mailhog.png" width="300px"/>

Mail environment credentials are at [.env](./.env.example).

The [Mailhog](https://github.com/mailhog/MailHog) Docker mail client runs at `http://localhost:8025`. This is running in the above image that is receiving emails from your Django app.

## iPython Django Shell

```bash
py manage.py shell -i ipython
```

## API

```bash
py manage.py show_urls
```

## Cache react app & view templates

```bash
py manage.py collectstatic
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
