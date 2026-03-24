

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, file_shares: pulumi.Input[InstanceFileSharesArgs], networks: pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]], tier: pulumi.Input[_builtins.str], deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_protection_reason: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_replica_state: Optional[pulumi.Input[_builtins.str]] = ..., directory_services: Optional[pulumi.Input[InstanceDirectoryServicesArgs]] = ..., initial_replication: Optional[pulumi.Input[InstanceInitialReplicationArgs]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., performance_config: Optional[pulumi.Input[InstancePerformanceConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> pulumi.Input[InstanceFileSharesArgs]:
        
        ...
    
    @file_shares.setter
    def file_shares(self, value: pulumi.Input[InstanceFileSharesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionReason")
    def deletion_protection_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_protection_reason.setter
    def deletion_protection_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredReplicaState")
    def desired_replica_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_replica_state.setter
    def desired_replica_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServices")
    def directory_services(self) -> Optional[pulumi.Input[InstanceDirectoryServicesArgs]]:
        
        ...
    
    @directory_services.setter
    def directory_services(self, value: Optional[pulumi.Input[InstanceDirectoryServicesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplication")
    def initial_replication(self) -> Optional[pulumi.Input[InstanceInitialReplicationArgs]]:
        
        ...
    
    @initial_replication.setter
    def initial_replication(self, value: Optional[pulumi.Input[InstanceInitialReplicationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> Optional[pulumi.Input[InstancePerformanceConfigArgs]]:
        
        ...
    
    @performance_config.setter
    def performance_config(self, value: Optional[pulumi.Input[InstancePerformanceConfigArgs]]): # -> None:
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
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @_utilities.deprecated(...)
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_protection_reason: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_replica_state: Optional[pulumi.Input[_builtins.str]] = ..., directory_services: Optional[pulumi.Input[InstanceDirectoryServicesArgs]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_replications: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEffectiveReplicationArgs]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., file_shares: Optional[pulumi.Input[InstanceFileSharesArgs]] = ..., initial_replication: Optional[pulumi.Input[InstanceInitialReplicationArgs]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]]] = ..., performance_config: Optional[pulumi.Input[InstancePerformanceConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionReason")
    def deletion_protection_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_protection_reason.setter
    def deletion_protection_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredReplicaState")
    def desired_replica_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_replica_state.setter
    def desired_replica_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServices")
    def directory_services(self) -> Optional[pulumi.Input[InstanceDirectoryServicesArgs]]:
        
        ...
    
    @directory_services.setter
    def directory_services(self, value: Optional[pulumi.Input[InstanceDirectoryServicesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveReplications")
    def effective_replications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEffectiveReplicationArgs]]]]:
        
        ...
    
    @effective_replications.setter
    def effective_replications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEffectiveReplicationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> Optional[pulumi.Input[InstanceFileSharesArgs]]:
        
        ...
    
    @file_shares.setter
    def file_shares(self, value: Optional[pulumi.Input[InstanceFileSharesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplication")
    def initial_replication(self) -> Optional[pulumi.Input[InstanceInitialReplicationArgs]]:
        
        ...
    
    @initial_replication.setter
    def initial_replication(self, value: Optional[pulumi.Input[InstanceInitialReplicationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> Optional[pulumi.Input[InstancePerformanceConfigArgs]]:
        
        ...
    
    @performance_config.setter
    def performance_config(self, value: Optional[pulumi.Input[InstancePerformanceConfigArgs]]): # -> None:
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
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:filestore/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_protection_reason: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_replica_state: Optional[pulumi.Input[_builtins.str]] = ..., directory_services: Optional[pulumi.Input[Union[InstanceDirectoryServicesArgs, InstanceDirectoryServicesArgsDict]]] = ..., file_shares: Optional[pulumi.Input[Union[InstanceFileSharesArgs, InstanceFileSharesArgsDict]]] = ..., initial_replication: Optional[pulumi.Input[Union[InstanceInitialReplicationArgs, InstanceInitialReplicationArgsDict]]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceNetworkArgs, InstanceNetworkArgsDict]]]]] = ..., performance_config: Optional[pulumi.Input[Union[InstancePerformanceConfigArgs, InstancePerformanceConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_protection_reason: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_replica_state: Optional[pulumi.Input[_builtins.str]] = ..., directory_services: Optional[pulumi.Input[Union[InstanceDirectoryServicesArgs, InstanceDirectoryServicesArgsDict]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_replications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceEffectiveReplicationArgs, InstanceEffectiveReplicationArgsDict]]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., file_shares: Optional[pulumi.Input[Union[InstanceFileSharesArgs, InstanceFileSharesArgsDict]]] = ..., initial_replication: Optional[pulumi.Input[Union[InstanceInitialReplicationArgs, InstanceInitialReplicationArgsDict]]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceNetworkArgs, InstanceNetworkArgsDict]]]]] = ..., performance_config: Optional[pulumi.Input[Union[InstancePerformanceConfigArgs, InstancePerformanceConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionReason")
    def deletion_protection_reason(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredReplicaState")
    def desired_replica_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServices")
    def directory_services(self) -> pulumi.Output[Optional[outputs.InstanceDirectoryServices]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveReplications")
    def effective_replications(self) -> pulumi.Output[Sequence[outputs.InstanceEffectiveReplication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> pulumi.Output[outputs.InstanceFileShares]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplication")
    def initial_replication(self) -> pulumi.Output[Optional[outputs.InstanceInitialReplication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def networks(self) -> pulumi.Output[Sequence[outputs.InstanceNetwork]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> pulumi.Output[Optional[outputs.InstancePerformanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


