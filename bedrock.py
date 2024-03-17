import boto3
import json

bedrock = boto3.client(
    service_name = 'bedrock-runtime',
    region_name = 'us-east-1'
    )
    
input = {
  "modelId": "cohere.command-text-v14",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{\"prompt\":\"Please write a four liner poem on machine learning.\",\"max_tokens\":400,\"temperature\":0.75,\"p\":0.01,\"k\":0,\"stop_sequences\":[],\"return_likelihoods\":\"NONE\"}"
}
    
response = bedrock.invoke_model(body=input["body"],
                                    modelId=input["modelId"],
                                    accept=input["accept"],
                                    contentType=input["contentType"])
                                    
response_body = json.loads(response['body'].read())
    
print(response_body)