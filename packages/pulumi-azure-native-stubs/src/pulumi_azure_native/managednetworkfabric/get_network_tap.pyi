import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkTapResult",
    "AwaitableGetNetworkTapResult",
    "get_network_tap",
    "get_network_tap_output",
]

@pulumi.output_type
class GetNetworkTapResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        configuration_state=...,
        destinations=...,
        id=...,
        location=...,
        name=...,
        network_packet_broker_id=...,
        polling_type=...,
        provisioning_state=...,
        source_tap_rule_id=...,
        system_data=...,
        tags=...,
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
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[outputs.NetworkTapPropertiesResponseDestinations]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkPacketBrokerId")
    def network_packet_broker_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pollingType")
    def polling_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceTapRuleId")
    def source_tap_rule_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNetworkTapResult(GetNetworkTapResult):
    def __await__(self): ...

def get_network_tap(
    network_tap_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkTapResult: ...
def get_network_tap_output(
    network_tap_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkTapResult]: ...
