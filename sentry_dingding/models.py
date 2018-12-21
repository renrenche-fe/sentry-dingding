import requests
from django import forms
from sentry.plugins.bases.notify import NotifyPlugin
import sentry_dingding

class DingDingOptionsForm(forms.Form):
    endpoint = forms.CharField(help_text="DingDing Endpoint", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'dingding endpoint'}))

class DingDingMessage(NotifyPlugin):
    author = 'Xierenhong'
    author_url = 'https://github.com/renrenche-fe/sentry-dingding'
    version = sentry_dingding.VERSION
    description = "sentry dingding"
    resource_links = [
        ('Bug Tracker', 'https://github.com/renrenche-fe/sentry-dingding/issues'),
        ('Source', 'https://github.com/renrenche-fe/sentry-dingding'),
    ]
    slug = 'dingding'
    title = 'DingDing'
    conf_title = title
    conf_key = 'dingding'
    project_conf_form = DingDingOptionsForm

    def is_configured(self, project):
        return bool(self.get_option('endpoint', project))

    def notify_users(self, group, event, fail_silently=False):
        project = event.project
        link = group.get_absolute_url()
        endpoint = self.get_option('endpoint', project)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "错误报警",
                "text": '''### 项目{project_name}发生错误，请尽快查看处理!   \n
> [点我直接查看BUG]({link})
                '''.format(
                    project_name=project,
                    link=link,
                ),
            },
        }
        self.send_payload(
            endpoint=endpoint,
            data=data
        )

    def send_payload(self, endpoint, data):
        requests.post(
            endpoint,
            json=data,
        )