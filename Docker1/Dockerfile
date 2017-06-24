FROM python
RUN pip install requests pandas boto3 botocore boto arrow jupyter notebook matplotlib scipy
COPY ./Assignment1/config.json /
COPY ./Assignment1/dataIngestion.py / 
COPY ./Assignment1/run.sh /
COPY ./Assignment1/logger.log /
COPY ./Assignment1/TX_170617_WBAN_13910.csv /
COPY ./Assignment1/rawDataEDA.ipynb /
ENTRYPOINT  ["bash", "run.sh"]

