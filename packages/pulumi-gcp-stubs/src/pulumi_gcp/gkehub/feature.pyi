

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FeatureArgs', 'Feature']
@pulumi.input_type
class FeatureArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], fleet_default_member_config: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[FeatureSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetDefaultMemberConfig")
    def fleet_default_member_config(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]]:
        
        ...
    
    @fleet_default_member_config.setter
    def fleet_default_member_config(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def spec(self) -> Optional[pulumi.Input[FeatureSpecArgs]]:
        
        ...
    
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[FeatureSpecArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FeatureState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fleet_default_member_config: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_states: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureResourceStateArgs]]]] = ..., spec: Optional[pulumi.Input[FeatureSpecArgs]] = ..., states: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetDefaultMemberConfig")
    def fleet_default_member_config(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]]:
        
        ...
    
    @fleet_default_member_config.setter
    def fleet_default_member_config(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStates")
    def resource_states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureResourceStateArgs]]]]:
        
        ...
    
    @resource_states.setter
    def resource_states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureResourceStateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[FeatureSpecArgs]]:
        
        ...
    
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[FeatureSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateArgs]]]]:
        
        ...
    
    @states.setter
    def states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:gkehub/feature:Feature")
class Feature(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., fleet_default_member_config: Optional[pulumi.Input[Union[FeatureFleetDefaultMemberConfigArgs, FeatureFleetDefaultMemberConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[Union[FeatureSpecArgs, FeatureSpecArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FeatureArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fleet_default_member_config: Optional[pulumi.Input[Union[FeatureFleetDefaultMemberConfigArgs, FeatureFleetDefaultMemberConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_states: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FeatureResourceStateArgs, FeatureResourceStateArgsDict]]]]] = ..., spec: Optional[pulumi.Input[Union[FeatureSpecArgs, FeatureSpecArgsDict]]] = ..., states: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FeatureStateArgs, FeatureStateArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Feature:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetDefaultMemberConfig")
    def fleet_default_member_config(self) -> pulumi.Output[Optional[outputs.FeatureFleetDefaultMemberConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStates")
    def resource_states(self) -> pulumi.Output[Sequence[outputs.FeatureResourceState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional[outputs.FeatureSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> pulumi.Output[Sequence[outputs.FeatureState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


