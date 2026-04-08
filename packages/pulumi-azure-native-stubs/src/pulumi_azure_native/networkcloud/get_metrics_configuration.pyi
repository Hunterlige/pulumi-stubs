import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMetricsConfigurationResult",
    "AwaitableGetMetricsConfigurationResult",
    "get_metrics_configuration",
    "get_metrics_configuration_output",
]

@pulumi.output_type
class GetMetricsConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        collection_interval=...,
        detailed_status=...,
        detailed_status_message=...,
        disabled_metrics=...,
        enabled_metrics=...,
        etag=...,
        extended_location=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="collectionInterval")
    def collection_interval(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disabledMetrics")
    def disabled_metrics(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
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

class AwaitableGetMetricsConfigurationResult(GetMetricsConfigurationResult):
    def __await__(self): ...

def get_metrics_configuration(
    cluster_name: Optional[_builtins.str] = ...,
    metrics_configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMetricsConfigurationResult: ...
def get_metrics_configuration_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    metrics_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMetricsConfigurationResult]: ...
