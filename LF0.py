import json

def lambda_handler(event, context):
    
    # TODO implement
    message = "Application under development. Search functionality will be implemented in Assignment 3"
    return {
        'statusCode': 200,
        'body': json.dumps('' + message)
    }
