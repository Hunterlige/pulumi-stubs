

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
__all__ = ['TriggerArgs', 'Trigger']
@pulumi.input_type
class TriggerArgs:
    def __init__(__self__, *, repository_name: pulumi.Input[_builtins.str], triggers: pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TriggerState:
    def __init__(__self__, *, configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_id.setter
    def configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerTriggerArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:codecommit/trigger:Trigger")
class Trigger(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerTriggerArgs, TriggerTriggerArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TriggerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerTriggerArgs, TriggerTriggerArgsDict]]]]] = ...) -> Trigger:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Sequence[outputs.TriggerTrigger]]:
        
        ...
    


