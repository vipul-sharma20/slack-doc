from plugins.base import ExportSlackThread
from plugins.markdown import ExportMarkdown
from plugins.outline import ExportOutline


PLUGINS = {
    # "export_thread": ExportSlackThread,
    "export_thread": ExportMarkdown
    # "export_thread": ExportOutline,
}
