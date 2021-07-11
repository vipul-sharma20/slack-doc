# slack-doc

Slack app to export conversation threads to documents and more.

## Deployment

```
docker-compose up
```

Make sure to update the environment variables.

Pre-built image at: https://hub.docker.com/repository/docker/vipul20/slack-doc

## Integration

- Create an app on Slack, for example: `slack-doc`.
- Create Slack bot token (check "OAuth & Permissions" in your app page) and add
  it as environment variable in [docker-compose.yml][docker-compose].
    - Add following scopes: `channels:history`, `channels:join`,
      `channels:read`, `chat:write`, `commands`, `users.profile:read`,
      `users:read`.
- Deploy the application with the tokens.
- Add "Request URL" under "Interactivity & Shortcuts" as `http://<host>:<port>/slack/shortcut-trigger/`.
- Create message "Shortcuts" under "Interactivity & Shortcuts"
    - Create a new shortcut for your plugin with callback ID as the one
      provided in the plugin [factory][plugin_factory].
- Add the Slack app in your channel (Example: `/invite @slack-doc`).
- Check message options on any thread and you should see the message shortcuts
  you would've added in the list.

## Exporters

This application has exporter plugins to export threads to different mediums.
Currently supported exporters:

- [Outline Wiki][outline_plugin]
- [Gist][gist_plugin]
- [Markdown][markdown_plugin] (generic markdown, currently being used as a base
  for all markdown based exporters)
- ...

Check [plugins doc][plugins_doc] on how to add your own custom exporter.


[plugin_base]: plugins/base.py
[plugin_map]: slack_doc/factory.py
[plugin_factory]: slack_doc/factory.py
[docker-compose]: docker-compose.yml
[outline_plugin]: plugins/outline.py
[gist_plugin]: plugins/gist.py
[markdown_plugin]: plugins/markdown.py
[plugins_doc]: plugins/README.md
