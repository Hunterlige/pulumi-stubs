

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectivityConfigurationResult', 'AwaitableGetConnectivityConfigurationResult', 'get_connectivity_configuration', 'get_connectivity_configuration_output']
@pulumi.output_type
class GetConnectivityConfigurationResult:
    
    def __init__(__self__, applies_to_groups=..., azure_api_version=..., connectivity_topology=..., delete_existing_peering=..., description=..., etag=..., hubs=..., id=..., is_global=..., name=..., provisioning_state=..., resource_guid=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> Sequence[outputs.ConnectivityGroupItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityTopology")
    def connectivity_topology(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteExistingPeering")
    def delete_existing_peering(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hubs(self) -> Optional[Sequence[outputs.HubResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectivityConfigurationResult(GetConnectivityConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectivityConfigurationResult]:
        ...
    


def get_connectivity_configuration(configuration_name: Optional[_builtins.str] = ..., network_manager_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectivityConfigurationResult:
    
    ...

def get_connectivity_configuration_output(configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectivityConfigurationResult]:
    
    ...

