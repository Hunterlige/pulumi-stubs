

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceResult', 'AwaitableGetNamespaceResult', 'get_namespace', 'get_namespace_output']
@pulumi.output_type
class GetNamespaceResult:
    
    def __init__(__self__, azure_api_version=..., created_at=..., critical=..., data_center=..., enabled=..., id=..., location=..., metric_id=..., name=..., namespace_type=..., network_acls=..., pns_credentials=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., region=..., replication_region=..., scale_unit=..., service_bus_endpoint=..., sku=..., status=..., subscription_id=..., system_data=..., tags=..., type=..., updated_at=..., zone_redundancy=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.NetworkAclsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pnsCredentials")
    def pns_credentials(self) -> Optional[outputs.PnsCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationRegion")
    def replication_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetNamespaceResult(GetNamespaceResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceResult]:
        ...
    


def get_namespace(namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceResult:
    
    ...

def get_namespace_output(namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceResult]:
    
    ...

