FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
COPY . .
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]