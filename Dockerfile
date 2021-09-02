FROM buildpack-deps:buster

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH


# set work directory
WORKDIR /usr/src/app


# install psycopg2 dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python-pip \
        python3-setuptools \
	&& rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

# Expose port where the Django app runs
EXPOSE 5000
# start server
CMD flask run
