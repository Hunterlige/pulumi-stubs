

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
__all__ = ['EkmConnectionArgs', 'EkmConnection']
@pulumi.input_type
class EkmConnectionArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], service_resolvers: pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]], crypto_space_path: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., key_management_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResolvers")
    def service_resolvers(self) -> pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]]:
        
        ...
    
    @service_resolvers.setter
    def service_resolvers(self, value: pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoSpacePath")
    def crypto_space_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crypto_space_path.setter
    def crypto_space_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementMode")
    def key_management_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_management_mode.setter
    def key_management_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _EkmConnectionState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., crypto_space_path: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., key_management_mode: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoSpacePath")
    def crypto_space_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crypto_space_path.setter
    def crypto_space_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementMode")
    def key_management_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_management_mode.setter
    def key_management_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="serviceResolvers")
    def service_resolvers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]]]:
        
        ...
    
    @service_resolvers.setter
    def service_resolvers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EkmConnectionServiceResolverArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:kms/ekmConnection:EkmConnection")
class EkmConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., crypto_space_path: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., key_management_mode: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EkmConnectionServiceResolverArgs, EkmConnectionServiceResolverArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EkmConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., crypto_space_path: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., key_management_mode: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service_resolvers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EkmConnectionServiceResolverArgs, EkmConnectionServiceResolverArgsDict]]]]] = ...) -> EkmConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoSpacePath")
    def crypto_space_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementMode")
    def key_management_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="serviceResolvers")
    def service_resolvers(self) -> pulumi.Output[Sequence[outputs.EkmConnectionServiceResolver]]:
        
        ...
    


