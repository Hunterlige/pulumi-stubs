

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInterfaceEndpointResult', 'AwaitableGetInterfaceEndpointResult', 'get_interface_endpoint', 'get_interface_endpoint_output']
@pulumi.output_type
class GetInterfaceEndpointResult:
    
    def __init__(__self__, azure_api_version=..., endpoint_service=..., etag=..., fqdn=..., id=..., location=..., name=..., network_interfaces=..., owner=..., provisioning_state=..., subnet=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointService")
    def endpoint_service(self) -> Optional[outputs.EndpointServiceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.NetworkInterfaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    


class AwaitableGetInterfaceEndpointResult(GetInterfaceEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetInterfaceEndpointResult]:
        ...
    


def get_interface_endpoint(expand: Optional[_builtins.str] = ..., interface_endpoint_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInterfaceEndpointResult:
    
    ...

def get_interface_endpoint_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., interface_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInterfaceEndpointResult]:
    
    ...

