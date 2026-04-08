import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListSkusByProjectResult",
    "AwaitableListSkusByProjectResult",
    "list_skus_by_project",
    "list_skus_by_project_output",
]

@pulumi.output_type
class ListSkusByProjectResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.DevCenterSkuResponse]: ...

class AwaitableListSkusByProjectResult(ListSkusByProjectResult):
    def __await__(self): ...

def list_skus_by_project(
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListSkusByProjectResult: ...
def list_skus_by_project_output(
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListSkusByProjectResult]: ...
