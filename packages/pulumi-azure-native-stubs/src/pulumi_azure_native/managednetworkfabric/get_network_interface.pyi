import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkInterfaceResult",
    "AwaitableGetNetworkInterfaceResult",
    "get_network_interface",
    "get_network_interface_output",
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        connected_to=...,
        id=...,
        interface_type=...,
        ipv4_address=...,
        ipv6_address=...,
        name=...,
        physical_identifier=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectedTo")
    def connected_to(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="physicalIdentifier")
    def physical_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    def __await__(self): ...

def get_network_interface(
    network_device_name: Optional[_builtins.str] = ...,
    network_interface_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkInterfaceResult: ...
def get_network_interface_output(
    network_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_interface_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkInterfaceResult]: ...
