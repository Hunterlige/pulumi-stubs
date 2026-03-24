

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
__all__ = ['WorkspaceConfigurationArgs', 'WorkspaceConfiguration']
@pulumi.input_type
class WorkspaceConfigurationArgs:
    def __init__(__self__, *, workspace_id: pulumi.Input[_builtins.str], limits_per_label_sets: Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitsPerLabelSets")
    def limits_per_label_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]]:
        
        ...
    
    @limits_per_label_sets.setter
    def limits_per_label_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodInDays")
    def retention_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period_in_days.setter
    def retention_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkspaceConfigurationState:
    def __init__(__self__, *, limits_per_label_sets: Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitsPerLabelSets")
    def limits_per_label_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]]:
        
        ...
    
    @limits_per_label_sets.setter
    def limits_per_label_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodInDays")
    def retention_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period_in_days.setter
    def retention_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[WorkspaceConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkspaceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., limits_per_label_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkspaceConfigurationLimitsPerLabelSetArgs, WorkspaceConfigurationLimitsPerLabelSetArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[Union[WorkspaceConfigurationTimeoutsArgs, WorkspaceConfigurationTimeoutsArgsDict]]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkspaceConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., limits_per_label_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkspaceConfigurationLimitsPerLabelSetArgs, WorkspaceConfigurationLimitsPerLabelSetArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[Union[WorkspaceConfigurationTimeoutsArgs, WorkspaceConfigurationTimeoutsArgsDict]]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkspaceConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitsPerLabelSets")
    def limits_per_label_sets(self) -> pulumi.Output[Optional[Sequence[outputs.WorkspaceConfigurationLimitsPerLabelSet]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodInDays")
    def retention_period_in_days(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.WorkspaceConfigurationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


