import os
from string import Template

import requests

from .markdown import ExportMarkdown


DOCUMENT_TEMPLATE = """
## About

This doc has been created from a Slack thread: $url

---

$text
"""


class ExportOutline(ExportMarkdown):
    """
    Export thread to outline document plugin.

    This inherits the generic markdown export plugin
    """

    def __init__(self, *args, **kwargs) -> None:
        self.outline_host = os.getenv("OUTLINE_HOST")
        self.outline_token = os.getenv("OUTLINE_TOKEN")
        self.collection_id = os.getenv("OUTLINE_COLLECTION_ID")

        super().__init__(*args, **kwargs)

    def export_thread(self):
        markdown_content = super().export_thread()

        template = Template(DOCUMENT_TEMPLATE)
        markdown_content = template.substitute({"text": markdown_content, "url": None})

        self._create_doc("draft", markdown_content)

    def _create_doc(self, title: str, text: str):
        url = self.outline_host + "/api/documents.create"

        headers = {"Authorization": f"Bearer {self.outline_token}"}
        payload = {
            "title": title,
            "text": text,
            "collectionId": self.collection_id,
            "publish": False,
        }

        requests.post(url, json=payload, headers=headers)
