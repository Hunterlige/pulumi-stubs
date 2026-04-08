import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNetworkTapResult",
    "AwaitableGetVirtualNetworkTapResult",
    "get_virtual_network_tap",
    "get_virtual_network_tap_output",
]

@pulumi.output_type
class GetVirtualNetworkTapResult:
    def __init__(
        __self__,
        azure_api_version=...,
        destination_load_balancer_front_end_ip_configuration=...,
        destination_network_interface_ip_configuration=...,
        destination_port=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        network_interface_tap_configurations=...,
        provisioning_state=...,
        resource_guid=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationLoadBalancerFrontEndIPConfiguration")
    def destination_load_balancer_front_end_ip_configuration(
        self,
    ) -> Optional[outputs.FrontendIPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="destinationNetworkInterfaceIPConfiguration")
    def destination_network_interface_ip_configuration(
        self,
    ) -> Optional[outputs.NetworkInterfaceIPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceTapConfigurations")
    def network_interface_tap_configurations(
        self,
    ) -> Sequence[outputs.NetworkInterfaceTapConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualNetworkTapResult(GetVirtualNetworkTapResult):
    def __await__(self): ...

def get_virtual_network_tap(
    resource_group_name: Optional[_builtins.str] = ...,
    tap_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkTapResult: ...
def get_virtual_network_tap_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tap_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkTapResult]: ...
