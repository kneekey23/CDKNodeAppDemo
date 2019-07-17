from aws_cdk.core import Stack, Construct, Environment
from aws_cdk import aws_ecs, aws_ec2, aws_ecs_patterns

AWS_ENV = Environment(account='805580953652', region='us-west-2')

VPC_ID = 'vpc-5903d820'

class CdkStack(Stack):

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # The code that defines your stack goes here
        vpc = aws_ec2.Vpc(self, 'vpc')
        cluster = aws_ecs.Cluster(self, 'cluster', vpc=vpc)
        # task_definition = aws_ecs.FargateTaskDefinition(self, 'NodeTask')
        # log_driver = aws_ecs.LogDriver.aws_logs(stream_prefix="NodeAppContainerLog")
        # container = task_definition.add_container('NodeApp',
        #                               image=aws_ecs.ContainerImage.from_asset("nodejsapp"), logging=log_driver)
        # port_mapping = aws_ecs.PortMapping(container_port=8080)
        # container.add_port_mappings(port_mapping)
        #
        # aws_ecs.FargateService(self, 'service',
        #                        cluster=cluster,
        #                        task_definition=task_definition,
        #                        desired_count=5)
        aws_ecs_patterns.LoadBalancedFargateService(self, 'NodeApp', cluster=cluster, desired_count=5, container_name="NodeApp", container_port=8080, image=aws_ecs.ContainerImage.from_asset("nodejsapp"))
