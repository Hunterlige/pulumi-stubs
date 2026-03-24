

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkDeviceStatusResult', 'AwaitableGetNetworkDeviceStatusResult', 'get_network_device_status', 'get_network_device_status_output']
@pulumi.output_type
class GetNetworkDeviceStatusResult:
    
    def __init__(__self__, operational_status=..., power_cycle_state=..., serial_number=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerCycleState")
    def power_cycle_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkDeviceStatusResult(GetNetworkDeviceStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkDeviceStatusResult]:
        ...
    


def get_network_device_status(network_device_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkDeviceStatusResult:
    
    ...

def get_network_device_status_output(network_device_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkDeviceStatusResult]:
    
    ...

