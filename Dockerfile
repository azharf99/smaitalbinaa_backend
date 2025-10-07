# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Add the Python binaries directory to the PATH
ENV PATH="/usr/local/bin:${PATH}"

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for mysqlclient and other packages
# Combining these into one layer improves build time and reduces image size.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       default-libmysqlclient-dev \
       gcc \
       pkg-config \
    && apt-get clean \
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# We copy the requirements file first to leverage Docker's cache
COPY requirements.txt .
# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Collect static files
# Set dummy variables required only for the build process (e.g., collectstatic).
# The real values will be injected at runtime from the .env file.
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# Gunicorn is a production-ready WSGI server
CMD ["gunicorn", "smaitalbinaa_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
# Copy the rest of the application's code into the container at /app
COPY . /app/