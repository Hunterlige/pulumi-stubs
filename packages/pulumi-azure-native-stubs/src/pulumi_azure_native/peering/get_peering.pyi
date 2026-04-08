import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPeeringResult",
    "AwaitableGetPeeringResult",
    "get_peering",
    "get_peering_output",
]

@pulumi.output_type
class GetPeeringResult:
    def __init__(
        __self__,
        azure_api_version=...,
        direct=...,
        exchange=...,
        id=...,
        kind=...,
        location=...,
        name=...,
        peering_location=...,
        provisioning_state=...,
        sku=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direct(self) -> Optional[outputs.PeeringPropertiesDirectResponse]: ...
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> Optional[outputs.PeeringPropertiesExchangeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.PeeringSkuResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPeeringResult(GetPeeringResult):
    def __await__(self): ...

def get_peering(
    peering_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPeeringResult: ...
def get_peering_output(
    peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPeeringResult]: ...
