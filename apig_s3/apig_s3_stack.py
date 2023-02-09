from aws_cdk import (    
    Stack,
    aws_apigateway as apig,
    aws_iam as iam
)
from aws_cdk.aws_apigateway import IntegrationOptions
from constructs import Construct

class ApigS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_apig = apig.RestApi(self, "ApigAndS3")
        bucket_resource = my_apig.root.add_resource("{bucketName}")
        item_resource = bucket_resource.add_resource("{item}")

        policy = {
          "s3write": iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(actions=["s3:PutObject"], effect=iam.Effect.ALLOW, resources=["*"])
              ]
            )
        }
        role = iam.Role(self, "APIGRole", assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"), inline_policies=policy)

        integration_response = apig.IntegrationResponse(status_code="200")
        integration_options = IntegrationOptions(
          request_parameters={
            "integration.request.path.bucket":"method.request.path.bucketName",
            "integration.request.path.object":"method.request.path.item"
          }, 
          credentials_role=role, 
          integration_responses=[integration_response]
        )        
        bucket_integration = apig.AwsIntegration(service="s3", integration_http_method="PUT", path="{bucket}/{object}", region="eu-west-1", options=integration_options)

        post_to_bucket_method = item_resource.add_method("PUT", integration=bucket_integration, 
          request_parameters={
            "method.request.path.bucketName": True,
            "method.request.path.item": True
          },
          method_responses=[apig.MethodResponse(status_code="200")]
        )  

        

        
