

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TargetArgs', 'Target']
@pulumi.input_type
class TargetArgs:
    def __init__(__self__, *, extended_location: pulumi.Input[ExtendedLocationArgs], resource_group_name: pulumi.Input[_builtins.str], components: Optional[pulumi.Input[Sequence[pulumi.Input[ComponentPropertiesArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., reconciliation_policy: Optional[pulumi.Input[ReconciliationPolicyArgs]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topologies: Optional[pulumi.Input[Sequence[pulumi.Input[TopologiesPropertiesArgs]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ComponentPropertiesArgs]]]]:
        
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ComponentPropertiesArgs]]]]): # -> None:
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
    @pulumi.getter(name="reconciliationPolicy")
    def reconciliation_policy(self) -> Optional[pulumi.Input[ReconciliationPolicyArgs]]:
        
        ...
    
    @reconciliation_policy.setter
    def reconciliation_policy(self, value: Optional[pulumi.Input[ReconciliationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topologies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopologiesPropertiesArgs]]]]:
        
        ...
    
    @topologies.setter
    def topologies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TopologiesPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotoperationsorchestrator:Target")
class Target(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ComponentPropertiesArgs, ComponentPropertiesArgsDict]]]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., reconciliation_policy: Optional[pulumi.Input[Union[ReconciliationPolicyArgs, ReconciliationPolicyArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topologies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TopologiesPropertiesArgs, TopologiesPropertiesArgsDict]]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TargetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Target:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Output[Optional[Sequence[outputs.ComponentPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconciliationPolicy")
    def reconciliation_policy(self) -> pulumi.Output[Optional[outputs.ReconciliationPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topologies(self) -> pulumi.Output[Optional[Sequence[outputs.TopologiesPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


