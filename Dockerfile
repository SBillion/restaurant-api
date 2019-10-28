FROM python:3.6.8

#prevent writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#prevent buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copy project
COPY . /code/

# Set work directory
WORKDIR /code



# Upgrade pip
RUN pip install pip --upgrade

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Install porject dependencies
RUN /root/.poetry/bin/poetry self:update --preview
RUN /root/.poetry/bin/poetry install



