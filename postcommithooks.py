#!/usr/bin/python3

import sys, os
import jiraconnector
from subprocess import check_output
import logging as l
l.basicConfig(format='%(levelname)s:%(message)s',level=l.DEBUG)

class PostCommitHook():

  def __init__(self):
    self.connector = jiraconnector.JiraConnector()
    self.branch_name = check_output(['git','symbolic-ref','--short','HEAD'])
    self.branch_name = self.branch_name.strip().decode('utf-8')
    self.issue = self.connector.get_issue(self.branch_name)
    try:
      self.make_diff()
    except FileNotFoundError as e:
      l.info("Phabricator arc is not installed! Review issue has not beed added to differential.")
    else:
      self.make_comment()
      self.change_status()

  def make_diff(self):
    pass
    #arc_result = check_output(['arc','diff'])
    #l.info(arc_result)

  def make_comment(self):
    self.connector.add_comment(self.issue, 'New commit and new review in differential!')
    l.info("Comment added to jira (issue: %s)"%self.branch_name)

  def change_status(self):
    self.connector.set_review_status(self.issue)
