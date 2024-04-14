import json
import boto3

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        # Retrieve the input data from the event
        input_data = json.loads(event['body'])
        action = input_data.get('action')
        instance_id = input_data.get('instanceId')
        instance_name = input_data.get('instanceName')
        ami_id = input_data.get('amiId')

        if action == 'stop':
            # Stop the instance
            ec2_client.stop_instances(InstanceIds=[instance_id])
            response = f"Instance {instance_id} is scheduled to be stopped."
        elif action == 'start':
            # Start the instance
            ec2_client.start_instances(InstanceIds=[instance_id])
            response = f"Instance {instance_id} is scheduled to be started."
        elif action == 'terminate':
            # Terminate the instance
            ec2_client.terminate_instances(InstanceIds=[instance_id])
            response = f"Instance {instance_id} is scheduled to be terminated."
        elif action == 'create':
            # Create a new EC2 instance
            new_instance = ec2_client.run_instances(
                ImageId=ami_id,
                InstanceType='t2.micro',  # Modify instance type as needed
                MinCount=1,
                MaxCount=1,
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': instance_name},
                        ]
                    },
                ]
            )
            new_instance_id = new_instance['Instances'][0]['InstanceId']
            response = f"New instance {new_instance_id} is being created."
        elif action == 'list':
            # List all instances and their statuses
            instances = ec2_client.describe_instances()
            instance_list = []
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    instance_state = instance['State']['Name']
                    instance_list.append(f"Instance ID: {instance_id}, State: {instance_state}")
            response = '\n'.join(instance_list)
        else:
            response = "Invalid action specified. Please provide 'action' as 'stop', 'start', 'terminate', 'create', or 'list'."

    except KeyError as e:
        # Handle KeyError if 'body' is not present in the event
        response = "Error: 'body' attribute not found in the request"
    except Exception as e:
        # Handle other exceptions
        response = f"Error: {str(e)}"

    return {
        'statusCode': 200,
        'body': response,
        'headers': {
            'Content-Type': 'text/plain'
        }
    }
