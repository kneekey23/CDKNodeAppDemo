#!/usr/bin/env python3

from aws_cdk.core import App
from cdk.cdk_stack import CdkStack


app = App()
CdkStack(app, "NodeJsWebAppCDK")

app.synth()
