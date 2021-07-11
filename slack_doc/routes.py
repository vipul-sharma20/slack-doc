import json
import traceback

from flask import current_app as app
from flask import request, make_response

from slack_doc.factory import PLUGINS


@app.route("/slack/shortcut-trigger/", methods=["POST"])
def shortcut_trigger():
    data = request.form

    payload = data.get("payload")
    try:
        payload = json.loads(payload)
        callback_id = payload["callback_id"]

        export_plugin = PLUGINS[callback_id](payload)
        export_plugin.export_thread()

        return make_response("", 200)

    except Exception:
        traceback.print_exc()

        return make_response("", 200)

