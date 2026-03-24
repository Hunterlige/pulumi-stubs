

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
__all__ = ['RulesetArgs', 'Ruleset']
@pulumi.input_type
class RulesetArgs:
    def __init__(__self__, *, source: pulumi.Input[RulesetSourceArgs], project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[RulesetSourceArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[RulesetSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RulesetState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[RulesetMetadataArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[RulesetSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RulesetMetadataArgs]]]]:
        
        ...
    
    @metadatas.setter
    def metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RulesetMetadataArgs]]]]): # -> None:
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
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[RulesetSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[RulesetSourceArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firebaserules/ruleset:Ruleset")
class Ruleset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[RulesetSourceArgs, RulesetSourceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RulesetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RulesetMetadataArgs, RulesetMetadataArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[RulesetSourceArgs, RulesetSourceArgsDict]]] = ...) -> Ruleset:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> pulumi.Output[Sequence[outputs.RulesetMetadata]]:
        
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
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.RulesetSource]:
        
        ...
    


