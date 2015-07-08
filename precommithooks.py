#!/usr/bin/python3

import sys, os
import jiraconnector
from subprocess import check_output

class PreCommitHook():

  def __init__(self,message_file):
    self.message_file = message_file
    self.update_message()

  def update_message(self):
    branch_name = check_output(['git','symbolic-ref','--short','HEAD'])

    connector = jiraconnector.JiraConnector()
    issue = connector.get_issue(branch_name)

    with open(self.message_file, 'w') as f:
      f.write("Jira issue: %s"%(issue.fields.summary))
