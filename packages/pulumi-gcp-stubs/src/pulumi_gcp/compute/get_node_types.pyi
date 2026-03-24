import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNodeTypesResult",
    "AwaitableGetNodeTypesResult",
    "get_node_types",
    "get_node_types_output",
]

@pulumi.output_type
class GetNodeTypesResult:
    def __init__(__self__, id=..., names=..., project=..., zone=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

class AwaitableGetNodeTypesResult(GetNodeTypesResult):
    def __await__(self): ...

def get_node_types(
    project: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNodeTypesResult: ...
def get_node_types_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNodeTypesResult]: ...
