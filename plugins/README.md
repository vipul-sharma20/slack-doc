## About

This directory has all the plugins to export Slack threads into different
mediums.

This application has exporter plugins to export threads to different mediums.
Currently supported exporters:

- [Outline Wiki][outline_plugin]
- [Gist][gist_plugin]
- [Markdown][markdown_plugin] (generic markdown, currently being used as a base
  for all markdown based exporters)
- ...

## Writing exporter plugins

Implement the `ExportThread` base class in [base.py][base] in a new plugin and
include them in [slack_doc/factory.py][factory]

Check one of the the pre-existing exporter plugins (for example:
[markdown.py][markdown_plugin])

To update/add the new exporter on Slack:
- Create new message "Shortcuts" under "Interactivity & Shortcuts"
- Create a new shortcut for your plugin with callback ID as the one
  provided in the plugin [factory][plugin_factory].


[gist_plugin]: gist.py
[outline_plugin]: outline.py
[markdown_plugin]: markdown.py
[factory]: ../slack_doc/factory.py
[base]: base.py
