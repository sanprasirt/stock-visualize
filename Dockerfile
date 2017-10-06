FROM python:2
MAINTAINER sanprasirt@pccth.com
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_8.x |bash -
RUN apt-get install -y nodejs
COPY . .
RUN npm install -g bower
RUN bower --allow-root install
CMD [ "python", "./app.py" ]
EXPOSE 5000