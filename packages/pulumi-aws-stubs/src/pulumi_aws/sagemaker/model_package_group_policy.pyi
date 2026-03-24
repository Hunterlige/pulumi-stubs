

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ModelPackageGroupPolicyArgs', 'ModelPackageGroupPolicy']
@pulumi.input_type
class ModelPackageGroupPolicyArgs:
    def __init__(__self__, *, model_package_group_name: pulumi.Input[_builtins.str], resource_policy: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @model_package_group_name.setter
    def model_package_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @resource_policy.setter
    def resource_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ModelPackageGroupPolicyState:
    def __init__(__self__, *, model_package_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_package_group_name.setter
    def model_package_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_policy.setter
    def resource_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ModelPackageGroupPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., model_package_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ModelPackageGroupPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., model_package_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> ModelPackageGroupPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> pulumi.Output[_builtins.str]:
        ...
    


