import os
import json

# Connect and retrieve on cold start
import trie_redis
from levenshtein import autocomplete, extract_suggestions

blob = trie_redis.get_word_list()
words = eval(blob) 

# Perform only autocomplete on warm start

def levenshtein(event, context):
    input_ = event["queryStringParameters"]["input"]

    limit = 5
    try:
        limit = event["queryStringParameters"]["limit"]
    except:
        pass

    print(limit)

    suggestions = autocomplete(words, input_, limit=int(limit))
    print(suggestions)
    body = {
            "suggestions": str(list(extract_suggestions(suggestions)))
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }
    return response
