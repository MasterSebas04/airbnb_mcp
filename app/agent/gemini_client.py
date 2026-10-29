from dotenv import load_dotenv
import json
import os
import boto3

load_dotenv(override=True)

client = boto3.client('bedrock-runtime', region_name=os.environ['AWS_REGION'])
response = client.invoke_model(
    modelId='us.anthropic.claude-opus-4-6-v1',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
)
print(json.loads(response['body'].read()))
