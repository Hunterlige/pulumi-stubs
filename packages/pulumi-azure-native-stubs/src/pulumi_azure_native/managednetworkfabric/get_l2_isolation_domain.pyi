import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetL2IsolationDomainResult",
    "AwaitableGetL2IsolationDomainResult",
    "get_l2_isolation_domain",
    "get_l2_isolation_domain_output",
]

@pulumi.output_type
class GetL2IsolationDomainResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        configuration_state=...,
        id=...,
        location=...,
        mtu=...,
        name=...,
        network_fabric_id=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        vlan_id=...,
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
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> _builtins.str: ...
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
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> _builtins.int: ...

class AwaitableGetL2IsolationDomainResult(GetL2IsolationDomainResult):
    def __await__(self): ...

def get_l2_isolation_domain(
    l2_isolation_domain_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetL2IsolationDomainResult: ...
def get_l2_isolation_domain_output(
    l2_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetL2IsolationDomainResult]: ...
