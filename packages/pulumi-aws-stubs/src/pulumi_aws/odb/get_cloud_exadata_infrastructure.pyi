

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudExadataInfrastructureResult', 'AwaitableGetCloudExadataInfrastructureResult', 'get_cloud_exadata_infrastructure', 'get_cloud_exadata_infrastructure_output']
@pulumi.output_type
class GetCloudExadataInfrastructureResult:
    
    def __init__(__self__, activated_storage_count=..., additional_storage_count=..., arn=..., availability_zone=..., availability_zone_id=..., available_storage_size_in_gbs=..., compute_count=..., compute_model=..., cpu_count=..., created_at=..., customer_contacts_to_send_to_ocis=..., data_storage_size_in_tbs=..., database_server_type=..., db_node_storage_size_in_gbs=..., db_server_version=..., display_name=..., id=..., last_maintenance_run_id=..., maintenance_windows=..., max_cpu_count=..., max_data_storage_in_tbs=..., max_db_node_storage_size_in_gbs=..., max_memory_in_gbs=..., memory_size_in_gbs=..., monthly_db_server_version=..., monthly_storage_server_version=..., next_maintenance_run_id=..., oci_resource_anchor_name=..., oci_url=..., ocid=..., percent_progress=..., region=..., shape=..., status=..., status_reason=..., storage_count=..., storage_server_type=..., storage_server_version=..., tags=..., total_storage_size_in_gbs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeInGbs")
    def available_storage_size_in_gbs(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerContactsToSendToOcis")
    def customer_contacts_to_send_to_ocis(self) -> Sequence[outputs.GetCloudExadataInfrastructureCustomerContactsToSendToOciResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerType")
    def database_server_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastMaintenanceRunId")
    def last_maintenance_run_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence[outputs.GetCloudExadataInfrastructureMaintenanceWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDataStorageInTbs")
    def max_data_storage_in_tbs(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeInGbs")
    def max_db_node_storage_size_in_gbs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMemoryInGbs")
    def max_memory_in_gbs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerType")
    def storage_server_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeInGbs")
    def total_storage_size_in_gbs(self) -> _builtins.int:
        
        ...
    


class AwaitableGetCloudExadataInfrastructureResult(GetCloudExadataInfrastructureResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudExadataInfrastructureResult]:
        ...
    


def get_cloud_exadata_infrastructure(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudExadataInfrastructureResult:
    
    ...

def get_cloud_exadata_infrastructure_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudExadataInfrastructureResult]:
    
    ...

