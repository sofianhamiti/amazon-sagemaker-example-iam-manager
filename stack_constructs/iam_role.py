import os
import json
from constructs import Construct
from aws_cdk import aws_iam as iam


class IAMRole(Construct):
    def __init__(self, scope: Construct, id: str, role_name: str, policy_folder: str):
        super().__init__(scope, id)

        # ==================================================
        # ================ CREATE IAM ROLE =================
        # ==================================================
        self.role = iam.Role(
            scope=self,
            id=role_name,
            role_name=role_name,
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
        )

        # ==================================================
        # ========= CREATE POLICIES FROM JSON FILES ========
        # ==================================================
        # Loop through the policy files in the specified folder
        for filename in os.listdir(policy_folder):
            if filename.endswith(".json"):
                with open(os.path.join(policy_folder, filename)) as f:
                    # Create IAM policy from JSON file
                    policy_document = iam.PolicyDocument.from_json(json.loads(f.read()))
                    policy = iam.Policy(
                        self, f"Policy{filename}",
                        policy_name=f"{filename}",
                        document=policy_document
                    )
                    
                    # Attach policy to IAM role
                    self.role.attach_inline_policy(policy)
