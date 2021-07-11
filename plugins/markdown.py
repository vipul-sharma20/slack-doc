from string import Template

from plugins.base import ExportSlackThread


MESSAGE_TEMPLATE = """
<@$user> said:

$text

---
"""

class ExportMarkdown(ExportSlackThread):
    """
    Export thread to markdown.

    This should be inherited for plugins which need to be built on top of markdown
    content. (For example: Outline, JIRA, Basecamp etc.)
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def export_thread(self) -> str:
        conversation_history = self.get_thread()
        markdown_content: str = ""

        # TODO: Make this more comprehensible
        for message in conversation_history["messages"]:
            text: str = ""

            for block in message["blocks"]:
                for elements in block["elements"]:
                    for element in elements["elements"]:

                        # handling plain text here
                        if element.get("type") == "text":
                            text += element.get("text", "")

                        # Handling links (hyperlink vs URLs)
                        elif element.get("type") == "link":
                            if element.get("text"):
                                text += f"[{element['text']}]({element['url']})"
                            else:
                                text += element["url"]

                        # Any other text type
                        else:
                            text += element.get("text", "")
            data = {
                "text": text,
                "user": message["user"],
            }
            src = Template(MESSAGE_TEMPLATE)
            content = src.substitute(data)
            markdown_content += content

        return markdown_content
