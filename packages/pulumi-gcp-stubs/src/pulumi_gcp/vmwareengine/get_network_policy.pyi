import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkPolicyResult",
    "AwaitableGetNetworkPolicyResult",
    "get_network_policy",
    "get_network_policy_output",
]

@pulumi.output_type
class GetNetworkPolicyResult:
    def __init__(
        __self__,
        create_time=...,
        description=...,
        edge_services_cidr=...,
        external_ips=...,
        id=...,
        internet_accesses=...,
        location=...,
        name=...,
        project=...,
        uid=...,
        update_time=...,
        vmware_engine_network=...,
        vmware_engine_network_canonical=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="edgeServicesCidr")
    def edge_services_cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalIps")
    def external_ips(self) -> Sequence[outputs.GetNetworkPolicyExternalIpResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internetAccesses")
    def internet_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkPolicyInternetAccessResult]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> _builtins.str: ...

class AwaitableGetNetworkPolicyResult(GetNetworkPolicyResult):
    def __await__(self): ...

def get_network_policy(
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkPolicyResult: ...
def get_network_policy_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkPolicyResult]: ...
