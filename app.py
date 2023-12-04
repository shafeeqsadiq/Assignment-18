from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Hello World Endpoint
@app.route('/')
def hello_world():
    return 'Hello World!'

# Get All Tweets Endpoint
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    with open('tweets.json', 'r') as file:
        tweets = json.load(file)
    return jsonify(tweets)

# Filter Tweets Endpoint
@app.route('/tweets', methods=['GET'])
def filter_tweets():
    filter_value = request.args.get('filter')
    with open('tweets.json', 'r') as file:
        tweets = json.load(file)
    filtered_tweets = [tweet for tweet in tweets if filter_value in tweet.values()]
    return jsonify(filtered_tweets)

# Get Specific Tweet Endpoint
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet(tweet_id):
    with open('tweets.json', 'r') as file:
        tweets = json.load(file)
    for tweet in tweets:
        if tweet.get('id') == tweet_id:
            return jsonify(tweet)
    return jsonify({'error': 'Tweet not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

