import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectivityTestRunResult",
    "AwaitableGetConnectivityTestRunResult",
    "get_connectivity_test_run",
    "get_connectivity_test_run_output",
]

@pulumi.output_type
class GetConnectivityTestRunResult:
    def __init__(
        __self__, id=..., name=..., project=..., reachability_details=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reachabilityDetails")
    def reachability_details(
        self,
    ) -> Sequence[outputs.GetConnectivityTestRunReachabilityDetailResult]: ...

class AwaitableGetConnectivityTestRunResult(GetConnectivityTestRunResult):
    def __await__(self): ...

def get_connectivity_test_run(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectivityTestRunResult: ...
def get_connectivity_test_run_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectivityTestRunResult]: ...
