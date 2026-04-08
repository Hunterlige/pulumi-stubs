import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInternetGatewayResult",
    "AwaitableGetInternetGatewayResult",
    "get_internet_gateway",
    "get_internet_gateway_output",
]

@pulumi.output_type
class GetInternetGatewayResult:
    def __init__(
        __self__,
        annotation=...,
        azure_api_version=...,
        id=...,
        internet_gateway_rule_id=...,
        ipv4_address=...,
        location=...,
        name=...,
        network_fabric_controller_id=...,
        port=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internetGatewayRuleId")
    def internet_gateway_rule_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkFabricControllerId")
    def network_fabric_controller_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetInternetGatewayResult(GetInternetGatewayResult):
    def __await__(self): ...

def get_internet_gateway(
    internet_gateway_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInternetGatewayResult: ...
def get_internet_gateway_output(
    internet_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInternetGatewayResult]: ...
