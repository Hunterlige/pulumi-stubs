import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudVmClusterResult",
    "AwaitableGetCloudVmClusterResult",
    "get_cloud_vm_cluster",
    "get_cloud_vm_cluster_output",
]

@pulumi.output_type
class GetCloudVmClusterResult:
    def __init__(
        __self__,
        arn=...,
        cloud_exadata_infrastructure_arn=...,
        cloud_exadata_infrastructure_id=...,
        cluster_name=...,
        compute_model=...,
        cpu_core_count=...,
        created_at=...,
        data_collection_options=...,
        data_storage_size_in_tbs=...,
        db_node_storage_size_in_gbs=...,
        db_servers=...,
        disk_redundancy=...,
        display_name=...,
        domain=...,
        gi_version=...,
        hostname_prefix_computed=...,
        id=...,
        iorm_config_caches=...,
        is_local_backup_enabled=...,
        is_sparse_disk_group_enabled=...,
        last_update_history_entry_id=...,
        license_model=...,
        listener_port=...,
        memory_size_in_gbs=...,
        node_count=...,
        oci_resource_anchor_name=...,
        oci_url=...,
        ocid=...,
        odb_network_arn=...,
        odb_network_id=...,
        percent_progress=...,
        region=...,
        scan_dns_name=...,
        scan_dns_record_id=...,
        scan_ip_ids=...,
        shape=...,
        ssh_public_keys=...,
        status=...,
        status_reason=...,
        storage_size_in_gbs=...,
        system_version=...,
        tags=...,
        timezone=...,
        vip_ids=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureArn")
    def cloud_exadata_infrastructure_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> Sequence[outputs.GetCloudVmClusterDataCollectionOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefixComputed")
    def hostname_prefix_computed(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iormConfigCaches")
    def iorm_config_caches(
        self,
    ) -> Sequence[outputs.GetCloudVmClusterIormConfigCacheResult]: ...
    @_builtins.property
    @pulumi.getter(name="isLocalBackupEnabled")
    def is_local_backup_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isSparseDiskGroupEnabled")
    def is_sparse_disk_group_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateHistoryEntryId")
    def last_update_history_entry_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanDnsName")
    def scan_dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageSizeInGbs")
    def storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vipIds")
    def vip_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetCloudVmClusterResult(GetCloudVmClusterResult):
    def __await__(self): ...

def get_cloud_vm_cluster(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCloudVmClusterResult: ...
def get_cloud_vm_cluster_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudVmClusterResult]: ...
