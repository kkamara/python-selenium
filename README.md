# Selenium Py

Automate Firefox web browsing with [Selenium](https://www.selenium.dev/) and Python 3 and Docker. 

## Requirements

- [Pipenv](https://pypi.org/project/pipenv/) (*optional*)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://www.python.org/downloads/)

Ensure Geckodriver is accessible from the global path in your operating system.

On debian systems we can do that by adding the following statement to your `$HOME/.bashrc`:
```
export PATH="/usr/bin/geckodriver:$PATH"
```

[Setting path for Windows users](https://www.computerhope.com/issues/ch000549.htm)


## Build Selenium Container

```
docker-compose up --build -d
```
You will get a container named `python-docker-skeleton_selenium_1` that you can view with `docker ps -a`.

## Usage
```
pipenv install
pipenv run python src/main.py
```
On successful run you will see a firefox browser window open for `http://seleniumhq.org/`. A screenshot named `test.png` will be saved to `repo-install-location/storage`.

This is a base from which you can continue testing with Selenium.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://www.gnu.org/licenses/quick-guide-gplv3.html)
