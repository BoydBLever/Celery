#See https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#application
from celery import Celery

#redis://localhost:6379/0 is the default port with database 0
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

# pip install celery
# pip install redis -> installs Python client library for redis
# brew install redis -> installs the actual Redis server on your machine

# Left terminal
# redis-server -> start the Redis server

# Right terminal
# redis-cli -> acccess Redis CLI in the terminal
#for testing:
# 127.0.0.1:6379> ping -> test the connection by running the 'ping' command. You should get a 'PONG' response.
# exit
# -> Start the Celery worker
# celery -A tasks worker --loglevel=info

# Run the Task in a New Terminal Window or Tab
# open a new terminal window or tab, not just a split pane.
# python3 -> enter Python interactive shell (>>> appears on the left of each line in the Python environment. If celery is not installed, use exit() to leave the python environment, and run pip3 install celery).

# Import your 'add' task and run it:
# >>> from tasks import add
# >>> result = add.delay(4,4)

# Get the Task Result
# >>> print(result.get(timeout=10))
