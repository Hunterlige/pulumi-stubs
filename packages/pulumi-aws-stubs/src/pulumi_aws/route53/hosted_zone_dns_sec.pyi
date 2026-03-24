

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HostedZoneDnsSecArgs', 'HostedZoneDnsSec']
@pulumi.input_type
class HostedZoneDnsSecArgs:
    def __init__(__self__, *, hosted_zone_id: pulumi.Input[_builtins.str], signing_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_status.setter
    def signing_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _HostedZoneDnsSecState:
    def __init__(__self__, *, hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., signing_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_status.setter
    def signing_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53/hostedZoneDnsSec:HostedZoneDnsSec")
class HostedZoneDnsSec(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., signing_status: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HostedZoneDnsSecArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., signing_status: Optional[pulumi.Input[_builtins.str]] = ...) -> HostedZoneDnsSec:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingStatus")
    def signing_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


