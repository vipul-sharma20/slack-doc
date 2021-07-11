FROM python:3.9

WORKDIR /home/slack-doc/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /home/slack-doc/

# 3rd party tokens etc.
ENV SLACK_API_TOKEN=xoxb-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENV OUTLINE_HOST=host
ENV OUTLINE_TOKEN=token
ENV OUTLINE_COLLECTION_ID=token
ENV GITHUB_TOKEN=token

# Cache
ENV REDIS_HOST=host.docker.internal
ENV REDIS_HOST=localhost
ENV REDIS_PORT=6379

# Application
ENV FLASK_APP=slack_doc

# CMD ["flask", "run", "-p", "8000"]
CMD ["uwsgi", "--http-socket", ":8000", "--enable-threads", "--threads", "4", "--module", "slack-doc:create_app()", "--workers", "2", "--buffer-size", "32768"]
