

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
__all__ = ['ManagementServerArgs', 'ManagementServer']
@pulumi.input_type
class ManagementServerArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ManagementServerState:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., management_uris: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerManagementUriArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]] = ..., oauth2_client_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementUris")
    def management_uris(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerManagementUriArgs]]]]:
        
        ...
    
    @management_uris.setter
    def management_uris(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerManagementUriArgs]]]]): # -> None:
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
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementServerNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oauth2_client_id.setter
    def oauth2_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagementServer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagementServerNetworkArgs, ManagementServerNetworkArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagementServerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_uris: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagementServerManagementUriArgs, ManagementServerManagementUriArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagementServerNetworkArgs, ManagementServerNetworkArgsDict]]]]] = ..., oauth2_client_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> ManagementServer:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementUris")
    def management_uris(self) -> pulumi.Output[Sequence[outputs.ManagementServerManagementUri]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence[outputs.ManagementServerNetwork]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


