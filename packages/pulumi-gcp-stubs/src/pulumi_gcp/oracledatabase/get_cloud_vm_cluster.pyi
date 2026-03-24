

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudVmClusterResult', 'AwaitableGetCloudVmClusterResult', 'get_cloud_vm_cluster', 'get_cloud_vm_cluster_output']
@pulumi.output_type
class GetCloudVmClusterResult:
    
    def __init__(__self__, backup_odb_subnet=..., backup_subnet_cidr=..., cidr=..., cloud_vm_cluster_id=..., create_time=..., deletion_protection=..., display_name=..., effective_labels=..., exadata_infrastructure=..., gcp_oracle_zone=..., id=..., labels=..., location=..., name=..., network=..., odb_network=..., odb_subnet=..., project=..., properties=..., pulumi_labels=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupOdbSubnet")
    def backup_odb_subnet(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructure")
    def exadata_infrastructure(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.GetCloudVmClusterPropertyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetCloudVmClusterResult(GetCloudVmClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudVmClusterResult]:
        ...
    


def get_cloud_vm_cluster(cloud_vm_cluster_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudVmClusterResult:
    
    ...

def get_cloud_vm_cluster_output(cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudVmClusterResult]:
    
    ...

