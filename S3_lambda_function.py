import json
import boto3
import base64
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')
def lambda_handler(event, context):
    try:
        # Retrieve the uploaded file data from the event
        file_content_base64 = event['body']
        file_content = base64.b64decode(file_content_base64)
        # Upload file to S3
        bucket_name = 's3-test-2131'
        file_key = 'uploaded-file.txt'  # Provide a key/name for the uploaded file
        s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)
        response = {
            'statusCode': 200,
            'body': json.dumps({"message": "File uploaded successfully to S3"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except KeyError:
        # Handle KeyError if 'body' is not present in the event
        response = {
            'statusCode': 400,
            'body': json.dumps({"error": "Request body is missing"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except ClientError as e:
        # Handle S3 upload errors
        response = {
            'statusCode': 500,
            'body': json.dumps({"error": f"Error uploading file to S3: {e.response['Error']['Message']}"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        # Handle other exceptions
        response = {
            'statusCode': 500,
            'body': json.dumps({"error": f"Internal server error: {str(e)}"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    return response
