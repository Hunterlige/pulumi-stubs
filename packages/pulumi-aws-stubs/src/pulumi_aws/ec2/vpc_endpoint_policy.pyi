

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcEndpointPolicyArgs', 'VpcEndpointPolicy']
@pulumi.input_type
class VpcEndpointPolicyArgs:
    def __init__(__self__, *, vpc_endpoint_id: pulumi.Input[_builtins.str], policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcEndpointPolicyState:
    def __init__(__self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/vpcEndpointPolicy:VpcEndpointPolicy")
class VpcEndpointPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcEndpointPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcEndpointPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


