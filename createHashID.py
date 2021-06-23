import json
import random
import string
import boto3

def lambda_handler(event, context):
    
    # get long url
    longurl = event["url"]
    rnd = generate_random(6)
    
    message = {"id": rnd, "url":longurl}
    
    client = boto3.client('sns')
    
    arn = 'topic_name'
    
    response = client.publish(
    TargetArn=arn,
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json'
    )
    
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {"id": rnd, "status": "Succesfully Posted to SNS" }
    else:
        return { "id": rnd, "status": "SNS Failure" }
        

def generate_random(n):
    
    # create a first random
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(n))
