FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code
WORKDIR /code
CMD python -u crawler_rss.py