from operator import itemgetter

import boto3
import operator

ec2_client = boto3.client('ec2', region_name='us-east-1')

snapshots = ec2_client.describe_snapshots(
    OwnerId=['self']
)
sorted_snapshots = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
for snap in sorted_snapshots[2:]:               ##we keep the two recent snapshots and remove the rest
    ec2_client.delete_snapshot(
        SnaphsotId= snap['SnapshotId']
    )