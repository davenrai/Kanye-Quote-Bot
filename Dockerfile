FROM python:3.7-alpine


COPY bot/Confidential.py /bot/
COPY bot/main.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "main.py"]