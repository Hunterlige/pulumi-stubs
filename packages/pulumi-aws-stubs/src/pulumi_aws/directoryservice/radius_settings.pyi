

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RadiusSettingsArgs', 'RadiusSettings']
@pulumi.input_type
class RadiusSettingsArgs:
    def __init__(__self__, *, authentication_protocol: pulumi.Input[_builtins.str], directory_id: pulumi.Input[_builtins.str], display_label: pulumi.Input[_builtins.str], radius_port: pulumi.Input[_builtins.int], radius_retries: pulumi.Input[_builtins.int], radius_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], radius_timeout: pulumi.Input[_builtins.int], shared_secret: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., use_same_username: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_protocol.setter
    def authentication_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_label.setter
    def display_label(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @radius_port.setter
    def radius_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @radius_retries.setter
    def radius_retries(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @radius_servers.setter
    def radius_servers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @radius_timeout.setter
    def radius_timeout(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @shared_secret.setter
    def shared_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_same_username.setter
    def use_same_username(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _RadiusSettingsState:
    def __init__(__self__, *, authentication_protocol: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., display_label: Optional[pulumi.Input[_builtins.str]] = ..., radius_port: Optional[pulumi.Input[_builtins.int]] = ..., radius_retries: Optional[pulumi.Input[_builtins.int]] = ..., radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., radius_timeout: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_secret: Optional[pulumi.Input[_builtins.str]] = ..., use_same_username: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_protocol.setter
    def authentication_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_label.setter
    def display_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @radius_port.setter
    def radius_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @radius_retries.setter
    def radius_retries(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @radius_servers.setter
    def radius_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @radius_timeout.setter
    def radius_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_same_username.setter
    def use_same_username(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:directoryservice/radiusSettings:RadiusSettings")
class RadiusSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authentication_protocol: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., display_label: Optional[pulumi.Input[_builtins.str]] = ..., radius_port: Optional[pulumi.Input[_builtins.int]] = ..., radius_retries: Optional[pulumi.Input[_builtins.int]] = ..., radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., radius_timeout: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_secret: Optional[pulumi.Input[_builtins.str]] = ..., use_same_username: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RadiusSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authentication_protocol: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., display_label: Optional[pulumi.Input[_builtins.str]] = ..., radius_port: Optional[pulumi.Input[_builtins.int]] = ..., radius_retries: Optional[pulumi.Input[_builtins.int]] = ..., radius_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., radius_timeout: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_secret: Optional[pulumi.Input[_builtins.str]] = ..., use_same_username: Optional[pulumi.Input[_builtins.bool]] = ...) -> RadiusSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


