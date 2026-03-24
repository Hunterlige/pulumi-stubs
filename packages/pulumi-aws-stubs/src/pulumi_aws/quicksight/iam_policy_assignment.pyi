

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IamPolicyAssignmentArgs', 'IamPolicyAssignment']
@pulumi.input_type
class IamPolicyAssignmentArgs:
    def __init__(__self__, *, assignment_name: pulumi.Input[_builtins.str], assignment_status: pulumi.Input[_builtins.str], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @assignment_name.setter
    def assignment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentStatus")
    def assignment_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @assignment_status.setter
    def assignment_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _IamPolicyAssignmentState:
    def __init__(__self__, *, assignment_id: Optional[pulumi.Input[_builtins.str]] = ..., assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., assignment_status: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentId")
    def assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assignment_id.setter
    def assignment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assignment_name.setter
    def assignment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentStatus")
    def assignment_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assignment_status.setter
    def assignment_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[IamPolicyAssignmentIdentitiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IamPolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., assignment_status: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[Union[IamPolicyAssignmentIdentitiesArgs, IamPolicyAssignmentIdentitiesArgsDict]]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IamPolicyAssignmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., assignment_id: Optional[pulumi.Input[_builtins.str]] = ..., assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., assignment_status: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[Union[IamPolicyAssignmentIdentitiesArgs, IamPolicyAssignmentIdentitiesArgsDict]]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> IamPolicyAssignment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentId")
    def assignment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentStatus")
    def assignment_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> pulumi.Output[Optional[outputs.IamPolicyAssignmentIdentities]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


