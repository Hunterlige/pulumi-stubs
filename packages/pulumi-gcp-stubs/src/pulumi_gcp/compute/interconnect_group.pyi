

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
__all__ = ['InterconnectGroupArgs', 'InterconnectGroup']
@pulumi.input_type
class InterconnectGroupArgs:
    def __init__(__self__, *, intent: pulumi.Input[InterconnectGroupIntentArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., interconnects: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> pulumi.Input[InterconnectGroupIntentArgs]:
        
        ...
    
    @intent.setter
    def intent(self, value: pulumi.Input[InterconnectGroupIntentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]]:
        
        ...
    
    @interconnects.setter
    def interconnects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]]): # -> None:
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
class _InterconnectGroupState:
    def __init__(__self__, *, configureds: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupConfiguredArgs]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[InterconnectGroupIntentArgs]] = ..., interconnects: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_structures: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupPhysicalStructureArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configureds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupConfiguredArgs]]]]:
        
        ...
    
    @configureds.setter
    def configureds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupConfiguredArgs]]]]): # -> None:
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
    @pulumi.getter
    def intent(self) -> Optional[pulumi.Input[InterconnectGroupIntentArgs]]:
        
        ...
    
    @intent.setter
    def intent(self, value: Optional[pulumi.Input[InterconnectGroupIntentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]]:
        
        ...
    
    @interconnects.setter
    def interconnects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupInterconnectArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalStructures")
    def physical_structures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupPhysicalStructureArgs]]]]:
        
        ...
    
    @physical_structures.setter
    def physical_structures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectGroupPhysicalStructureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/interconnectGroup:InterconnectGroup")
class InterconnectGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[Union[InterconnectGroupIntentArgs, InterconnectGroupIntentArgsDict]]] = ..., interconnects: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectGroupInterconnectArgs, InterconnectGroupInterconnectArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InterconnectGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configureds: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectGroupConfiguredArgs, InterconnectGroupConfiguredArgsDict]]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[Union[InterconnectGroupIntentArgs, InterconnectGroupIntentArgsDict]]] = ..., interconnects: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectGroupInterconnectArgs, InterconnectGroupInterconnectArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_structures: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectGroupPhysicalStructureArgs, InterconnectGroupPhysicalStructureArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> InterconnectGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configureds(self) -> pulumi.Output[Sequence[outputs.InterconnectGroupConfigured]]:
        
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
    @pulumi.getter
    def intent(self) -> pulumi.Output[outputs.InterconnectGroupIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnects(self) -> pulumi.Output[Optional[Sequence[outputs.InterconnectGroupInterconnect]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalStructures")
    def physical_structures(self) -> pulumi.Output[Sequence[outputs.InterconnectGroupPhysicalStructure]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


