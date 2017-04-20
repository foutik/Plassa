from facepy import GraphAPI
import json
oauth_access_token='EAACEdEose0cBAG2MQPtn8cYL3JIDuLgxprP60IMIEuUdZCHWH5ONXH3QtQQcCOnKUzTXvZA9A20pqKF7J6ST7EhZBWdTEd4pznU4jZCWmvYdJN9bk2JWtLKAFQES7V76Fm3ZBab7ZCQNihIdEJPreMTwlAzwgZBMZANakFjLM3Moi2TbyqwjSH3nDhIOrfqfB9MZD'
graph = GraphAPI(oauth_access_token)
parsed=graph.get('597236887003311/posts')['data'][0]
print( json.dumps(parsed, indent=4, sort_keys=True))