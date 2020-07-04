import os
import json

import trie_redis


def search(event, context):

    input_ = event["queryStringParameters"]["input"]

    blob = trie_redis.retrieve_trie()
    trie = eval(blob)

    suggestions = trie_redis.autocomplete_trie(trie, input_)
    body = {
            "suggestions": str(list(suggestions))
    } 
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
