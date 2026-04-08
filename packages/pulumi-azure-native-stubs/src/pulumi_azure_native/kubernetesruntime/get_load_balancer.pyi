import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLoadBalancerResult",
    "AwaitableGetLoadBalancerResult",
    "get_load_balancer",
    "get_load_balancer_output",
]

@pulumi.output_type
class GetLoadBalancerResult:
    def __init__(
        __self__,
        addresses=...,
        advertise_mode=...,
        azure_api_version=...,
        bgp_peers=...,
        id=...,
        name=...,
        provisioning_state=...,
        service_selector=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="advertiseMode")
    def advertise_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bgpPeers")
    def bgp_peers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceSelector")
    def service_selector(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    def __await__(self): ...

def get_load_balancer(
    load_balancer_name: Optional[_builtins.str] = ...,
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLoadBalancerResult: ...
def get_load_balancer_output(
    load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLoadBalancerResult]: ...
