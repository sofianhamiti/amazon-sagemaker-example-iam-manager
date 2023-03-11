from constructs import Construct
from aws_cdk import (
    App,
    Stack,
)
from stack_constructs.iam_role import IAMRole


class IamManagerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str):
        super().__init__(scope, construct_id)

        # ===============================================
        # =============== CREATE IAM ROLE ===============
        # ===============================================
        iam_role = IAMRole(
            self, "iam_role", role_name="sm_role", policy_folder="iam_policies"
        )


app = App()
IamManagerStack(app, "IamManagerStack")
app.synth()
