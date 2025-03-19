import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

def check_instance_status ():
    statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        instance_status = status['InstanceStatus']['Status']
        system_status = status['InstanceStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} and instance status is {instance_status} & system status is {system_status}")
schedule.every(5).seconds.do(check_instance_status)
while True:
    schedule.run_pending()