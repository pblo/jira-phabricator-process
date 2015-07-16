#!/usr/bin/python3

import sys, os
import jira
import jiraconnector
from subprocess import check_output
import pexpect, struct, fcntl, termios, signal
import logging as l
l.basicConfig(format='%(levelname)s:%(message)s',level=l.DEBUG)

def sigwinch_passthrough (sig, data):
  s = struct.pack("HHHH", 0, 0, 0, 0)
  a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ , s))
  global p
  p.setwinsize(a[0],a[1])

class PostCommitHook():

  def __init__(self):
    self.connector = jiraconnector.JiraConnector()
    self.branch_name = check_output(['git','symbolic-ref','--short','HEAD'])
    self.branch_name = self.branch_name.strip().decode('utf-8')
    self.issue = self.connector.get_issue(self.branch_name)
    self.make_diff()
    #try:
    #  self.make_diff()
    #except pexpect.ExceptionPexpect as e:
    #  l.info("Phabricator arc is not installed! Review issue has not beed added to differential.")
    #else:
    #  self.make_comment()
    #  self.change_status()

  def make_diff(self):
    #from subprocess import Popen
    #po = Popen("arc diff --trace", shell=True, cwd='/home/pblo/phabricator/test_project/phabricator-test/')
    #po.communicate()

    print("in script:%s"%sys.stdin.fileno())

    pexpect.STDIN_FILENO = sys.stdin.fileno()
    pexpect.STDOUT_FILENO = sys.stdout.fileno()
    child = pexpect.spawn('arc diff',cwd='/home/pblo/phabricator/test_project/phabricator-test/')
    if sys.stdin.isatty(): print("in YES")
    if sys.stdout.isatty(): print("out YES")
    #child.expect(".Ignore these untracked files and continue.*")
    #child.sendline('y')
    #child.expect(".Do you want to use this message?.*")
    #child.sendline('y')
    child.interact()

  def make_comment(self):

    commit_message = self._get_last_commit_message()

    self.connector.add_comment(self.issue, "New commit and new review in differential!\n\n%s"%(commit_message))
    l.info("Comment added to jira (issue: %s)"%self.branch_name)

  def change_status(self):
    try:
      self.connector.set_review_status(self.issue)
    except jira.utils.JIRAError as e:
      pass

  def _get_last_commit_message(self):
    return check_output(['git', 'log', '-1', 'HEAD']).decode('utf-8')
