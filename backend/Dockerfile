FROM python:3.12.2
WORKDIR /code
RUN pip install black
RUN pip install pip-tools
COPY . .
RUN pip install -r requirements.txt
CMD ["./start-dev.sh"]