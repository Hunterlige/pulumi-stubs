

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssessmentDelegationArgs', 'AssessmentDelegation']
@pulumi.input_type
class AssessmentDelegationArgs:
    def __init__(__self__, *, assessment_id: pulumi.Input[_builtins.str], control_set_id: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], role_type: pulumi.Input[_builtins.str], comment: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @assessment_id.setter
    def assessment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlSetId")
    def control_set_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @control_set_id.setter
    def control_set_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_type.setter
    def role_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AssessmentDelegationState:
    def __init__(__self__, *, assessment_id: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., control_set_id: Optional[pulumi.Input[_builtins.str]] = ..., delegation_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., role_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assessment_id.setter
    def assessment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlSetId")
    def control_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_set_id.setter
    def control_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationId")
    def delegation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegation_id.setter
    def delegation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AssessmentDelegation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assessment_id: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., control_set_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., role_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AssessmentDelegationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., assessment_id: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., control_set_id: Optional[pulumi.Input[_builtins.str]] = ..., delegation_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., role_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> AssessmentDelegation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlSetId")
    def control_set_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationId")
    def delegation_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


