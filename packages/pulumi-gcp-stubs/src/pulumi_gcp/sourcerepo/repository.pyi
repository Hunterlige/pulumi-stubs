

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
__all__ = ['RepositoryArgs', 'Repository']
@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *, create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_configs: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_ignore_already_exists.setter
    def create_ignore_already_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]]:
        
        ...
    
    @pubsub_configs.setter
    def pubsub_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _RepositoryState:
    def __init__(__self__, *, create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_configs: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_ignore_already_exists.setter
    def create_ignore_already_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]]:
        
        ...
    
    @pubsub_configs.setter
    def pubsub_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryPubsubConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:sourcerepo/repository:Repository")
class Repository(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RepositoryPubsubConfigArgs, RepositoryPubsubConfigArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[RepositoryArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RepositoryPubsubConfigArgs, RepositoryPubsubConfigArgsDict]]]]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> Repository:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> pulumi.Output[Optional[Sequence[outputs.RepositoryPubsubConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


