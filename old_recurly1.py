#!/usr/bin/env/python

import recurly, requests, uuid, logging

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



