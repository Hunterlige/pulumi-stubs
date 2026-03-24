

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
__all__ = ['VolumeReplicationArgs', 'VolumeReplication']
@pulumi.input_type
class VolumeReplicationArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], replication_schedule: pulumi.Input[_builtins.str], volume_name: pulumi.Input[_builtins.str], delete_destination_volume: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume_parameters: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]] = ..., force_stopping: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_mirror: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replication_schedule.setter
    def replication_schedule(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteDestinationVolume")
    def delete_destination_volume(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_destination_volume.setter
    def delete_destination_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVolumeParameters")
    def destination_volume_parameters(self) -> Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]]:
        
        ...
    
    @destination_volume_parameters.setter
    def destination_volume_parameters(self, value: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStopping")
    def force_stopping(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_stopping.setter
    def force_stopping(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="replicationEnabled")
    def replication_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replication_enabled.setter
    def replication_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForMirror")
    def wait_for_mirror(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_mirror.setter
    def wait_for_mirror(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _VolumeReplicationState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_destination_volume: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume_parameters: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_stopping: Optional[pulumi.Input[_builtins.bool]] = ..., healthy: Optional[pulumi.Input[_builtins.bool]] = ..., hybrid_peering_details: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridPeeringDetailArgs]]]] = ..., hybrid_replication_type: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_replication_user_commands: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridReplicationUserCommandArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mirror_state: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., replication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., replication_schedule: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., source_volume: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., transfer_stats: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationTransferStatArgs]]]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_mirror: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteDestinationVolume")
    def delete_destination_volume(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_destination_volume.setter
    def delete_destination_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVolume")
    def destination_volume(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_volume.setter
    def destination_volume(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVolumeParameters")
    def destination_volume_parameters(self) -> Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]]:
        
        ...
    
    @destination_volume_parameters.setter
    def destination_volume_parameters(self, value: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStopping")
    def force_stopping(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_stopping.setter
    def force_stopping(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def healthy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @healthy.setter
    def healthy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridPeeringDetails")
    def hybrid_peering_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridPeeringDetailArgs]]]]:
        
        ...
    
    @hybrid_peering_details.setter
    def hybrid_peering_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridPeeringDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationType")
    def hybrid_replication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hybrid_replication_type.setter
    def hybrid_replication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationUserCommands")
    def hybrid_replication_user_commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridReplicationUserCommandArgs]]]]:
        
        ...
    
    @hybrid_replication_user_commands.setter
    def hybrid_replication_user_commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationHybridReplicationUserCommandArgs]]]]): # -> None:
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
    @pulumi.getter(name="mirrorState")
    def mirror_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mirror_state.setter
    def mirror_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="replicationEnabled")
    def replication_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replication_enabled.setter
    def replication_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_schedule.setter
    def replication_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVolume")
    def source_volume(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_volume.setter
    def source_volume(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_details.setter
    def state_details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferStats")
    def transfer_stats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationTransferStatArgs]]]]:
        
        ...
    
    @transfer_stats.setter
    def transfer_stats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReplicationTransferStatArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForMirror")
    def wait_for_mirror(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_mirror.setter
    def wait_for_mirror(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("gcp:netapp/volumeReplication:VolumeReplication")
class VolumeReplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delete_destination_volume: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume_parameters: Optional[pulumi.Input[Union[VolumeReplicationDestinationVolumeParametersArgs, VolumeReplicationDestinationVolumeParametersArgsDict]]] = ..., force_stopping: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., replication_schedule: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_mirror: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VolumeReplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_destination_volume: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume: Optional[pulumi.Input[_builtins.str]] = ..., destination_volume_parameters: Optional[pulumi.Input[Union[VolumeReplicationDestinationVolumeParametersArgs, VolumeReplicationDestinationVolumeParametersArgsDict]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_stopping: Optional[pulumi.Input[_builtins.bool]] = ..., healthy: Optional[pulumi.Input[_builtins.bool]] = ..., hybrid_peering_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeReplicationHybridPeeringDetailArgs, VolumeReplicationHybridPeeringDetailArgsDict]]]]] = ..., hybrid_replication_type: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_replication_user_commands: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeReplicationHybridReplicationUserCommandArgs, VolumeReplicationHybridReplicationUserCommandArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mirror_state: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., replication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., replication_schedule: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., source_volume: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., transfer_stats: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeReplicationTransferStatArgs, VolumeReplicationTransferStatArgsDict]]]]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_mirror: Optional[pulumi.Input[_builtins.bool]] = ...) -> VolumeReplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteDestinationVolume")
    def delete_destination_volume(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVolume")
    def destination_volume(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVolumeParameters")
    def destination_volume_parameters(self) -> pulumi.Output[Optional[outputs.VolumeReplicationDestinationVolumeParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStopping")
    def force_stopping(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def healthy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridPeeringDetails")
    def hybrid_peering_details(self) -> pulumi.Output[Sequence[outputs.VolumeReplicationHybridPeeringDetail]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationType")
    def hybrid_replication_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationUserCommands")
    def hybrid_replication_user_commands(self) -> pulumi.Output[Sequence[outputs.VolumeReplicationHybridReplicationUserCommand]]:
        
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
    @pulumi.getter(name="mirrorState")
    def mirror_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="replicationEnabled")
    def replication_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVolume")
    def source_volume(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferStats")
    def transfer_stats(self) -> pulumi.Output[Sequence[outputs.VolumeReplicationTransferStat]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForMirror")
    def wait_for_mirror(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


