import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFunctionsResult",
    "AwaitableGetFunctionsResult",
    "get_functions",
    "get_functions_output",
]

@pulumi.output_type
class GetFunctionsResult:
    def __init__(
        __self__, function_arns=..., function_names=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArns")
    def function_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionNames")
    def function_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetFunctionsResult(GetFunctionsResult):
    def __await__(self): ...

def get_functions(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetFunctionsResult: ...
def get_functions_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFunctionsResult]: ...
