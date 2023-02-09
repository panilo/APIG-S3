import aws_cdk as core
import aws_cdk.assertions as assertions

from apig+s3.apig+s3_stack import Apig+s3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in apig+s3/apig+s3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Apig+s3Stack(app, "apig-s3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
