

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkProfileResult', 'AwaitableGetNetworkProfileResult', 'get_network_profile', 'get_network_profile_output']
@pulumi.output_type
class GetNetworkProfileResult:
    
    def __init__(__self__, azure_api_version=..., container_network_interface_configurations=..., container_network_interfaces=..., etag=..., id=..., location=..., name=..., provisioning_state=..., resource_guid=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerNetworkInterfaceConfigurations")
    def container_network_interface_configurations(self) -> Optional[Sequence[outputs.ContainerNetworkInterfaceConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerNetworkInterfaces")
    def container_network_interfaces(self) -> Sequence[outputs.ContainerNetworkInterfaceResponse]:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkProfileResult(GetNetworkProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkProfileResult]:
        ...
    


def get_network_profile(expand: Optional[_builtins.str] = ..., network_profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkProfileResult:
    
    ...

def get_network_profile_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., network_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkProfileResult]:
    
    ...

