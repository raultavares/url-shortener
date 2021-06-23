import json
import boto3

def lambda_handler(event, context):
    
    uri = event["Records"][0]["cf"]["request"]["uri"];
    
    response = {
        "status": "301",
        "statusDescription": "Moved Permanently",
        "headers": {"location": [{"key": "Location", "value": get_longURL(uri)}], "cache-control": [{
            "key": 'Cache-Control',
            "value": "max-age=100"
          }],},
    }
    
    # CloudWatch Logs' life made easy!
    print(response)

    return response
    
def get_longURL(url_hash):
    
    dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')

    table = dynamodb.Table('TABLE_NAME')

    response = table.get_item(Key={'url-hash': url_hash})
    
    return response["Item"]["longurl"]
