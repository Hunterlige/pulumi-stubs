

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RestorePlanArgs', 'RestorePlan']
@pulumi.input_type
class RestorePlanArgs:
    def __init__(__self__, *, backup_plan: pulumi.Input[_builtins.str], cluster: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], restore_config: pulumi.Input[RestorePlanRestoreConfigArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_plan.setter
    def backup_plan(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreConfig")
    def restore_config(self) -> pulumi.Input[RestorePlanRestoreConfigArgs]:
        
        ...
    
    @restore_config.setter
    def restore_config(self, value: pulumi.Input[RestorePlanRestoreConfigArgs]): # -> None:
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
    


@pulumi.input_type
class _RestorePlanState:
    def __init__(__self__, *, backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., restore_config: Optional[pulumi.Input[RestorePlanRestoreConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_reason: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_plan.setter
    def backup_plan(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="restoreConfig")
    def restore_config(self) -> Optional[pulumi.Input[RestorePlanRestoreConfigArgs]]:
        
        ...
    
    @restore_config.setter
    def restore_config(self, value: Optional[pulumi.Input[RestorePlanRestoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_reason.setter
    def state_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:gkebackup/restorePlan:RestorePlan")
class RestorePlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., restore_config: Optional[pulumi.Input[Union[RestorePlanRestoreConfigArgs, RestorePlanRestoreConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RestorePlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., restore_config: Optional[pulumi.Input[Union[RestorePlanRestoreConfigArgs, RestorePlanRestoreConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_reason: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> RestorePlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
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
    @pulumi.getter(name="restoreConfig")
    def restore_config(self) -> pulumi.Output[outputs.RestorePlanRestoreConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


