import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectivityTestsResult",
    "AwaitableGetConnectivityTestsResult",
    "get_connectivity_tests",
    "get_connectivity_tests_output",
]

@pulumi.output_type
class GetConnectivityTestsResult:
    def __init__(
        __self__, connectivity_tests=..., filter=..., id=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectivityTests")
    def connectivity_tests(
        self,
    ) -> Sequence[outputs.GetConnectivityTestsConnectivityTestResult]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetConnectivityTestsResult(GetConnectivityTestsResult):
    def __await__(self): ...

def get_connectivity_tests(
    filter: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectivityTestsResult: ...
def get_connectivity_tests_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectivityTestsResult]: ...
