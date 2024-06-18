FROM python:3.10.14-alpine3.20

# Set Working Directory for Docker Container, Location Where All Subsequent Comamnds Will be Executed
WORKDIR /usr/src/myproject

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy and Install Dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

# Copy Project Code
COPY ./src ./

# Expose Port 8000
EXPOSE 8000

# Run Backend Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
