# Welcome to Star Wars Sentiment Analysis API
![](https://i.ytimg.com/vi/COpfoyX3qMY/maxresdefault.jpg)

This API has been created in order to analyse the level of **negativity/positivity** and **objectivity/subjectivity** of Star Wars characters during the episodes IV, V and VI.

Follow the steps below to navigate the API.

## API Endpoints
You can call the following endpoints to get the information you're requesting:

### GET endpoints
* /characters: You will get a list containing every characters' name and their ID number.
* /episodes: You will get a list containing every episode name and its ID number.
* /dialogue/"charactername": Replace "charactername" for any of the character names you got from the endpoint "/characters" to get the character's dialogue (i.e. if you type "/dialogue/yoda", you will get a list of all what Yoda said during the movies).
* /dialogue/"charactername"/sent: Replace "charactername" as explained in the previous bullet point. You will get the sentiment analysis of the specific character.
* /dialogues: You will get all dialogues in the 3 movies.
* /all/sent: It analyses the sentiment from all dialogues in the 3 movies.

### POST endpoints
* /newdialogue: Use this endpoint (post type) to post a new dialogue in the API. In order to do this, use Jupyter Notebook and make a post request with the following data:
    * import requests and type "requests.post(url, data=yourdictionary)", where:
        - **url** = http://127.0.0.1:5000/newdialogue
        - **data** = {'dialogue':"Insert your new dialogue here","char": Insert the ID number of the chosen character here (see "/characters" endpoint to get their ID),"episode":Insert the ID number of the chosen episode here (see "/episodes" endpoint to get their ID)}.

       An example of a dialogue insertion would be: **"{'dialogue':"hello","char":2,"episode":3}**, where "hello" is what the character says, 2 is the character ID (that we know it corresponds to Luke because of "/characters" endpoint) and 3 is the episode ID (that we know it corresponds to episode 6 because of "/episodes" endpoint).