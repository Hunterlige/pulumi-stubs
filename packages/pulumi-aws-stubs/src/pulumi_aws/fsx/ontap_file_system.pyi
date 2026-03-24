import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OntapFileSystemArgs", "OntapFileSystem"]

@pulumi.input_type
class OntapFileSystemArgs:
    def __init__(
        __self__,
        *,
        deployment_type: pulumi.Input[_builtins.str],
        preferred_subnet_id: pulumi.Input[_builtins.str],
        storage_capacity: pulumi.Input[_builtins.int],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]
        ] = ...,
        endpoint_ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
        fsx_admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ha_pairs: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput_capacity_per_ha_pair: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_type.setter
    def deployment_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @storage_capacity.setter
    def storage_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]]: ...
    @disk_iops_configuration.setter
    def disk_iops_configuration(
        self, value: Optional[pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressRange")
    def endpoint_ip_address_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_ip_address_range.setter
    def endpoint_ip_address_range(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fsxAdminPassword")
    def fsx_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fsx_admin_password.setter
    def fsx_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="haPairs")
    def ha_pairs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ha_pairs.setter
    def ha_pairs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @route_table_ids.setter
    def route_table_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacityPerHaPair")
    def throughput_capacity_per_ha_pair(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity_per_ha_pair.setter
    def throughput_capacity_per_ha_pair(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _OntapFileSystemState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]
        ] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointArgs]]]
        ] = ...,
        fsx_admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ha_pairs: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput_capacity_per_ha_pair: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> Optional[pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]]: ...
    @disk_iops_configuration.setter
    def disk_iops_configuration(
        self, value: Optional[pulumi.Input[OntapFileSystemDiskIopsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressRange")
    def endpoint_ip_address_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_ip_address_range.setter
    def endpoint_ip_address_range(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointArgs]]]
    ]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fsxAdminPassword")
    def fsx_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fsx_admin_password.setter
    def fsx_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="haPairs")
    def ha_pairs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ha_pairs.setter
    def ha_pairs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_interface_ids.setter
    def network_interface_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @route_table_ids.setter
    def route_table_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacityPerHaPair")
    def throughput_capacity_per_ha_pair(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity_per_ha_pair.setter
    def throughput_capacity_per_ha_pair(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:fsx/ontapFileSystem:OntapFileSystem")
class OntapFileSystem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapFileSystemDiskIopsConfigurationArgs,
                    OntapFileSystemDiskIopsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        endpoint_ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
        fsx_admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ha_pairs: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput_capacity_per_ha_pair: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OntapFileSystemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[
                Union[
                    OntapFileSystemDiskIopsConfigurationArgs,
                    OntapFileSystemDiskIopsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_ip_address_range: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            OntapFileSystemEndpointArgs, OntapFileSystemEndpointArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        fsx_admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ha_pairs: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput_capacity_per_ha_pair: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OntapFileSystem: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> pulumi.Output[outputs.OntapFileSystemDiskIopsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressRange")
    def endpoint_ip_address_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[outputs.OntapFileSystemEndpoint]]: ...
    @_builtins.property
    @pulumi.getter(name="fsxAdminPassword")
    def fsx_admin_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="haPairs")
    def ha_pairs(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacityPerHaPair")
    def throughput_capacity_per_ha_pair(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> pulumi.Output[_builtins.str]: ...
