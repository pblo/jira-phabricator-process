This is set of integrates jira-phabricator-and-git work flow.

Git hooks:

1) prepare-commit-msg
  - Prepares commit message with information of jira api
  - Feature branch name is an identifier.

2) post-commit
  - Makes review ticket for phabricator differential tool
  - Posts appriopriate comment to jira issue comment board.
  - Changes jira issue status to "Waiting for review"

Assumptions:
  - Working with feature branches git workflow (but feature branch means jira issue branch).
  - Phabricator arc tool is installed
  - All files should be placed in .git/hooks directory

More info about used git workflow:
http://nvie.com/posts/a-successful-git-branching-model/
https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
