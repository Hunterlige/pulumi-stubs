import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetInputResult", "AwaitableGetInputResult", "get_input", "get_input_output"]

@pulumi.output_type
class GetInputResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetInputResult(GetInputResult):
    def __await__(self): ...

def get_input(
    input_name: Optional[_builtins.str] = ...,
    job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInputResult: ...
def get_input_output(
    input_name: Optional[pulumi.Input[_builtins.str]] = ...,
    job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInputResult]: ...
