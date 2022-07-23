# Image Webscrape Microservice

## Instructions

1. Download the repository locally.
2. If not already installed, install python3, requests, bs4, flask
3. Navigate to main.py and either run python3 main.py or "flask run"
   Congratulations the server is now running!

## Sending a request to the microservice (via HTTP)

1. GET requests are sent to localhost:105/get_image/<vegetable> where <vegetable> is the vegetable you'd like an image for

## Receiving a response from the microservice (via HTTP)

The response is a JSON object {"image-link": <link_to_google_image>} where <link_to_google_image> is a link to a google image associated with that vegetable searched

Note: In the offchance that the vegetable was unable to be found via google image search, a response of "Sorry, unable to find image associated with {vegetable}" will be returned.
