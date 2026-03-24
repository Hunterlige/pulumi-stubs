import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSupportedServiceResult",
    "AwaitableGetSupportedServiceResult",
    "get_supported_service",
    "get_supported_service_output",
]

@pulumi.output_type
class GetSupportedServiceResult:
    def __init__(
        __self__,
        available_on_restricted_vip=...,
        id=...,
        known_limitations=...,
        service_name=...,
        service_support_stage=...,
        support_stage=...,
        supported_methods=...,
        title=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availableOnRestrictedVip")
    def available_on_restricted_vip(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="knownLimitations")
    def known_limitations(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceSupportStage")
    def service_support_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportStage")
    def support_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedMethods")
    def supported_methods(
        self,
    ) -> Sequence[outputs.GetSupportedServiceSupportedMethodResult]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

class AwaitableGetSupportedServiceResult(GetSupportedServiceResult):
    def __await__(self): ...

def get_supported_service(
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSupportedServiceResult: ...
def get_supported_service_output(
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSupportedServiceResult]: ...
