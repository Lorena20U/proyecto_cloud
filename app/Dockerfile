FROM python:3.8

WORKDIR /app

COPY requerimientos.txt requerimientos.txt
RUN pip install -r requerimientos.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
