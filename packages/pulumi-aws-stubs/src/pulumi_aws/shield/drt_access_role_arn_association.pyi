

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
__all__ = ['DrtAccessRoleArnAssociationArgs', 'DrtAccessRoleArnAssociation']
@pulumi.input_type
class DrtAccessRoleArnAssociationArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], timeouts: Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DrtAccessRoleArnAssociationState:
    def __init__(__self__, *, role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DrtAccessRoleArnAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DrtAccessRoleArnAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DrtAccessRoleArnAssociationTimeoutsArgs, DrtAccessRoleArnAssociationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DrtAccessRoleArnAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DrtAccessRoleArnAssociationTimeoutsArgs, DrtAccessRoleArnAssociationTimeoutsArgsDict]]] = ...) -> DrtAccessRoleArnAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DrtAccessRoleArnAssociationTimeouts]]:
        ...
    


