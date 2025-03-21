from operator import itemgetter

import boto3
import operator

ec2_client = boto3.client('ec2', region_name='us-east-1')

# we make a list of volumes based on special volume tag.
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        }
    ]
)
#make a list of all snapshots for each volume we found in previous list and find them by VolumeId filtering

for volume in volumes['Volumes']:
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )
    sorted_snapshots = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    ##we keep the two recent snapshots and remove the rest of them
    for snap in sorted_snapshots[2:]:
        ec2_client.delete_snapshot(
            SnaphsotId=snap['SnapshotId']
        )
