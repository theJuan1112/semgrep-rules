import boto3
from boto3 import client

# ruleid:hardcoded-token
client("s3", aws_secret_access_key="9ekAkjIs+UE2f1XLm7wgSAf9HkBEqJmbK3oHx9NC")

# ruleid:hardcoded-token
boto3.sessions.Session(aws_secret_access_key="9ekAkjIs+UE2f1XLm7wgSAf9HkBEqJmbK3oHx9NC")

s = boto3.sessions
# ruleid:hardcoded-token
s.Session(aws_access_key_id="AKIAYVP4CIPPMP5UU6VI")

uhoh_key = "AKIAYVP4CIPPMP5UU6VI"
ok_secret = os.environ.get("SECRET_ACCESS_KEY")
# ruleid:hardcoded-token
s3 = boto3.resource(
    "s3",
    aws_access_key_id=uhoh_key,
    aws_secret_access_key=ok_secret,
    region_name="sfo2",
    endpoint_url="https://sfo2.digitaloceanspaces.com",
)

ok_key = os.environ.get("ACCESS_KEY_ID")
uhoh_secret = "9ekAkjIs+UE2f1XLm7wgSAf9HkBEqJmbK3oHx9NC"
# ruleid:hardcoded-token
s3 = boto3.resource(
    "s3",
    aws_access_key_id=ok_key,
    aws_secret_access_key=uhoh_secret,
    region_name="sfo2",
    endpoint_url="https://sfo2.digitaloceanspaces.com",
)

# ok:hardcoded-token
s3 = client("s3", aws_access_key_id="this-is-not-a-key")

# ok:hardcoded-token
s3 = boto3.resource(
    "s3",
    aws_access_key_id="XXXXXXXX",
    aws_secret_access_key="----------------",
    region_name="us-east-1",
)

# ok:hardcoded-token
s3 = boto3.resource(
    "s3",
    aws_access_key_id="<your token here>",
    aws_secret_access_key="<your secret here>",
    region_name="us-east-1",
)

# ok:hardcoded-token
key = os.environ.get("ACCESS_KEY_ID")
secret = os.environ.get("SECRET_ACCESS_KEY")
s3 = boto3.resource(
    "s3",
    aws_access_key_id=key,
    aws_secret_access_key=secret,
    region_name="sfo2",
    endpoint_url="https://sfo2.digitaloceanspaces.com",
)
