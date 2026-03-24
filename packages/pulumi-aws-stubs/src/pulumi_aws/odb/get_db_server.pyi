

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDbServerResult', 'AwaitableGetDbServerResult', 'get_db_server', 'get_db_server_output']
@pulumi.output_type
class GetDbServerResult:
    
    def __init__(__self__, autonomous_virtual_machine_ids=..., autonomous_vm_cluster_ids=..., cloud_exadata_infrastructure_id=..., compute_model=..., cpu_core_count=..., created_at=..., db_node_storage_size_in_gbs=..., db_server_patching_details=..., display_name=..., exadata_infrastructure_id=..., id=..., max_cpu_count=..., max_db_node_storage_in_gbs=..., max_memory_in_gbs=..., memory_size_in_gbs=..., oci_resource_anchor_name=..., ocid=..., region=..., shape=..., status=..., status_reason=..., vm_cluster_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousVirtualMachineIds")
    def autonomous_virtual_machine_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousVmClusterIds")
    def autonomous_vm_cluster_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServerPatchingDetails")
    def db_server_patching_details(self) -> Sequence[outputs.GetDbServerDbServerPatchingDetailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageInGbs")
    def max_db_node_storage_in_gbs(self) -> _builtins.int:
        
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
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str:
        
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
    @pulumi.getter(name="vmClusterIds")
    def vm_cluster_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetDbServerResult(GetDbServerResult):
    def __await__(self): # -> Generator[Never, Any, GetDbServerResult]:
        ...
    


def get_db_server(cloud_exadata_infrastructure_id: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDbServerResult:
    
    ...

def get_db_server_output(cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDbServerResult]:
    
    ...

