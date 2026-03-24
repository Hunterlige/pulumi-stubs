import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResourceCollectionResult",
    "AwaitableGetResourceCollectionResult",
    "get_resource_collection",
    "get_resource_collection_output",
]

@pulumi.output_type
class GetResourceCollectionResult:
    def __init__(
        __self__, cloudformations=..., id=..., region=..., tags=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cloudformations(
        self,
    ) -> Sequence[outputs.GetResourceCollectionCloudformationResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetResourceCollectionTagResult]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetResourceCollectionResult(GetResourceCollectionResult):
    def __await__(self): ...

def get_resource_collection(
    region: Optional[_builtins.str] = ...,
    type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResourceCollectionResult: ...
def get_resource_collection_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    type: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResourceCollectionResult]: ...
