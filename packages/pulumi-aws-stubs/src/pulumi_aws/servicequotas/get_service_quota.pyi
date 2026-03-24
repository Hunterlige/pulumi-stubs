import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceQuotaResult",
    "AwaitableGetServiceQuotaResult",
    "get_service_quota",
    "get_service_quota_output",
]

@pulumi.output_type
class GetServiceQuotaResult:
    def __init__(
        __self__,
        adjustable=...,
        arn=...,
        default_value=...,
        global_quota=...,
        id=...,
        quota_code=...,
        quota_name=...,
        region=...,
        service_code=...,
        service_name=...,
        usage_metrics=...,
        value=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def adjustable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="globalQuota")
    def global_quota(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usageMetrics")
    def usage_metrics(self) -> Sequence[outputs.GetServiceQuotaUsageMetricResult]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float: ...

class AwaitableGetServiceQuotaResult(GetServiceQuotaResult):
    def __await__(self): ...

def get_service_quota(
    quota_code: Optional[_builtins.str] = ...,
    quota_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    service_code: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceQuotaResult: ...
def get_service_quota_output(
    quota_code: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    quota_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_code: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceQuotaResult]: ...
