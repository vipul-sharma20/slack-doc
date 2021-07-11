import os

import github

from plugins.markdown import ExportMarkdown


class ExportGist(ExportMarkdown):
    """
    Export thread to Github Gist plugin.

    This inherits the generic markdown export plugin
    """

    def __init__(self, *args, **kwargs) -> None:
        self.gh = github.Github(os.getenv("GITHUB_TOKEN"))

        super().__init__(*args, **kwargs)

    def export_thread(self):
        markdown_content = super().export_thread()

        gh_auth_user = self.gh.get_user()
        gist = gh_auth_user.create_gist(public=False,
                                        files={"test.md": github.InputFileContent(markdown_content)})
        self.send_message(gist.html_url)
