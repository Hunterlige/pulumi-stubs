

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountAssignmentArgs', 'AccountAssignment']
@pulumi.input_type
class AccountAssignmentArgs:
    def __init__(__self__, *, instance_arn: pulumi.Input[_builtins.str], permission_set_arn: pulumi.Input[_builtins.str], principal_id: pulumi.Input[_builtins.str], principal_type: pulumi.Input[_builtins.str], target_id: pulumi.Input[_builtins.str], target_type: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission_set_arn.setter
    def permission_set_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal_type.setter
    def principal_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AccountAssignmentState:
    def __init__(__self__, *, instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @permission_set_arn.setter
    def permission_set_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_type.setter
    def principal_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ssoadmin/accountAssignment:AccountAssignment")
class AccountAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccountAssignmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ...) -> AccountAssignment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


