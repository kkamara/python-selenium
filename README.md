# Selenium Py

Automate web browsing with Chrome. 

## Requirements

- [Pipenv](https://pypi.org/project/pipenv/) (*optional*)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://www.python.org/downloads/)

## Build Selenium Container

```
docker-compose up --build -d
```
You will get a selenium grid that you can view at `http://localhost:4444/grid/console`.

## Usage
```
pipenv install
pipenv run python src/main.py
```
A screenshot named `test.png` will be saved to `repo-install-location/storage`.

This is a base from which you can continue testing with Selenium.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
