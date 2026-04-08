import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDedicatedHsmResult",
    "AwaitableGetDedicatedHsmResult",
    "get_dedicated_hsm",
    "get_dedicated_hsm_output",
]

@pulumi.output_type
class GetDedicatedHsmResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        management_network_profile=...,
        name=...,
        network_profile=...,
        provisioning_state=...,
        sku=...,
        stamp_id=...,
        status_message=...,
        system_data=...,
        tags=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementNetworkProfile")
    def management_network_profile(
        self,
    ) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="stampId")
    def stamp_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
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
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetDedicatedHsmResult(GetDedicatedHsmResult):
    def __await__(self): ...

def get_dedicated_hsm(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDedicatedHsmResult: ...
def get_dedicated_hsm_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDedicatedHsmResult]: ...
