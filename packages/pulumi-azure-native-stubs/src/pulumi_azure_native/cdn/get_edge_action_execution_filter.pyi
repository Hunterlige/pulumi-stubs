import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEdgeActionExecutionFilterResult",
    "AwaitableGetEdgeActionExecutionFilterResult",
    "get_edge_action_execution_filter",
    "get_edge_action_execution_filter_output",
]

@pulumi.output_type
class GetEdgeActionExecutionFilterResult:
    def __init__(
        __self__,
        azure_api_version=...,
        execution_filter_identifier_header_name=...,
        execution_filter_identifier_header_value=...,
        id=...,
        last_update_time=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        version_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderName")
    def execution_filter_identifier_header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderValue")
    def execution_filter_identifier_header_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> _builtins.str: ...
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
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str: ...

class AwaitableGetEdgeActionExecutionFilterResult(GetEdgeActionExecutionFilterResult):
    def __await__(self): ...

def get_edge_action_execution_filter(
    edge_action_name: Optional[_builtins.str] = ...,
    execution_filter: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEdgeActionExecutionFilterResult: ...
def get_edge_action_execution_filter_output(
    edge_action_name: Optional[pulumi.Input[_builtins.str]] = ...,
    execution_filter: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEdgeActionExecutionFilterResult]: ...
