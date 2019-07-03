sudo yum update

On the Linux EC2 instance, run the following command and paste the Access Key and Secret Access key from the downloaded Excel file into the terminal. Also specify the region name, where your EC2 instance is running. For the last “Default output format” hit “Enter” and move forward.

[ec2-user@ip-172-31-43-46 ~]$ aws configure
AWS Access Key ID [None]: AK----------V3KAQ
AWS Secret Access Key [None]: abtQ/1+5---------RObx4FQt
Default region name [None]: us-east-2   
Default output format [None]:

Copy your .pem and the workerfunction.py file to the EC2 instance from the S3 bucket you uploaded it to in Step 2
aws s3 cp s3://tests3ankit/keys/ankit09.pem /home/ec2-user/
aws s3 cp s3://videos-original/wang.pem /home/ec2-user/
aws s3 cp s3://videos-original/worker_function.py /home/ec2-user/
aws s3 cp s3://videos-original/worker_function.zip /home/ec2-user/

Run the following commands to setup your EC2 instance.
pip install virtualenv
virtualenv /home/ec2-user/emotionai-env
source /home/ec2-user/emotionai-env/bin/activate
pip install paramiko
pip install pandas
pip install boto3
zip -r /home/ec2-user/worker_function.zip /home/ec2-user/emotionai-env/lib/python2.7/site-packages/
zip -r /home/ec2-user/worker_function.zip /home/ec2-user/emotionai-env/lib64/python2.7/site-packages/
zip worker_function.zip worker_function.py
aws s3 cp /home/ec2-user/worker_function.zip s3://videos-original/keys/
