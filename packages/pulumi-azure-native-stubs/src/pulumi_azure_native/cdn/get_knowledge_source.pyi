import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKnowledgeSourceResult",
    "AwaitableGetKnowledgeSourceResult",
    "get_knowledge_source",
    "get_knowledge_source_output",
]

@pulumi.output_type
class GetKnowledgeSourceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        id=...,
        last_refreshed_time=...,
        name=...,
        provisioning_state=...,
        source_type=...,
        system_data=...,
        type=...,
        update_frequency=...,
        url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshedTime")
    def last_refreshed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateFrequency")
    def update_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

class AwaitableGetKnowledgeSourceResult(GetKnowledgeSourceResult):
    def __await__(self): ...

def get_knowledge_source(
    knowledge_source_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    web_agent_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKnowledgeSourceResult: ...
def get_knowledge_source_output(
    knowledge_source_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    web_agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKnowledgeSourceResult]: ...
