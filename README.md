# Turing-Terminal-Back-End

This is a Django project that was initiated with [`django-admin startproject <project-name>`]([https://vitejs.dev/guide/](https://docs.djangoproject.com/en/5.0/intro/tutorial01/))

## Description

Turing-Terminal is a web-based financial terminal developed using React, and Django.

## Prerequisites

- Node.js: Ensure node.js is downloaded

## Installation & Setup

1.  **Clone the repository**
   
```
git clone git@github.com:michaelslice/turing-terminal-back-end.git
cd turing-terminal-back-end/src
```

2. **Start Front-End**
```
python3 manage.py runserver
```

3. **Build Front-End**
```
npm run build
```

3. **Test on Docker**

```
docker build -t test .
docker run -p 8000:8000 test
```
4. **Stop Docker Container**
```
docker ps
docker kill <CONTAINER ID>
```

## API Endpoints

- `api/v1/focus/`
- `api/v1/chart/`
- `api/v1/chat/`
- `api/v1/companyevents/`
- `api/v1/equityscreener/`
- `api/v1/filings/`
- `api/v1/financials/`
- `api/v1/holders/`
- `api/v1/ipo/`
- `api/v1/news/`
- `api/v1/optionchain/`
- `api/v1/quotemonitor/`
- `api/v1/worldindices/`
- `api/v1/description/`

## Documentation

- [Yahoo Finance API](https://python-yahoofinance.readthedocs.io/en/latest/index.html)
- [Yahoo Fin API](https://theautomatic.net/yahoo_fin-documentation/)
- [SEC Edgar Filings API](https://sec-api.io/docs)
- [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- [Polygon.io API](https://polygon.io/docs/options/getting-started)

## Technologies Used

- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/5.0/ref/)
