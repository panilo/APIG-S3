#!/usr/bin/env python3
import os

import aws_cdk as cdk

from apig_s3.apig_s3_stack import ApigS3Stack


app = cdk.App()
ApigS3Stack(app, "ApigS3Stack")

app.synth()