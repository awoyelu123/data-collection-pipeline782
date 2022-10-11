
FROM python:3.8-slim-buster

ADD water_scraper.py .

RUN pip install 

CMD ["python", "./water_scraper.py"]