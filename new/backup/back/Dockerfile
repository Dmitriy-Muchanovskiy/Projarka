FROM python:3
WORKDIR /usr/src/app
COPY back/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY back/* ./
CMD [ "python3", "./api.py" ]
EXPOSE 8888

