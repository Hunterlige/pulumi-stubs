import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOntapFileSystemResult",
    "AwaitableGetOntapFileSystemResult",
    "get_ontap_file_system",
    "get_ontap_file_system_output",
]

@pulumi.output_type
class GetOntapFileSystemResult:
    def __init__(
        __self__,
        arn=...,
        automatic_backup_retention_days=...,
        daily_automatic_backup_start_time=...,
        deployment_type=...,
        disk_iops_configurations=...,
        dns_name=...,
        endpoint_ip_address_range=...,
        endpoints=...,
        ha_pairs=...,
        id=...,
        kms_key_id=...,
        network_interface_ids=...,
        owner_id=...,
        preferred_subnet_id=...,
        region=...,
        route_table_ids=...,
        storage_capacity=...,
        storage_type=...,
        subnet_ids=...,
        tags=...,
        throughput_capacity=...,
        throughput_capacity_per_ha_pair=...,
        vpc_id=...,
        weekly_maintenance_start_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfigurations")
    def disk_iops_configurations(
        self,
    ) -> Sequence[outputs.GetOntapFileSystemDiskIopsConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressRange")
    def endpoint_ip_address_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetOntapFileSystemEndpointResult]: ...
    @_builtins.property
    @pulumi.getter(name="haPairs")
    def ha_pairs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacityPerHaPair")
    def throughput_capacity_per_ha_pair(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> _builtins.str: ...

class AwaitableGetOntapFileSystemResult(GetOntapFileSystemResult):
    def __await__(self): ...

def get_ontap_file_system(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOntapFileSystemResult: ...
def get_ontap_file_system_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOntapFileSystemResult]: ...
