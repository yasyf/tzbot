from api import API
import tweepy, os

USERNAME = os.getenv('TWITTER_USERNAME')

class StreamListener(tweepy.StreamListener):
  def on_status(self, status):
    if status.user.screen_name != USERNAME and not status.retweeted:
      self.api.update_status('@{} {} to you too!'.format(status.user.screen_name, status.text))

class Stream(object):
  def __init__(self):
    self.api = API().client
    self.listener = StreamListener(self.api)

  def start(self):
    tweepy.Stream(auth=self.api.auth, listener=self.listener).userstream()