

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
__all__ = ['BackupPlanArgs', 'BackupPlan']
@pulumi.input_type
class BackupPlanArgs:
    def __init__(__self__, *, cluster: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], backup_config: Optional[pulumi.Input[BackupPlanBackupConfigArgs]] = ..., backup_schedule: Optional[pulumi.Input[BackupPlanBackupScheduleArgs]] = ..., deactivated: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., retention_policy: Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> Optional[pulumi.Input[BackupPlanBackupConfigArgs]]:
        
        ...
    
    @backup_config.setter
    def backup_config(self, value: Optional[pulumi.Input[BackupPlanBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> Optional[pulumi.Input[BackupPlanBackupScheduleArgs]]:
        
        ...
    
    @backup_schedule.setter
    def backup_schedule(self, value: Optional[pulumi.Input[BackupPlanBackupScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deactivated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deactivated.setter
    def deactivated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]]:
        
        ...
    
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BackupPlanState:
    def __init__(__self__, *, backup_config: Optional[pulumi.Input[BackupPlanBackupConfigArgs]] = ..., backup_schedule: Optional[pulumi.Input[BackupPlanBackupScheduleArgs]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deactivated: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protected_namespace_count: Optional[pulumi.Input[_builtins.int]] = ..., protected_pod_count: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., retention_policy: Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_reason: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> Optional[pulumi.Input[BackupPlanBackupConfigArgs]]:
        
        ...
    
    @backup_config.setter
    def backup_config(self, value: Optional[pulumi.Input[BackupPlanBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> Optional[pulumi.Input[BackupPlanBackupScheduleArgs]]:
        
        ...
    
    @backup_schedule.setter
    def backup_schedule(self, value: Optional[pulumi.Input[BackupPlanBackupScheduleArgs]]): # -> None:
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
    def deactivated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deactivated.setter
    def deactivated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="protectedNamespaceCount")
    def protected_namespace_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @protected_namespace_count.setter
    def protected_namespace_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedPodCount")
    def protected_pod_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @protected_pod_count.setter
    def protected_pod_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]]:
        
        ...
    
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[BackupPlanRetentionPolicyArgs]]): # -> None:
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
    


@pulumi.type_token("gcp:gkebackup/backupPlan:BackupPlan")
class BackupPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_config: Optional[pulumi.Input[Union[BackupPlanBackupConfigArgs, BackupPlanBackupConfigArgsDict]]] = ..., backup_schedule: Optional[pulumi.Input[Union[BackupPlanBackupScheduleArgs, BackupPlanBackupScheduleArgsDict]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deactivated: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., retention_policy: Optional[pulumi.Input[Union[BackupPlanRetentionPolicyArgs, BackupPlanRetentionPolicyArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BackupPlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_config: Optional[pulumi.Input[Union[BackupPlanBackupConfigArgs, BackupPlanBackupConfigArgsDict]]] = ..., backup_schedule: Optional[pulumi.Input[Union[BackupPlanBackupScheduleArgs, BackupPlanBackupScheduleArgsDict]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deactivated: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protected_namespace_count: Optional[pulumi.Input[_builtins.int]] = ..., protected_pod_count: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., retention_policy: Optional[pulumi.Input[Union[BackupPlanRetentionPolicyArgs, BackupPlanRetentionPolicyArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_reason: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> BackupPlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> pulumi.Output[Optional[outputs.BackupPlanBackupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> pulumi.Output[Optional[outputs.BackupPlanBackupSchedule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deactivated(self) -> pulumi.Output[_builtins.bool]:
        
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
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="protectedNamespaceCount")
    def protected_namespace_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedPodCount")
    def protected_pod_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Output[Optional[outputs.BackupPlanRetentionPolicy]]:
        
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
    


