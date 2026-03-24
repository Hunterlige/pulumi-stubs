

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
__all__ = ['IndexingConfigurationArgs', 'IndexingConfiguration']
@pulumi.input_type
class IndexingConfigurationArgs:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_indexing_configuration: Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]] = ..., thing_indexing_configuration: Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupIndexingConfiguration")
    def thing_group_indexing_configuration(self) -> Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]]:
        
        ...
    
    @thing_group_indexing_configuration.setter
    def thing_group_indexing_configuration(self, value: Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingIndexingConfiguration")
    def thing_indexing_configuration(self) -> Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]]:
        
        ...
    
    @thing_indexing_configuration.setter
    def thing_indexing_configuration(self, value: Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _IndexingConfigurationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_indexing_configuration: Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]] = ..., thing_indexing_configuration: Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupIndexingConfiguration")
    def thing_group_indexing_configuration(self) -> Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]]:
        
        ...
    
    @thing_group_indexing_configuration.setter
    def thing_group_indexing_configuration(self, value: Optional[pulumi.Input[IndexingConfigurationThingGroupIndexingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingIndexingConfiguration")
    def thing_indexing_configuration(self) -> Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]]:
        
        ...
    
    @thing_indexing_configuration.setter
    def thing_indexing_configuration(self, value: Optional[pulumi.Input[IndexingConfigurationThingIndexingConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IndexingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_indexing_configuration: Optional[pulumi.Input[Union[IndexingConfigurationThingGroupIndexingConfigurationArgs, IndexingConfigurationThingGroupIndexingConfigurationArgsDict]]] = ..., thing_indexing_configuration: Optional[pulumi.Input[Union[IndexingConfigurationThingIndexingConfigurationArgs, IndexingConfigurationThingIndexingConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[IndexingConfigurationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thing_group_indexing_configuration: Optional[pulumi.Input[Union[IndexingConfigurationThingGroupIndexingConfigurationArgs, IndexingConfigurationThingGroupIndexingConfigurationArgsDict]]] = ..., thing_indexing_configuration: Optional[pulumi.Input[Union[IndexingConfigurationThingIndexingConfigurationArgs, IndexingConfigurationThingIndexingConfigurationArgsDict]]] = ...) -> IndexingConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingGroupIndexingConfiguration")
    def thing_group_indexing_configuration(self) -> pulumi.Output[outputs.IndexingConfigurationThingGroupIndexingConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thingIndexingConfiguration")
    def thing_indexing_configuration(self) -> pulumi.Output[outputs.IndexingConfigurationThingIndexingConfiguration]:
        
        ...
    


