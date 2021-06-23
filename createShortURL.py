import json
import boto3

def lambda_handler(event, context):
    
    #parsing the message
    info = json.loads(event['Records'][0]['Sns']['Message'])
    
    hashID = '/' + info["id"]
    longURL = info["url"]

    # call the InsertFunction
    InsertDynamo(longURL, hashID)
    

def InsertDynamo(longURL, hashID):
	

	# creates the dynamo OBJECT
    dynamodb = boto3.resource("dynamodb", region_name="sa-east-1")
	
    # specify the dynamo table
    table = dynamodb.Table("TABLE_NAME")

    # boto3 put_item function to insert into a dynamoDB table
    table.put_item(
        Item={
            "url-hash": hashID,
            "longurl": longURL
        }
    )
