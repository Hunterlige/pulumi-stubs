import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUserWorkloadsConfigMapResult",
    "AwaitableGetUserWorkloadsConfigMapResult",
    "get_user_workloads_config_map",
    "get_user_workloads_config_map_output",
]

@pulumi.output_type
class GetUserWorkloadsConfigMapResult:
    def __init__(
        __self__, data=..., environment=..., id=..., name=..., project=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

class AwaitableGetUserWorkloadsConfigMapResult(GetUserWorkloadsConfigMapResult):
    def __await__(self): ...

def get_user_workloads_config_map(
    environment: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserWorkloadsConfigMapResult: ...
def get_user_workloads_config_map_output(
    environment: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserWorkloadsConfigMapResult]: ...
