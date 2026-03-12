ef lambda_handler(event, context):
    # Example: return a simple message
    return {
        'statusCode': 200,
        'body': 'Hello from AWS Lambda using Python and created by Hero Arjun!'
    }
