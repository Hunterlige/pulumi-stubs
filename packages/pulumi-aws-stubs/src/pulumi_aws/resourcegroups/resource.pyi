

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourceArgs', 'Resource']
@pulumi.input_type
class ResourceArgs:
    def __init__(__self__, *, group_arn: pulumi.Input[_builtins.str], resource_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupArn")
    def group_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_arn.setter
    def group_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourceState:
    def __init__(__self__, *, group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupArn")
    def group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_arn.setter
    def group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:resourcegroups/resource:Resource")
class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ...) -> Resource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupArn")
    def group_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


