import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OntapVolumeArgs", "OntapVolume"]

@pulumi.input_type
class OntapVolumeArgs:
    def __init__(
        __self__,
        *,
        storage_virtual_machine_id: pulumi.Input[_builtins.str],
        aggregate_configuration: Optional[
            pulumi.Input[OntapVolumeAggregateConfigurationArgs]
        ] = ...,
        bypass_snaplock_enterprise_retention: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        junction_path: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ontap_volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        snaplock_configuration: Optional[
            pulumi.Input[OntapVolumeSnaplockConfigurationArgs]
        ] = ...,
        snapshot_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_efficiency_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tiering_policy: Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]] = ...,
        volume_style: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageVirtualMachineId")
    def storage_virtual_machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_virtual_machine_id.setter
    def storage_virtual_machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aggregateConfiguration")
    def aggregate_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeAggregateConfigurationArgs]]: ...
    @aggregate_configuration.setter
    def aggregate_configuration(
        self, value: Optional[pulumi.Input[OntapVolumeAggregateConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bypassSnaplockEnterpriseRetention")
    def bypass_snaplock_enterprise_retention(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_snaplock_enterprise_retention.setter
    def bypass_snaplock_enterprise_retention(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @final_backup_tags.setter
    def final_backup_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="junctionPath")
    def junction_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @junction_path.setter
    def junction_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ontapVolumeType")
    def ontap_volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ontap_volume_type.setter
    def ontap_volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_in_bytes.setter
    def size_in_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInMegabytes")
    def size_in_megabytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_in_megabytes.setter
    def size_in_megabytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_backup.setter
    def skip_final_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snaplockConfiguration")
    def snaplock_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationArgs]]: ...
    @snaplock_configuration.setter
    def snaplock_configuration(
        self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_policy.setter
    def snapshot_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEfficiencyEnabled")
    def storage_efficiency_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_efficiency_enabled.setter
    def storage_efficiency_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]]: ...
    @tiering_policy.setter
    def tiering_policy(
        self, value: Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeStyle")
    def volume_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_style.setter
    def volume_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OntapVolumeState:
    def __init__(
        __self__,
        *,
        aggregate_configuration: Optional[
            pulumi.Input[OntapVolumeAggregateConfigurationArgs]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bypass_snaplock_enterprise_retention: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        flexcache_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        junction_path: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ontap_volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        snaplock_configuration: Optional[
            pulumi.Input[OntapVolumeSnaplockConfigurationArgs]
        ] = ...,
        snapshot_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_efficiency_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tiering_policy: Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_style: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregateConfiguration")
    def aggregate_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeAggregateConfigurationArgs]]: ...
    @aggregate_configuration.setter
    def aggregate_configuration(
        self, value: Optional[pulumi.Input[OntapVolumeAggregateConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bypassSnaplockEnterpriseRetention")
    def bypass_snaplock_enterprise_retention(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_snaplock_enterprise_retention.setter
    def bypass_snaplock_enterprise_retention(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @final_backup_tags.setter
    def final_backup_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flexcacheEndpointType")
    def flexcache_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flexcache_endpoint_type.setter
    def flexcache_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="junctionPath")
    def junction_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @junction_path.setter
    def junction_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ontapVolumeType")
    def ontap_volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ontap_volume_type.setter
    def ontap_volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_in_bytes.setter
    def size_in_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInMegabytes")
    def size_in_megabytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_in_megabytes.setter
    def size_in_megabytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_backup.setter
    def skip_final_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snaplockConfiguration")
    def snaplock_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationArgs]]: ...
    @snaplock_configuration.setter
    def snaplock_configuration(
        self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_policy.setter
    def snapshot_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEfficiencyEnabled")
    def storage_efficiency_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_efficiency_enabled.setter
    def storage_efficiency_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageVirtualMachineId")
    def storage_virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_virtual_machine_id.setter
    def storage_virtual_machine_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]]: ...
    @tiering_policy.setter
    def tiering_policy(
        self, value: Optional[pulumi.Input[OntapVolumeTieringPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeStyle")
    def volume_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_style.setter
    def volume_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:fsx/ontapVolume:OntapVolume")
class OntapVolume(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aggregate_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapVolumeAggregateConfigurationArgs,
                    OntapVolumeAggregateConfigurationArgsDict,
                ]
            ]
        ] = ...,
        bypass_snaplock_enterprise_retention: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        junction_path: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ontap_volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        snaplock_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapVolumeSnaplockConfigurationArgs,
                    OntapVolumeSnaplockConfigurationArgsDict,
                ]
            ]
        ] = ...,
        snapshot_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_efficiency_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tiering_policy: Optional[
            pulumi.Input[
                Union[OntapVolumeTieringPolicyArgs, OntapVolumeTieringPolicyArgsDict]
            ]
        ] = ...,
        volume_style: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OntapVolumeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aggregate_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapVolumeAggregateConfigurationArgs,
                    OntapVolumeAggregateConfigurationArgsDict,
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bypass_snaplock_enterprise_retention: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        flexcache_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        junction_path: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ontap_volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        snaplock_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapVolumeSnaplockConfigurationArgs,
                    OntapVolumeSnaplockConfigurationArgsDict,
                ]
            ]
        ] = ...,
        snapshot_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_efficiency_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tiering_policy: Optional[
            pulumi.Input[
                Union[OntapVolumeTieringPolicyArgs, OntapVolumeTieringPolicyArgsDict]
            ]
        ] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_style: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OntapVolume: ...
    @_builtins.property
    @pulumi.getter(name="aggregateConfiguration")
    def aggregate_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.OntapVolumeAggregateConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bypassSnaplockEnterpriseRetention")
    def bypass_snaplock_enterprise_retention(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="flexcacheEndpointType")
    def flexcache_endpoint_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="junctionPath")
    def junction_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ontapVolumeType")
    def ontap_volume_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInMegabytes")
    def size_in_megabytes(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snaplockConfiguration")
    def snaplock_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.OntapVolumeSnaplockConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEfficiencyEnabled")
    def storage_efficiency_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="storageVirtualMachineId")
    def storage_virtual_machine_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.OntapVolumeTieringPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeStyle")
    def volume_style(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
