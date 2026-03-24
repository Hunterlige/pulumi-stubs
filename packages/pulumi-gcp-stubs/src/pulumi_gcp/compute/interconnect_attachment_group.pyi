

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
__all__ = ['InterconnectAttachmentGroupArgs', 'InterconnectAttachmentGroup']
@pulumi.input_type
class InterconnectAttachmentGroupArgs:
    def __init__(__self__, *, intent: pulumi.Input[InterconnectAttachmentGroupIntentArgs], attachments: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., interconnect_group: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> pulumi.Input[InterconnectAttachmentGroupIntentArgs]:
        
        ...
    
    @intent.setter
    def intent(self, value: pulumi.Input[InterconnectAttachmentGroupIntentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]]:
        
        ...
    
    @attachments.setter
    def attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectGroup")
    def interconnect_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interconnect_group.setter
    def interconnect_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _InterconnectAttachmentGroupState:
    def __init__(__self__, *, attachments: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]] = ..., configureds: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupConfiguredArgs]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[InterconnectAttachmentGroupIntentArgs]] = ..., interconnect_group: Optional[pulumi.Input[_builtins.str]] = ..., logical_structures: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupLogicalStructureArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]]:
        
        ...
    
    @attachments.setter
    def attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configureds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupConfiguredArgs]]]]:
        
        ...
    
    @configureds.setter
    def configureds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupConfiguredArgs]]]]): # -> None:
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
    def intent(self) -> Optional[pulumi.Input[InterconnectAttachmentGroupIntentArgs]]:
        
        ...
    
    @intent.setter
    def intent(self, value: Optional[pulumi.Input[InterconnectAttachmentGroupIntentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectGroup")
    def interconnect_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interconnect_group.setter
    def interconnect_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalStructures")
    def logical_structures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupLogicalStructureArgs]]]]:
        
        ...
    
    @logical_structures.setter
    def logical_structures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentGroupLogicalStructureArgs]]]]): # -> None:
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
    


@pulumi.type_token(...)
class InterconnectAttachmentGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attachments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectAttachmentGroupAttachmentArgs, InterconnectAttachmentGroupAttachmentArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[Union[InterconnectAttachmentGroupIntentArgs, InterconnectAttachmentGroupIntentArgsDict]]] = ..., interconnect_group: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InterconnectAttachmentGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attachments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectAttachmentGroupAttachmentArgs, InterconnectAttachmentGroupAttachmentArgsDict]]]]] = ..., configureds: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectAttachmentGroupConfiguredArgs, InterconnectAttachmentGroupConfiguredArgsDict]]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[Union[InterconnectAttachmentGroupIntentArgs, InterconnectAttachmentGroupIntentArgsDict]]] = ..., interconnect_group: Optional[pulumi.Input[_builtins.str]] = ..., logical_structures: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectAttachmentGroupLogicalStructureArgs, InterconnectAttachmentGroupLogicalStructureArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> InterconnectAttachmentGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> pulumi.Output[Optional[Sequence[outputs.InterconnectAttachmentGroupAttachment]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configureds(self) -> pulumi.Output[Sequence[outputs.InterconnectAttachmentGroupConfigured]]:
        
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
    def intent(self) -> pulumi.Output[outputs.InterconnectAttachmentGroupIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectGroup")
    def interconnect_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalStructures")
    def logical_structures(self) -> pulumi.Output[Sequence[outputs.InterconnectAttachmentGroupLogicalStructure]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


