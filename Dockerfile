FROM python:3.7-alpine


COPY confidential.py
COPY main.py
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
WORKDIR /
CMD ["python3", "main.py"]