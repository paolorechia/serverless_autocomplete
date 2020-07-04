import os
import json

# Connect and retrieve on cold start
import trie_redis


blob = trie_redis.retrieve_trie()
trie = eval(blob)

# Perform only autocomplete on warm start
def search(event, context):

    input_ = event["queryStringParameters"]["input"]

    suggestions = trie_redis.autocomplete_trie(trie, input_)
    body = {
            "suggestions": str(list(suggestions))
    } 
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
