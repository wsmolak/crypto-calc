FROM python:alpine
COPY . /coin-calc-app
WORKDIR /coin-calc-app
RUN pip install -r requirements.txt
CMD python coinmarketcap_test.py config.json