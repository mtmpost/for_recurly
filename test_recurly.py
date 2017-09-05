#!/usr/lib/env python
import recurly_common, pytest, logging 
log = logging.getLogger('recurly.http.response')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
log.addHandler(ch)


class Test_UI(object):


  def test_api_calls(self):
    make_subs = 3
    sub = 0
    api = recurly_common.APICalls()
    log.info("\n")
    log.info("#=========making subscriptions#")
    mksub = api.new_subscription
    while sub < make_subs:
      mksub()
      sub += 1
    log.info("getting subscriptions")
    getsub = api.get_subs()

    if make_subs == getsub:
      log.info("Subscriptions successfully created")
    else:
      log.info("there's a problem. We only have {} subscription and there should be {}".format(getsub, make_subs))

  def test_search(self):
    self.ui_driver = recurly_common.UI_Interactor()
    self.ui_driver.start()
    self.ui_driver.login_page()
    self.ui_driver.login('mtmpost@gmail.com', '1change2me3')
    self.ui_driver.subscriptions()
    self.ui_driver.search("Michael1")
