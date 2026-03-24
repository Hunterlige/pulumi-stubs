import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppregistryAttributeGroupAssociationsResult",
    ...,
    "get_appregistry_attribute_group_associations",
    ...,
]

@pulumi.output_type
class GetAppregistryAttributeGroupAssociationsResult:
    def __init__(
        __self__, attribute_group_ids=..., id=..., name=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeGroupIds")
    def attribute_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetAppregistryAttributeGroupAssociationsResult(
    GetAppregistryAttributeGroupAssociationsResult
):
    def __await__(self): ...

def get_appregistry_attribute_group_associations(
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppregistryAttributeGroupAssociationsResult: ...
def get_appregistry_attribute_group_associations_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppregistryAttributeGroupAssociationsResult]: ...
