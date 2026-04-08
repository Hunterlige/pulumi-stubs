import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAgentResult",
    "AwaitableGetWebAgentResult",
    "get_web_agent",
    "get_web_agent_output",
]

@pulumi.output_type
class GetWebAgentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        id=...,
        location=...,
        name=...,
        paths=...,
        profile_agent_links=...,
        provisioning_state=...,
        system_data=...,
        system_prompt=...,
        tags=...,
        type=...,
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
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[outputs.AgentPathResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="profileAgentLinks")
    def profile_agent_links(self) -> Sequence[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemPrompt")
    def system_prompt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAgentResult(GetWebAgentResult):
    def __await__(self): ...

def get_web_agent(
    resource_group_name: Optional[_builtins.str] = ...,
    web_agent_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAgentResult: ...
def get_web_agent_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    web_agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAgentResult]: ...
