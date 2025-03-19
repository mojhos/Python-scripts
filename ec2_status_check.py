import boto3

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"instance is {instance['State']['Name']}")

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    instance_status = status['InstanceStatus']['Status']
    system_status = status['InstanceStatus']['Status']
    state = status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {state} and instance status is {instance_status} & system status is {system_status}")