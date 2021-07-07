FROM python:3.9

WORKDIR /home/slack-doc/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /home/slack-doc/

ENV SLACK_API_TOKEN=xoxb-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENV OUTLINE_HOST=host
ENV OUTLINE_TOKEN=token
ENV OUTLINE_COLLECTION_ID=token

ENV PYTHONPATH=/home/slack-doc/slack_doc
ENV FLASK_APP=slack_doc/__init__.py

CMD ["flask", "run", "-p", "8000"]
# CMD ["uwsgi", "--http-socket", ":5000", "--enable-threads", "--threads", "4", "--module", "slack-doc:create_app()", "--workers", "2", "--buffer-size", "32768"]
