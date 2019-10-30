FROM python:3.6.8

#prevent writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#prevent buffering stdout and stderr
ENV PYTHONUNBUFFERED 1




# Set work directory
RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./

# Upgrade pip
RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt



# Copy project
COPY . .



