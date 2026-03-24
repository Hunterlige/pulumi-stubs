

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLogicalNetworkResult', 'AwaitableGetLogicalNetworkResult', 'get_logical_network', 'get_logical_network_output']
@pulumi.output_type
class GetLogicalNetworkResult:
    
    def __init__(__self__, azure_api_version=..., dhcp_options=..., extended_location=..., id=..., location=..., name=..., provisioning_state=..., status=..., subnets=..., system_data=..., tags=..., type=..., vm_switch_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional[outputs.LogicalNetworkPropertiesDhcpOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.LogicalNetworkStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.SubnetResponse]]:
        
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
    @pulumi.getter(name="vmSwitchName")
    def vm_switch_name(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetLogicalNetworkResult(GetLogicalNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetLogicalNetworkResult]:
        ...
    


def get_logical_network(logical_network_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLogicalNetworkResult:
    
    ...

def get_logical_network_output(logical_network_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLogicalNetworkResult]:
    
    ...

