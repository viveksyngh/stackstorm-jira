from lib.base import BaseJiraAction

__all__ = ["JiraIssueAddWatcherAction"]


class JiraIssueAddWatcherAction(BaseJiraAction):
    def run(self, issue_key, username):
        return self._client.add_watcher(issue_key, username)
