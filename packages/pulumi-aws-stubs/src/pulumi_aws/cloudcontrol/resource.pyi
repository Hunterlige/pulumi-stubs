

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
    def __init__(__self__, *, desired_state: pulumi.Input[_builtins.str], type_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., type_version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeVersionId")
    def type_version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_version_id.setter
    def type_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourceState:
    def __init__(__self__, *, desired_state: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., type_version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeVersionId")
    def type_version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_version_id.setter
    def type_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudcontrol/resource:Resource")
class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., type_version_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., type_version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Resource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeVersionId")
    def type_version_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


