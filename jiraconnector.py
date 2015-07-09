import jira
import configparser
import logging as l
l.basicConfig(format='%(levelname)s:%(message)s',level=l.DEBUG)

class JiraConnector():

  def __init__(self):

    self.config = configparser.ConfigParser()
    self.config.read('jira_config.ini')

    l.debug("Connecting to jira")
    self.jira = jira.JIRA(self.config['JiraAuth']['Url'], basic_auth=(self.config['JiraAuth']['GitUserName'],self.config['JiraAuth']['GitUserPassword']))

  def _log(self,msg):
    print(msg)

  def get_issue(self,name):
    issue = self.jira.issue(name)
    l.debug("Issue fetched")
    l.debug(issue.fields.summary)
    l.debug(issue.fields.status)
    return issue

  def add_comment(self,issue,msg):
    self.jira.add_comment(issue, msg)
    l.debug("NEW COMMENT: %s"%(msg))

  def set_review_status(self,issue):
    self.jira.transition_issue(issue,741)

if __name__ == "__main__":
  jira_connector = JiraConnector()
  issue = jira_connector.get_issue('TP-3')
