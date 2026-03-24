

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
__all__ = ['RouterArgs', 'Router']
@pulumi.input_type
class RouterArgs:
    def __init__(__self__, *, bgp: Optional[pulumi.Input[RouterBgpArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encrypted_interconnect_router: Optional[pulumi.Input[_builtins.bool]] = ..., md5_authentication_keys: Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ncc_gateway: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[RouterParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bgp(self) -> Optional[pulumi.Input[RouterBgpArgs]]:
        
        ...
    
    @bgp.setter
    def bgp(self, value: Optional[pulumi.Input[RouterBgpArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted_interconnect_router.setter
    def encrypted_interconnect_router(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKeys")
    def md5_authentication_keys(self) -> Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]]:
        
        ...
    
    @md5_authentication_keys.setter
    def md5_authentication_keys(self, value: Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nccGateway")
    def ncc_gateway(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ncc_gateway.setter
    def ncc_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RouterParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[RouterParamsArgs]]): # -> None:
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
    


@pulumi.input_type
class _RouterState:
    def __init__(__self__, *, bgp: Optional[pulumi.Input[RouterBgpArgs]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encrypted_interconnect_router: Optional[pulumi.Input[_builtins.bool]] = ..., md5_authentication_keys: Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ncc_gateway: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[RouterParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bgp(self) -> Optional[pulumi.Input[RouterBgpArgs]]:
        
        ...
    
    @bgp.setter
    def bgp(self, value: Optional[pulumi.Input[RouterBgpArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted_interconnect_router.setter
    def encrypted_interconnect_router(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKeys")
    def md5_authentication_keys(self) -> Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]]:
        
        ...
    
    @md5_authentication_keys.setter
    def md5_authentication_keys(self, value: Optional[pulumi.Input[RouterMd5AuthenticationKeysArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nccGateway")
    def ncc_gateway(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ncc_gateway.setter
    def ncc_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RouterParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[RouterParamsArgs]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/router:Router")
class Router(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bgp: Optional[pulumi.Input[Union[RouterBgpArgs, RouterBgpArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encrypted_interconnect_router: Optional[pulumi.Input[_builtins.bool]] = ..., md5_authentication_keys: Optional[pulumi.Input[Union[RouterMd5AuthenticationKeysArgs, RouterMd5AuthenticationKeysArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ncc_gateway: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[RouterParamsArgs, RouterParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[RouterArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bgp: Optional[pulumi.Input[Union[RouterBgpArgs, RouterBgpArgsDict]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encrypted_interconnect_router: Optional[pulumi.Input[_builtins.bool]] = ..., md5_authentication_keys: Optional[pulumi.Input[Union[RouterMd5AuthenticationKeysArgs, RouterMd5AuthenticationKeysArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ncc_gateway: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[RouterParamsArgs, RouterParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> Router:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bgp(self) -> pulumi.Output[Optional[outputs.RouterBgp]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKeys")
    def md5_authentication_keys(self) -> pulumi.Output[Optional[outputs.RouterMd5AuthenticationKeys]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nccGateway")
    def ncc_gateway(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.RouterParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


