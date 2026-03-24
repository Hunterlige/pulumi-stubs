

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MachineGroupArgs', 'MachineGroup']
@pulumi.input_type
class MachineGroupArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], count: Optional[pulumi.Input[_builtins.int]] = ..., group_type: Optional[pulumi.Input[Union[_builtins.str, MachineGroupType]]] = ..., machine_group_name: Optional[pulumi.Input[_builtins.str]] = ..., machines: Optional[pulumi.Input[Sequence[pulumi.Input[MachineReferenceWithHintsArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[Union[_builtins.str, MachineGroupType]]]:
        
        ...
    
    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[Union[_builtins.str, MachineGroupType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineGroupName")
    def machine_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_group_name.setter
    def machine_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def machines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MachineReferenceWithHintsArgs]]]]:
        
        ...
    
    @machines.setter
    def machines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MachineReferenceWithHintsArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:operationalinsights:MachineGroup")
class MachineGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., count: Optional[pulumi.Input[_builtins.int]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., group_type: Optional[pulumi.Input[Union[_builtins.str, MachineGroupType]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., machine_group_name: Optional[pulumi.Input[_builtins.str]] = ..., machines: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MachineReferenceWithHintsArgs, MachineReferenceWithHintsArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MachineGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MachineGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def machines(self) -> pulumi.Output[Optional[Sequence[outputs.MachineReferenceWithHintsResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


