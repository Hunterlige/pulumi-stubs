import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkInterfaceStatusResult",
    "AwaitableGetNetworkInterfaceStatusResult",
    "get_network_interface_status",
    "get_network_interface_status_output",
]

@pulumi.output_type
class GetNetworkInterfaceStatusResult:
    def __init__(
        __self__,
        administrative_state=...,
        connected_to=...,
        operational_status=...,
        phy_status=...,
        transceiver_status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectedTo")
    def connected_to(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phyStatus")
    def phy_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transceiverStatus")
    def transceiver_status(self) -> Optional[_builtins.str]: ...

class AwaitableGetNetworkInterfaceStatusResult(GetNetworkInterfaceStatusResult):
    def __await__(self): ...

def get_network_interface_status(
    network_device_name: Optional[_builtins.str] = ...,
    network_interface_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkInterfaceStatusResult: ...
def get_network_interface_status_output(
    network_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_interface_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkInterfaceStatusResult]: ...
