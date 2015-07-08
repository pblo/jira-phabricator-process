This is set of tools for jira-phabricator-and-git workflow automatization.

Git hooks:

1) prepare-commit-msg
  - Updates commit message with information from jira API
  - Feature branch name is an identifier

2) post-commit
  - Makes commit diff
  - Makes review ticket for phabricator differential tool
  - Posts appriopriate comment to jira issue comment board
  - Changes jira issue status to "Waiting for review"

Assumptions:
  - Git feature branch workflow is used (but feature means jira issue here)
  - Phabricator arc tool is installed and configured (api token installed)
  - All files should be placed in .git/hooks directory

More info about used git workflow:

http://nvie.com/posts/a-successful-git-branching-model/
https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
