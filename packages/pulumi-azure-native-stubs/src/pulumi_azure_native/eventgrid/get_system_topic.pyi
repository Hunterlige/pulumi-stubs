import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSystemTopicResult",
    "AwaitableGetSystemTopicResult",
    "get_system_topic",
    "get_system_topic_output",
]

@pulumi.output_type
class GetSystemTopicResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        identity=...,
        location=...,
        metric_resource_id=...,
        name=...,
        provisioning_state=...,
        source=...,
        system_data=...,
        tags=...,
        topic_type=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricResourceId")
    def metric_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="topicType")
    def topic_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSystemTopicResult(GetSystemTopicResult):
    def __await__(self): ...

def get_system_topic(
    resource_group_name: Optional[_builtins.str] = ...,
    system_topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSystemTopicResult: ...
def get_system_topic_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    system_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSystemTopicResult]: ...
