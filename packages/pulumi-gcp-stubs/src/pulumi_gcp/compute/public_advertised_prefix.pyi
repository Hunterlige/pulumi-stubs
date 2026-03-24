

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PublicAdvertisedPrefixArgs', 'PublicAdvertisedPrefix']
@pulumi.input_type
class PublicAdvertisedPrefixArgs:
    def __init__(__self__, *, ip_cidr_range: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., dns_verification_ip: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pdp_scope: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_verification_ip.setter
    def dns_verification_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pdpScope")
    def pdp_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pdp_scope.setter
    def pdp_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PublicAdvertisedPrefixState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., dns_verification_ip: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pdp_scope: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., shared_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_verification_ip.setter
    def dns_verification_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pdpScope")
    def pdp_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pdp_scope.setter
    def pdp_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PublicAdvertisedPrefix(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns_verification_ip: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pdp_scope: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PublicAdvertisedPrefixArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns_verification_ip: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pdp_scope: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., shared_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> PublicAdvertisedPrefix:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pdpScope")
    def pdp_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


