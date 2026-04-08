import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHybridUseBenefitResult",
    "AwaitableGetHybridUseBenefitResult",
    "get_hybrid_use_benefit",
    "get_hybrid_use_benefit_output",
]

@pulumi.output_type
class GetHybridUseBenefitResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_date=...,
        etag=...,
        id=...,
        last_updated_date=...,
        name=...,
        provisioning_state=...,
        sku=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetHybridUseBenefitResult(GetHybridUseBenefitResult):
    def __await__(self): ...

def get_hybrid_use_benefit(
    plan_id: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHybridUseBenefitResult: ...
def get_hybrid_use_benefit_output(
    plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHybridUseBenefitResult]: ...
