import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        :"JSFLjgpdtPyOhDOvdu1lLasFz"
    "consumer_secret"     :"of3nZBlmln0YA6NRq719w9PYxX2XyLnayvDoZ9ieec07HhGYMU"
    "access_token"        :"966159043055308800-Uw2ELg4YZgrQkv90kzdhTtxKiSr7PNx"
    "access_token_secret" :"0JJkaaMvgR0qyDgyhy0JhgEvf617euPvw1hNLTRHwsnQf"

    }

  api = get_api(cfg)
  tweet = "hello rishika here"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
