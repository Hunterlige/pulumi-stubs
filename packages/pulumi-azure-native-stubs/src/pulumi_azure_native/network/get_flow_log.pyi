import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFlowLogResult",
    "AwaitableGetFlowLogResult",
    "get_flow_log",
    "get_flow_log_output",
]

@pulumi.output_type
class GetFlowLogResult:
    def __init__(
        __self__,
        azure_api_version=...,
        enabled=...,
        enabled_filtering_criteria=...,
        etag=...,
        flow_analytics_configuration=...,
        format=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        provisioning_state=...,
        retention_policy=...,
        storage_id=...,
        tags=...,
        target_resource_guid=...,
        target_resource_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enabledFilteringCriteria")
    def enabled_filtering_criteria(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="flowAnalyticsConfiguration")
    def flow_analytics_configuration(
        self,
    ) -> Optional[outputs.TrafficAnalyticsPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[outputs.FlowLogFormatParametersResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[outputs.RetentionPolicyParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageId")
    def storage_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGuid")
    def target_resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFlowLogResult(GetFlowLogResult):
    def __await__(self): ...

def get_flow_log(
    flow_log_name: Optional[_builtins.str] = ...,
    network_watcher_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFlowLogResult: ...
def get_flow_log_output(
    flow_log_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_watcher_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFlowLogResult]: ...
