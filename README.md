# APIGateway + S3

Uses API Gateway as a proxy for S3, based on AWS POC at this [link](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html). 

This example only exposes a PUT method to store data in S3, though can be extended to support further operations.

## Sending data to S3

You can use _curl_ to send data to S3 with the following command 

`curl -XPUT https://1234.execute-api.eu-west-1.amazonaws.com/prod/mybucket/myfile.json -d @message.json`

Replace 
- the API Gateway URL with the one you deployed;
- mybucket and myfile.json, the former with a bucket that exists and you have write access on, the latter is the object key of your choice;
- message.json is a simple JSON payload as the following, stored in a file named _message.json_

```json
{
  "id": "a1",
  "version": "1.1",
  "arr1": [
    {
      "name": "item1"
    },
    {
      "name": "item2"
    }
  ],
  "object": {
    "attr1": "blabla"
  },
  "arr2": [
    {
      "field": "blabla"
    }
  ]
}
```