FROM python:3
COPY . /passwd
WORKDIR /passwd
RUN pip install password
RUN pip install pybase64
CMD ["python","./passwd.py"]