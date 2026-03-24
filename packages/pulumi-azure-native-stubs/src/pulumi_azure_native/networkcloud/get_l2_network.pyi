

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetL2NetworkResult', 'AwaitableGetL2NetworkResult', 'get_l2_network', 'get_l2_network_output']
@pulumi.output_type
class GetL2NetworkResult:
    def __init__(__self__, associated_resource_ids=..., azure_api_version=..., cluster_id=..., detailed_status=..., detailed_status_message=..., etag=..., extended_location=..., hybrid_aks_clusters_associated_ids=..., hybrid_aks_plugin_type=..., id=..., interface_name=..., l2_isolation_domain_id=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., virtual_machines_associated_ids=...) -> None:
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
    @pulumi.getter(name="hybridAksPluginType")
    def hybrid_aks_plugin_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="l2IsolationDomainId")
    def l2_isolation_domain_id(self) -> _builtins.str:
        
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
    


class AwaitableGetL2NetworkResult(GetL2NetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetL2NetworkResult]:
        ...
    


def get_l2_network(l2_network_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetL2NetworkResult:
    
    ...

def get_l2_network_output(l2_network_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetL2NetworkResult]:
    
    ...

