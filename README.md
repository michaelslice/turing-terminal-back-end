# Turing-Terminal-Back-End

This is a Django project that was initiated with [`django-admin startproject <project-name>`]([https://vitejs.dev/guide/](https://docs.djangoproject.com/en/5.0/intro/tutorial01/))

## Description

Turing-Terminal is a web-based financial terminal developed using React, TypeScript, Django, Python, PostgreSQL, Firebase, Docker, and SocketIO.

## Prerequisites

- Node.js: Ensure node.js is installed on your machine. [Download  here](https://nodejs.org/en/download/prebuilt-installer/current)
- A PostgreSQL account: This project used PostgreSQL for database management. An account can be through Postgres after downloading [here](https://www.postgresql.org/download/)
- Firebase Account: Firebase Authentication is used for authentication in this project. This can be done [here](https://firebase.google.com/)
- Docker Account: This project's frontend and backend are containerized using Docker. Setup [here](https://www.docker.com/products/docker-desktop/)

## Installation & Setup

1.  **Clone the repository**
```
git clone git@github.com:michaelslice/turing-terminal-back-end.git
cd turing-terminal-back-end/src
```
2. **Setup the Environment Variables**
   The environment variables need to be set up next. Follow these steps: <br> 
   - In the directory ```venv/turing-terminal-back-end/```
   - Access the ```.env``` file in your text editor.
   - Append the following lines to the file: <br>
   ```
   ALPHA_VANTAGE_API_KEY=<Your Alpha Vantage API key>
   POSTGRES_KEY=<Your PostgreSQL database password>
   EDGAR_SEC_API_KEY=<Your Edgar SEC API key>
   POLYGON_API_KEY=<Your Polygon API key>
   ```
   - Replace the placeholders with your actual values. Here's how you can obtain each of these:
     - ALPHA_VANTAGE_API_KEY: An API key can be obtained [here](https://www.alphavantage.co/support/#api-key)
     - POSTGRES_KEY: After downloading PostgreSQL, create a database called ```turing-terminal```, and after doing so you will be prompted for a database password. For this to work ensure to replace ```<Your PostgreSQL database password>``` with your database password
     - EDGAR_SEC_API_KEY: An API key can be obtained [here](https://sec-api.io/signup/free)
     - POLYGON_API_KEY: An API key can be obtained [here](https://polygon.io/)
   - After obtaining these values, replace the placeholders in ```.env``` file with the actual values and save the file.
3. **Pull the Docker Image**
```
docker pull ghcr.io/michaelslice/turing-terminal-back-end:latest
```
4. **Build and Run Docker Container**
```
docker build -t turing-terminal-back-end .
docker run -p 8000:8000 turing-terminal-back-end
```
5. **Stop Docker Container**
```
docker ps
docker kill <CONTAINER ID>
```
### Alternatively, manually set up the project

1.  **Clone the Repository**
```
git clone git@github.com:michaelslice/turing-terminal-back-end.git
cd turing-terminal-back-end/src
```
2. **Create a Virtual Environment** <br>
This step should not be skipped to ensure, there are no other package version conflicts with existing packages ready downloaded on your machine. To download and create the virtual environment run the following command 
```
pip install virtualenv
```
```
python -m venv venv
```
4. **Activate the Virtual Environment** <br>
```
venv\Scripts\activate
```
6. **Download Dependencies** <br>
```
pip install -r requirements.txt
```
7. **Setup the Environment Variables**
   The environment variables need to be set up next. Follow these steps: <br> 
   - In the directory ```venv/turing-terminal-back-end/```
   - Access the ```.env``` file in your text editor.
   - Append the following lines to the file: <br>
   ```
   ALPHA_VANTAGE_API_KEY=<Your Alpha Vantage API key>
   POSTGRES_KEY=<Your PostgreSQL database password>
   EDGAR_SEC_API_KEY=<Your Edgar SEC API key>
   POLYGON_API_KEY=<Your Polygon API key>
   ```
   - Replace the placeholders with your actual values. Here's how you can obtain each of these:
     - ALPHA_VANTAGE_API_KEY: An API key can be obtained [here](https://www.alphavantage.co/support/#api-key)
     - POSTGRES_KEY: After downloading PostgreSQL, create a database called ```turing-terminal```, and after doing so you will be prompted for a database password. For this to work ensure to replace ```<Your PostgreSQL database password>``` with your database password
     - EDGAR_SEC_API_KEY: An API key can be obtained [here](https://sec-api.io/signup/free)
     - POLYGON_API_KEY: An API key can be obtained [here](https://polygon.io/)
   - After obtaining these values, replace the placeholders in ```.env``` file with the actual values and save the file.
8. **Start Back-End**
```
python3 manage.py runserver
```
The project should now be running at ```http://localhost:8000```. <br>
9. Start **Websocket Server**
```
python socketio_server.py
```
The websocket server should now be running at ```http://localhost:4000```. <br>

# API Endpoints

## api/v1/focus
Description: This endpoint provides the most recent stock price, daily change, and percentage change for a given ticker. The backend processes the request, interacts with stock price data providers, and returns the requested information. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/focus/ticker/?ticker=AAPL"``` <br> 

## api/v1/chart
Description: This endpoint provides an all-time stock chart for a specified ticker. The backend handles the request, fetches historical price data from stock data providers, and returns the chart data. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/chart/getdailydata/?ticker=IBM"``` <br>

<!-- 
## api/v1/chat
Query Parameters: <br>
HTTP Method: POST, GET <br>
-->
## api/v1/companyevents
Description: This endpoint fetches recent company events based on the ticker symbol. The backend processes the request, queries event data sources, and returns the list of recent events. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/companyevents/get_company_events/?ticker=AVGO"``` <br>

## api/v1/equityscreener
Description:  This endpoint screens companies by market capitalization within the S&P 500. The backend processes the request, applies the specified criteria, and returns a list of companies that meet the criteria. <br>
Query Parameters: ```inequality"``` (string): The user selected inequality. ```market_cap``` (int): The user selected market cap. <br>
HTTP Method: GET <br>

## api/v1/filings
Description: This endpoint retrieves the most recent SEC filings for a specified company ticker. The backend processes the request, queries the appropriate data source, and returns the latest filing information. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/filings/getfilings/?ticker=NVDA"``` <br>

## api/v1/financials
Description: This endpoint provides financial information, such as balance sheets, cash flow statements, and income statements. The backend processes the request based on the document type and ticker, retrieves data from the appropriate source, and returns it. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. ```document_type``` (string): The type of financial document requested (balance sheet, cash flow, or income statement). <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/financials/getcashflow/?ticker=IBM"``` <br>

## api/v1/holders
Description: This endpoint provides information about the largest holders of a company based on its ticker. The backend handles the request, interacts with the data source, and delivers the list of major holders. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/holders/getholders/?ticker=META"``` <br>

## api/v1/bio
Description: This endpoint allows users to submit their bio information, which is then saved to the PostgreSQL database. The backend processes the request, validates input, and stores user data in the database. <br>
HTTP Method: POST <br>

## api/v1/accountmanagement
Description: This endpoint retrieves the most recent account settings for a logged-in user. The backend processes the request, queries the database for user settings, and returns the settings information. <br>
HTTP Method: GET <br>

## api/v1/news
Description: This endpoint fetches the latest news articles for a company identified by its ticker. The backend processes the request, queries news APIs or databases, and returns recent news headlines and summaries. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/news/getnews/?ticker=AMZN"``` <br>

## api/v1/optionchain
Description: This endpoint retrieves option chain data, including calls and puts, for a specified company ticker. The backend processes the request, queries option data sources, and returns the option chain details. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. ```option_type``` (string): Type of options requested (calls or puts). <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/optionchain/getcalls/?ticker=IBM"``` <br>

## api/v1/quotemonitor
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: POST, GET, DELETE, PUT <br>

## api/v1/worldindices
Description: This endpoint retrieves data for global indices. The backend handles the request, queries the data source for world indices, and returns the current data. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/worldindices/getworldindices/``` <br>

## api/v1/description
Description: This endpoint provides a brief description of a company based on its ticker symbol. The backend handles the request, retrieves the description from a data source or API, and returns it in the response. <br>
Query Parameters: ```ticker``` (string): The ticker symbol of the company. <br>
HTTP Method: GET <br>
Request Example: ```curl -X GET "http://127.0.0.1:8000/api/v1/description/getdescription/?ticker=AAPL"``` <br>

# Database Schema

![turing-terminal-database-schema](https://github.com/user-attachments/assets/29a391f9-a2a0-4fbb-8517-3136fba174ea)


## External APIs Used

- [Yahoo Finance API](https://python-yahoofinance.readthedocs.io/en/latest/index.html)
- [Yahoo Fin API](https://theautomatic.net/yahoo_fin-documentation/)
- [SEC Edgar Filings API](https://sec-api.io/docs)
- [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- [Polygon.io API](https://polygon.io/docs/options/getting-started)

## Technologies Used

- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/5.0/ref/)
- [SocketIO](https://python-socketio.readthedocs.io/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)
- [Firebase Authentication](https://firebase.google.com/docs/auth/)
- [Docker](https://www.docker.com/products/docker-desktop/)
