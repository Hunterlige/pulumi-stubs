

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OutboundWebIdentityFederationArgs', 'OutboundWebIdentityFederation']
@pulumi.input_type
class OutboundWebIdentityFederationArgs:
    def __init__(__self__) -> None:
        
        ...
    


@pulumi.input_type
class _OutboundWebIdentityFederationState:
    def __init__(__self__, *, issuer_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerIdentifier")
    def issuer_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issuer_identifier.setter
    def issuer_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OutboundWebIdentityFederation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[OutboundWebIdentityFederationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., issuer_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> OutboundWebIdentityFederation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerIdentifier")
    def issuer_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


