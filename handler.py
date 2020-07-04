import os
import json
import redis


def search(event, context):

    input = event["queryStringParameters"]["input"]
    r = redis.Redis(
        host = os.getenv("REDIS_HOST"),
        port = os.getenv("REDIS_PORT"),
        password = os.getenv("REDIS_PASSWORD")
    )

    r.set('foo','bar')
    redis_response = r.get('foo')
    r.set('foo2','bar2')
    redis_response2 = r.get('foo2')

    body = {
            "message": "Redis says: {}".format(redis_response),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
