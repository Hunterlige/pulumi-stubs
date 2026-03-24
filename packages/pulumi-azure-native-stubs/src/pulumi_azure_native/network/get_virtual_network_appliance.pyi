

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkApplianceResult', 'AwaitableGetVirtualNetworkApplianceResult', 'get_virtual_network_appliance', 'get_virtual_network_appliance_output']
@pulumi.output_type
class GetVirtualNetworkApplianceResult:
    
    def __init__(__self__, azure_api_version=..., bandwidth_in_gbps=..., etag=..., id=..., ip_configurations=..., location=..., name=..., provisioning_state=..., resource_guid=..., subnet=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.VirtualNetworkApplianceIpConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubnetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualNetworkApplianceResult(GetVirtualNetworkApplianceResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkApplianceResult]:
        ...
    


def get_virtual_network_appliance(resource_group_name: Optional[_builtins.str] = ..., virtual_network_appliance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkApplianceResult:
    
    ...

def get_virtual_network_appliance_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_appliance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkApplianceResult]:
    
    ...

