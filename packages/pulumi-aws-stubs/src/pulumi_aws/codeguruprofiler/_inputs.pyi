import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProfilingGroupAgentOrchestrationConfigArgs",
    "ProfilingGroupAgentOrchestrationConfigArgsDict",
]

class ProfilingGroupAgentOrchestrationConfigArgsDict(TypedDict):
    profiling_enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ProfilingGroupAgentOrchestrationConfigArgs:
    def __init__(
        __self__, *, profiling_enabled: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profilingEnabled")
    def profiling_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @profiling_enabled.setter
    def profiling_enabled(self, value: pulumi.Input[_builtins.bool]): ...
