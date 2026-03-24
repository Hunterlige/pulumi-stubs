import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUserHierarchyStructureResult",
    "AwaitableGetUserHierarchyStructureResult",
    "get_user_hierarchy_structure",
    "get_user_hierarchy_structure_output",
]

@pulumi.output_type
class GetUserHierarchyStructureResult:
    def __init__(
        __self__, hierarchy_structures=..., id=..., instance_id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyStructures")
    def hierarchy_structures(
        self,
    ) -> Sequence[outputs.GetUserHierarchyStructureHierarchyStructureResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetUserHierarchyStructureResult(GetUserHierarchyStructureResult):
    def __await__(self): ...

def get_user_hierarchy_structure(
    instance_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserHierarchyStructureResult: ...
def get_user_hierarchy_structure_output(
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserHierarchyStructureResult]: ...
