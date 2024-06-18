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

## Technologies Used

- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/5.0/ref/)
