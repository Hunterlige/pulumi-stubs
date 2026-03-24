

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcEndpointServiceAllowedPrincipleArgs', 'VpcEndpointServiceAllowedPrinciple']
@pulumi.input_type
class VpcEndpointServiceAllowedPrincipleArgs:
    def __init__(__self__, *, principal_arn: pulumi.Input[_builtins.str], vpc_endpoint_service_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal_arn.setter
    def principal_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcEndpointServiceAllowedPrincipleState:
    def __init__(__self__, *, principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_arn.setter
    def principal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcEndpointServiceAllowedPrinciple(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcEndpointServiceAllowedPrincipleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcEndpointServiceAllowedPrinciple:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


