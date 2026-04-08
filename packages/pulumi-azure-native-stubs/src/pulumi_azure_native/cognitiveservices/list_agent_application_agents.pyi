import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAgentApplicationAgentsResult",
    "AwaitableListAgentApplicationAgentsResult",
    "list_agent_application_agents",
    "list_agent_application_agents_output",
]

@pulumi.output_type
class ListAgentApplicationAgentsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.AgentReferenceResponse]]: ...

class AwaitableListAgentApplicationAgentsResult(ListAgentApplicationAgentsResult):
    def __await__(self): ...

def list_agent_application_agents(
    account_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAgentApplicationAgentsResult: ...
def list_agent_application_agents_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAgentApplicationAgentsResult]: ...
