#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_enquete.cdk_enquete_stack import CdkEnqueteStack


app = cdk.App()
CdkEnqueteStack(app, "CdkEnqueteStack")

app.synth()
