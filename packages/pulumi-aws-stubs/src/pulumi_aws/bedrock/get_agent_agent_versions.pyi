import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAgentAgentVersionsResult",
    "AwaitableGetAgentAgentVersionsResult",
    "get_agent_agent_versions",
    "get_agent_agent_versions_output",
]

@pulumi.output_type
class GetAgentAgentVersionsResult:
    def __init__(
        __self__, agent_id=..., agent_version_summaries=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentVersionSummaries")
    def agent_version_summaries(
        self,
    ) -> Optional[Sequence[outputs.GetAgentAgentVersionsAgentVersionSummaryResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetAgentAgentVersionsResult(GetAgentAgentVersionsResult):
    def __await__(self): ...

def get_agent_agent_versions(
    agent_id: Optional[_builtins.str] = ...,
    agent_version_summaries: Optional[
        Sequence[
            Union[
                GetAgentAgentVersionsAgentVersionSummaryArgs,
                GetAgentAgentVersionsAgentVersionSummaryArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAgentAgentVersionsResult: ...
def get_agent_agent_versions_output(
    agent_id: Optional[pulumi.Input[_builtins.str]] = ...,
    agent_version_summaries: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetAgentAgentVersionsAgentVersionSummaryArgs,
                        GetAgentAgentVersionsAgentVersionSummaryArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAgentAgentVersionsResult]: ...
