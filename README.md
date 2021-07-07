# slack-doc

Slack app to export conversation threads to documents.

This app works on plugin based design

🚧WIP🚧

TODO: Fix documentation

## Development

- Implement the [plugin][plugin_base] and keep them at `slack_doc/plugins`.
- Add your plugin in [`PLUGINS`][plugin_map]

### Slack configuration

- Create app and add `HOST:PORT/slack/shortcut-trigger/` in the interactivity
  URL. Any interaction event on Slack will be sent to this hook.
- Create a new shortcut for your plugin with `callback_id` as the one you used
  to register your plugin.

## Plugins supported

- [Outline][outline_home]
- Markdown (generic markdown, currently being used as a base for all markdown based plugins)
- ...

[plugin_base]: slack_doc/plugins/base.py
[plugin_map]: slack_doc/routes.py
[outline_home]: https://www.getoutline.com/
