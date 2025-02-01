# Flask Twitter API

A simple Flask-based RESTful API that simulates basic Twitter functionality. This API provides endpoints for retrieving, filtering, and creating tweets using a JSON file as data storage.

## Features

1. **Tweet Management**
   - Get all tweets
   - Filter tweets based on specific values
   - Retrieve individual tweets by ID
   - Create new tweets

2. **API Endpoints**
   - `GET /`: Hello World endpoint
   - `GET /tweets`: Retrieve all tweets
   - `GET /tweets?filter=value`: Filter tweets by value
   - `GET /tweet/<tweet_id>`: Get specific tweet by ID
   - `POST /tweet`: Create a new tweet

## Data Storage

The API uses a JSON file (`100tweets.json`) to store tweet data. Ensure this file exists in your project directory with proper read/write permissions.

## Error Handling

- 404: Tweet not found
- 400: Invalid request (missing required fields)
- 201: Tweet created successfully

