import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMetricAlertResult",
    "AwaitableGetMetricAlertResult",
    "get_metric_alert",
    "get_metric_alert_output",
]

@pulumi.output_type
class GetMetricAlertResult:
    def __init__(
        __self__,
        actions=...,
        auto_mitigate=...,
        azure_api_version=...,
        criteria=...,
        description=...,
        enabled=...,
        evaluation_frequency=...,
        id=...,
        is_migrated=...,
        last_updated_time=...,
        location=...,
        name=...,
        scopes=...,
        severity=...,
        tags=...,
        target_resource_region=...,
        target_resource_type=...,
        type=...,
        window_size=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[outputs.MetricAlertActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isMigrated")
    def is_migrated(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceRegion")
    def target_resource_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> _builtins.str: ...

class AwaitableGetMetricAlertResult(GetMetricAlertResult):
    def __await__(self): ...

def get_metric_alert(
    resource_group_name: Optional[_builtins.str] = ...,
    rule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMetricAlertResult: ...
def get_metric_alert_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMetricAlertResult]: ...
