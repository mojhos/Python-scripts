import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-1')

def create_snapshot_from_volumes():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )

schedule.every(12).hours.do(create_snapshot_from_volumes)
while True:
    schedule.run_pending()