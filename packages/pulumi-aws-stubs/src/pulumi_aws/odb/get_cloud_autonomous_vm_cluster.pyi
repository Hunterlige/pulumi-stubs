import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudAutonomousVmClusterResult",
    "AwaitableGetCloudAutonomousVmClusterResult",
    "get_cloud_autonomous_vm_cluster",
    "get_cloud_autonomous_vm_cluster_output",
]

@pulumi.output_type
class GetCloudAutonomousVmClusterResult:
    def __init__(
        __self__,
        arn=...,
        autonomous_data_storage_percentage=...,
        autonomous_data_storage_size_in_tbs=...,
        available_autonomous_data_storage_size_in_tbs=...,
        available_container_databases=...,
        available_cpus=...,
        cloud_exadata_infrastructure_arn=...,
        cloud_exadata_infrastructure_id=...,
        compute_model=...,
        cpu_core_count=...,
        cpu_core_count_per_node=...,
        cpu_percentage=...,
        created_at=...,
        data_storage_size_in_gbs=...,
        data_storage_size_in_tbs=...,
        db_servers=...,
        description=...,
        display_name=...,
        domain=...,
        exadata_storage_in_tbs_lowest_scaled_value=...,
        hostname=...,
        id=...,
        is_mtls_enabled_vm_cluster=...,
        license_model=...,
        maintenance_windows=...,
        max_acds_lowest_scaled_value=...,
        memory_per_oracle_compute_unit_in_gbs=...,
        memory_size_in_gbs=...,
        node_count=...,
        non_provisionable_autonomous_container_databases=...,
        oci_resource_anchor_name=...,
        oci_url=...,
        ocid=...,
        odb_network_arn=...,
        odb_network_id=...,
        odb_node_storage_size_in_gbs=...,
        percent_progress=...,
        provisionable_autonomous_container_databases=...,
        provisioned_autonomous_container_databases=...,
        provisioned_cpus=...,
        reclaimable_cpus=...,
        region=...,
        reserved_cpus=...,
        scan_listener_port_non_tls=...,
        scan_listener_port_tls=...,
        shape=...,
        status=...,
        status_reason=...,
        tags=...,
        time_database_ssl_certificate_expires=...,
        time_ords_certificate_expires=...,
        time_zone=...,
        total_container_databases=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDataStoragePercentage")
    def autonomous_data_storage_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="availableAutonomousDataStorageSizeInTbs")
    def available_autonomous_data_storage_size_in_tbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="availableContainerDatabases")
    def available_container_databases(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableCpus")
    def available_cpus(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureArn")
    def cloud_exadata_infrastructure_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuPercentage")
    def cpu_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInGbs")
    def data_storage_size_in_gbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exadataStorageInTbsLowestScaledValue")
    def exadata_storage_in_tbs_lowest_scaled_value(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isMtlsEnabledVmCluster")
    def is_mtls_enabled_vm_cluster(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Sequence[outputs.GetCloudAutonomousVmClusterMaintenanceWindowResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxAcdsLowestScaledValue")
    def max_acds_lowest_scaled_value(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nonProvisionableAutonomousContainerDatabases")
    def non_provisionable_autonomous_container_databases(self) -> _builtins.int: ...
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
    @pulumi.getter(name="odbNodeStorageSizeInGbs")
    def odb_node_storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="provisionableAutonomousContainerDatabases")
    def provisionable_autonomous_container_databases(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedAutonomousContainerDatabases")
    def provisioned_autonomous_container_databases(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedCpus")
    def provisioned_cpus(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="reclaimableCpus")
    def reclaimable_cpus(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservedCpus")
    def reserved_cpus(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeDatabaseSslCertificateExpires")
    def time_database_ssl_certificate_expires(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeOrdsCertificateExpires")
    def time_ords_certificate_expires(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> _builtins.int: ...

class AwaitableGetCloudAutonomousVmClusterResult(GetCloudAutonomousVmClusterResult):
    def __await__(self): ...

def get_cloud_autonomous_vm_cluster(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCloudAutonomousVmClusterResult: ...
def get_cloud_autonomous_vm_cluster_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudAutonomousVmClusterResult]: ...
