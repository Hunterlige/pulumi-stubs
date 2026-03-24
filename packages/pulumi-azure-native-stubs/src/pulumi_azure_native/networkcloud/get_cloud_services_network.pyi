

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudServicesNetworkResult', 'AwaitableGetCloudServicesNetworkResult', 'get_cloud_services_network', 'get_cloud_services_network_output']
@pulumi.output_type
class GetCloudServicesNetworkResult:
    
    def __init__(__self__, additional_egress_endpoints=..., associated_resource_ids=..., azure_api_version=..., cluster_id=..., detailed_status=..., detailed_status_message=..., enable_default_egress_endpoints=..., enabled_egress_endpoints=..., etag=..., extended_location=..., hybrid_aks_clusters_associated_ids=..., id=..., interface_name=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., virtual_machines_associated_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEgressEndpoints")
    def additional_egress_endpoints(self) -> Optional[Sequence[outputs.EgressEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultEgressEndpoints")
    def enable_default_egress_endpoints(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledEgressEndpoints")
    def enabled_egress_endpoints(self) -> Sequence[outputs.EgressEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetCloudServicesNetworkResult(GetCloudServicesNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudServicesNetworkResult]:
        ...
    


def get_cloud_services_network(cloud_services_network_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudServicesNetworkResult:
    
    ...

def get_cloud_services_network_output(cloud_services_network_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudServicesNetworkResult]:
    
    ...

