import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDbNodeResult",
    "AwaitableGetDbNodeResult",
    "get_db_node",
    "get_db_node_output",
]

@pulumi.output_type
class GetDbNodeResult:
    def __init__(
        __self__,
        additional_details=...,
        arn=...,
        backup_ip_id=...,
        backup_vnic2_id=...,
        backup_vnic_id=...,
        cloud_vm_cluster_id=...,
        cpu_core_count=...,
        created_at=...,
        db_server_id=...,
        db_storage_size_in_gbs=...,
        db_system_id=...,
        fault_domain=...,
        floating_ip_address=...,
        host_ip_id=...,
        hostname=...,
        id=...,
        maintenance_type=...,
        memory_size_in_gbs=...,
        oci_resource_anchor_name=...,
        ocid=...,
        private_ip_address=...,
        region=...,
        software_storage_size_in_gbs=...,
        status=...,
        status_reason=...,
        time_maintenance_window_end=...,
        time_maintenance_window_start=...,
        total_cpu_core_count=...,
        vnic2_id=...,
        vnic_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupIpId")
    def backup_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupVnic2Id")
    def backup_vnic2_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupVnicId")
    def backup_vnic_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbServerId")
    def db_server_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbStorageSizeInGbs")
    def db_storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="floatingIpAddress")
    def floating_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostIpId")
    def host_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceType")
    def maintenance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareStorageSizeInGbs")
    def software_storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeMaintenanceWindowEnd")
    def time_maintenance_window_end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeMaintenanceWindowStart")
    def time_maintenance_window_start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalCpuCoreCount")
    def total_cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vnic2Id")
    def vnic2_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vnicId")
    def vnic_id(self) -> _builtins.str: ...

class AwaitableGetDbNodeResult(GetDbNodeResult):
    def __await__(self): ...

def get_db_node(
    cloud_vm_cluster_id: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDbNodeResult: ...
def get_db_node_output(
    cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDbNodeResult]: ...
