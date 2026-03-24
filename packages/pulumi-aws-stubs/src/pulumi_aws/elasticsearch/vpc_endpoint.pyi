

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
__all__ = ['VpcEndpointArgs', 'VpcEndpoint']
@pulumi.input_type
class VpcEndpointArgs:
    def __init__(__self__, *, domain_arn: pulumi.Input[_builtins.str], vpc_options: pulumi.Input[VpcEndpointVpcOptionsArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_arn.setter
    def domain_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Input[VpcEndpointVpcOptionsArgs]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: pulumi.Input[VpcEndpointVpcOptionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcEndpointState:
    def __init__(__self__, *, domain_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_options: Optional[pulumi.Input[VpcEndpointVpcOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_arn.setter
    def domain_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input[VpcEndpointVpcOptionsArgs]]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input[VpcEndpointVpcOptionsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:elasticsearch/vpcEndpoint:VpcEndpoint")
class VpcEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_options: Optional[pulumi.Input[Union[VpcEndpointVpcOptionsArgs, VpcEndpointVpcOptionsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., domain_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_options: Optional[pulumi.Input[Union[VpcEndpointVpcOptionsArgs, VpcEndpointVpcOptionsArgsDict]]] = ...) -> VpcEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output[outputs.VpcEndpointVpcOptions]:
        
        ...
    


