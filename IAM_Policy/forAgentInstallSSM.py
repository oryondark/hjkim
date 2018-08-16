cli = boto3.client('sts')
res = cli.assume_role(
	RoleArn="roleARNofMasters",
	RoleSessionName="test"
)
ack = res['Credentials']['AccessKeyId']
sec = res['Credentials']['SecretAccessKey']
token = res['Credentials']['SessionToken']
cli = boto3.client(
	'ssm',
	aws_access_key_id=ack,
	aws_secret_access_key=sec,
	aws_session_token=token
)

res = cli.send_command(
	Targets=[{
		'Key':'instanceids',
		'Values':['instanceID']
	}],
	DocumentName='AWS-ConfigureAWSPackage',
	Parameters={"action":["Install"],"name":["AmazonCloudWatchAgent"],"version":["latest"]}
)

res = cli.send_command(
	Targets=[{
		'Key':'instanceids',
		'Values':['instanceID']
	}],
	DocumentName="AmazonCloudWatch-ManageAgent",
	Parameters={"action":["configure"],"mode":["ec2"],"optionalConfigurationSource":["ssm"],"optionalConfigurationLocation":["AmazonCloudWatch-linux"],"optionalRestart":["yes"]}
)

res = cli.send_command(
	Targets=[{
		'Key':'instanceids',
		'Values':['instanceID']
	}],
	DocumentName="AmazonCloudWatch-ManageAgent",
	Parameters={"action":["start"],"mode":["ec2"],"optionalConfigurationSource":["ssm"],"optionalRestart":["yes"]}
)
