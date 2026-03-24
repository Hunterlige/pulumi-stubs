

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectedClusterResult', 'AwaitableGetConnectedClusterResult', 'get_connected_cluster', 'get_connected_cluster_output']
@pulumi.output_type
class GetConnectedClusterResult:
    
    def __init__(__self__, aad_profile=..., agent_public_key_certificate=..., agent_version=..., arc_agent_profile=..., azure_api_version=..., azure_hybrid_benefit=..., connectivity_status=..., distribution=..., distribution_version=..., id=..., identity=..., infrastructure=..., kind=..., kubernetes_version=..., last_connectivity_time=..., location=..., managed_identity_certificate_expiration_time=..., miscellaneous_properties=..., name=..., offering=..., private_link_scope_resource_id=..., private_link_state=..., provisioning_state=..., system_data=..., tags=..., total_core_count=..., total_node_count=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[outputs.AadProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPublicKeyCertificate")
    def agent_public_key_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> Optional[outputs.ArcAgentProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionVersion")
    def distribution_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> outputs.ConnectedClusterIdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def infrastructure(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConnectivityTime")
    def last_connectivity_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityCertificateExpirationTime")
    def managed_identity_certificate_expiration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="miscellaneousProperties")
    def miscellaneous_properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offering(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkState")
    def private_link_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="totalCoreCount")
    def total_core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalNodeCount")
    def total_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectedClusterResult(GetConnectedClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectedClusterResult]:
        ...
    


def get_connected_cluster(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectedClusterResult:
    
    ...

def get_connected_cluster_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectedClusterResult]:
    
    ...

