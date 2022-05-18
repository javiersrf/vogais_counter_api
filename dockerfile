FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY . .
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
RUN ln -fs /usr/share/zoneinfo/America/Belem /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]