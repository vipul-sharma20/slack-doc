import json

import requests
from flask import current_app as app
from flask import request, make_response

import slack_doc.constants as constants
from slack_doc.factory import PLUGINS


@app.route("/slack/shortcut-trigger/", methods=["POST"])
def shortcut_trigger():
    payload = json.loads(request.form["payload"])
    callback_id = payload["callback_id"]
    response_url = payload["response_url"]

    try:
        requests.post(response_url,
                      json={"text": constants.EPHEMERAL_RESPONSE_ON_EXPORT,
                            "response_type": constants.RESPONSE_TYPE_EPHEMERAL})

        export_plugin = PLUGINS[callback_id](payload)
        export_plugin.export_thread()

        return make_response("", 200)

    except Exception as e:
        requests.post(response_url,
                      json={"text": f"Cannot create doc. Error: \n\n{e}",
                            "response_type": constants.RESPONSE_TYPE_EPHEMERAL})

        return make_response("", 200)
