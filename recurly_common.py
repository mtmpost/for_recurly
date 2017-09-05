#!/usr/bin/env/python

import recurly, requests, uuid, logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 

api_key = 'c11e76cf377144c8b5be2925e3800a5f'
recurly.SUBDOMAIN = 'mtmpost'
recurly.API_KEY = api_key
recurly.DEFAULT_CURRENCY = 'USD'

log = logging.getLogger('recurly.http.response')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
log.addHandler(ch)


class APICalls(object):

  def new_subscription(self):
    
    try:
      subscription = recurly.Subscription()
      subscription.plan_code = 'pro'
      subscription.currency = 'USD'

      account = recurly.Account(account_code = uuid.uuid1())
      account.email = 'mtmpost+1@gmail.com'
      account.first_name = 'Michael1'
      account.last_name = 'McGovern'

      billing_info = recurly.BillingInfo()
      billing_info.number = '4111-1111-1111-1111'
      billing_info.month = 05
      billing_info.year = 2019

      account.billing_info = billing_info
      subscription.account = account
      log.warn("========================test========================")
      subscription.save()
    except recurly.NotFoundError:
      print 'Account not Found.\n'
    except recurly.errors:
      for e in errors:
	print "%s:%s" % (e.field, e.message) 

  def get_subs(self):
    sub_num = 0
    for subs in recurly.Subscription.all():
      print 'Subscriptions: {}'.format(subs.state)
      sub_num += 1
    return sub_num

#===============================================

class UI_Interactor(object):
  #base class for interacting with the UI

  def __init__(self):
    self.driver = webdriver.Chrome()
    self.driver.set_window_size(1280, 900)
    self.driver.maximize_window()
    self.start()

  def start(self):
    self.driver.get("https://recurly.com/")
    log.info("=============>>>>>>>>>>{}<<<<<<<=============\n".format(self.driver.title))


  def login_page(self):
    inputElement = self.driver.find_element_by_xpath('//a[@data-event="login-clicked"]')
    inputElement.click()

  def login(self, email, pwd):
    enterEmail = self.driver.find_element_by_id("user_email").send_keys(email)
    enterPassword = self.driver.find_element_by_id("user_password").send_keys(pwd)
    login = self.driver.find_element_by_id("submit_button")
    login.submit()

  def subscriptions(self):
    subscriptions = self.driver.find_element_by_xpath('//a[@href="/subscriptions"]')
    subscriptions.click()

  def search(self, term):
    search = self.driver.find_element_by_name("q")
    search.send_keys(term)
    searchButton = self.driver.find_element_by_xpath('//i[@class="ricon ricon-search"]')
    searchButton.click()


  """
  try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese"))
    print driver.title
  finally:
    driver.quit()
  """








"""
make_subs = 3
sub = 0
api = APICalls()
mksub = api.new_subscription

while sub < make_subs:
  mksub()
  sub += 1

getsub = api.get_subs()

if make_subs == getsub:
  print 'all subs successfully created'
else:
  print "there's a problem. We only have {} subscription and there should be {}".format(getsub, make_subs)
"""


