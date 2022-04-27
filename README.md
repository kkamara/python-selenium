# Selenium Py

Automate web browsing with Chrome. 

## Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://www.python.org/downloads/)

## Setup

```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate
(env) pip3 install -r requirements.txt
```

## Build Selenium Container

```
docker-compose up --build -d
```
You will get a selenium grid that you can view at `http://localhost:4444/grid/console`.

## Usage
```
python3 python src/main.py
```

This is a base from which you can continue testing with Selenium.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
