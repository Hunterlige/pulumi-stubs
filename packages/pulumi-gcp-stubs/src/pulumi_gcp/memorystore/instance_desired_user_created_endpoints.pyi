

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceDesiredUserCreatedEndpointsArgs', 'InstanceDesiredUserCreatedEndpoints']
@pulumi.input_type
class InstanceDesiredUserCreatedEndpointsArgs:
    def __init__(__self__, *, region: pulumi.Input[_builtins.str], desired_user_created_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredUserCreatedEndpoints")
    def desired_user_created_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]]:
        
        ...
    
    @desired_user_created_endpoints.setter
    def desired_user_created_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceDesiredUserCreatedEndpointsState:
    def __init__(__self__, *, desired_user_created_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredUserCreatedEndpoints")
    def desired_user_created_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]]:
        
        ...
    
    @desired_user_created_endpoints.setter
    def desired_user_created_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InstanceDesiredUserCreatedEndpoints(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., desired_user_created_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs, InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceDesiredUserCreatedEndpointsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., desired_user_created_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs, InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceDesiredUserCreatedEndpoints:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredUserCreatedEndpoints")
    def desired_user_created_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpoint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


