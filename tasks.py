#See https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#application
from celery import Celery

#redis://localhost:6379/0 is the default port
app = Celery('tasks', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y

# pip install celery
# pip install redis -> installs Python client library for redis
# brew install redis -> installs the actual Redis server on your machine
# redis-server -> start the Redis server
# redis-cli -> acccess Redis CLI in the terminal
# 127.0.0.1:6379> ping -> test the connection by running the 'ping' command. You should get a 'PONG' response.
