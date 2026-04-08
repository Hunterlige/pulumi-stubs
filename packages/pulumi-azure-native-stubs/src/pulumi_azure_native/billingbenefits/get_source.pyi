import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSourceResult",
    "AwaitableGetSourceResult",
    "get_source",
    "get_source_output",
]

@pulumi.output_type
class GetSourceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        credit=...,
        etag=...,
        id=...,
        identity=...,
        impacted_billing_period=...,
        kind=...,
        location=...,
        managed_by=...,
        name=...,
        plan=...,
        sku=...,
        source_resource_id=...,
        status=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def credit(self) -> Optional[outputs.CommitmentResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="impactedBillingPeriod")
    def impacted_billing_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSourceResult(GetSourceResult):
    def __await__(self): ...

def get_source(
    credit_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    source_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSourceResult: ...
def get_source_output(
    credit_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    source_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSourceResult]: ...
