

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, associated_workspaces=..., azure_api_version=..., billing_type=..., capacity_reservation_properties=..., cluster_id=..., created_date=..., id=..., identity=..., is_availability_zones_enabled=..., is_double_encryption_enabled=..., key_vault_properties=..., last_modified_date=..., location=..., name=..., provisioning_state=..., sku=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedWorkspaces")
    def associated_workspaces(self) -> Optional[Sequence[outputs.AssociatedWorkspaceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationProperties")
    def capacity_reservation_properties(self) -> Optional[outputs.CapacityReservationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAvailabilityZonesEnabled")
    def is_availability_zones_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDoubleEncryptionEnabled")
    def is_double_encryption_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ClusterSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

