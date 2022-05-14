FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install "pip<22"
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000  
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
