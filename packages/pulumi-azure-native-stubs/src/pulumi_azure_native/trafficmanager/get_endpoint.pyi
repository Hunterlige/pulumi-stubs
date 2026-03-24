

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEndpointResult', 'AwaitableGetEndpointResult', 'get_endpoint', 'get_endpoint_output']
@pulumi.output_type
class GetEndpointResult:
    
    def __init__(__self__, always_serve=..., azure_api_version=..., custom_headers=..., endpoint_location=..., endpoint_monitor_status=..., endpoint_status=..., geo_mapping=..., id=..., min_child_endpoints=..., min_child_endpoints_i_pv4=..., min_child_endpoints_i_pv6=..., name=..., priority=..., subnets=..., target=..., target_resource_id=..., type=..., weight=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[Sequence[outputs.EndpointPropertiesCustomHeadersItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.EndpointPropertiesSubnetsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.float]:
        
        ...
    


class AwaitableGetEndpointResult(GetEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetEndpointResult]:
        ...
    


def get_endpoint(endpoint_name: Optional[_builtins.str] = ..., endpoint_type: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEndpointResult:
    
    ...

def get_endpoint_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEndpointResult]:
    
    ...

