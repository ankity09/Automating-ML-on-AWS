import boto3
import paramiko
import sys
def worker_handler(event, context):

    s3_client = boto3.client('s3')
    #Download private key file from secure S3 bucket
    s3_client.download_file('tests3ankit','s3-key-bucket/keys/ankit09.pem', '/tmp/ankit09.pem')

    k = paramiko.RSAKey.from_private_key_file("/tmp/ankit09.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host=event['IP']
    print "Connecting to " + host
    c.connect( hostname = host, username = "ec2-user", pkey = k )
    print "Connected to " + host

    commands = [
        "aws s3 cp s3://tests3ankit/s3-bucket/scripts/VoterPref.csv --region us-east-2 /home/ec2-user/VoterPref.csv",
        "aws s3 cp s3://tests3ankit/s3-bucket/scripts/test1.py --region us-east-2 /home/ec2-user/test1.py",
        "python /home/ec2-user/test1.py /home/ec2-user/VoterPref.csv",
        "aws s3 cp /home/ec2-user/Head_Voter.csv s3://emotion.ai.s3/Head_Voter.csv"
        ]

    for command in commands:
        print "Executing {}".format(command)
        stdin , stdout, stderr = c.exec_command(command)
        print stdout.read()
        print stderr.read()

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }


