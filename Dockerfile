FROM python:3.7
ADD . /monitor-service
WORKDIR /monitor-service
RUN pip install pipenv && \
    pip install gunicorn && \
    pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--chdir", "src", "main"]