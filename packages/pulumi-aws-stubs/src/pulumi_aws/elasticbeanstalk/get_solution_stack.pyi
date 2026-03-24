import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSolutionStackResult",
    "AwaitableGetSolutionStackResult",
    "get_solution_stack",
    "get_solution_stack_output",
]

@pulumi.output_type
class GetSolutionStackResult:
    def __init__(
        __self__, id=..., most_recent=..., name=..., name_regex=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetSolutionStackResult(GetSolutionStackResult):
    def __await__(self): ...

def get_solution_stack(
    most_recent: Optional[_builtins.bool] = ...,
    name_regex: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSolutionStackResult: ...
def get_solution_stack_output(
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSolutionStackResult]: ...
