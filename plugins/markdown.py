from string import Template

import plugins.utils as utils
from plugins.base import ExportSlackThread


MESSAGE_TEMPLATE = """
@$user said:

$text

---
"""


class ExportMarkdown(ExportSlackThread):
    """
    Export thread to markdown.

    This should be inherited for plugins which need to be built on top of
    markdown content. (For example: Outline, JIRA, Basecamp etc.)
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def export_thread(self) -> str:
        conversation_history = self.get_thread()
        markdown_content: str = ""

        for message in conversation_history["messages"]:
            data = {
                "text": self._prepare_text(message["text"]),
                "user": utils.get_user_names_from_id(message["user"], self.client),
            }
            src = Template(MESSAGE_TEMPLATE)
            content = src.substitute(data)
            markdown_content += content

        return markdown_content

    def _prepare_text(self, text: str) -> str:
        # fix code snippets
        text = text.replace("```", "```\n")

        return text
