import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStandardsControlAssociationsResult",
    "AwaitableGetStandardsControlAssociationsResult",
    "get_standards_control_associations",
    "get_standards_control_associations_output",
]

@pulumi.output_type
class GetStandardsControlAssociationsResult:
    def __init__(
        __self__,
        id=...,
        region=...,
        security_control_id=...,
        standards_control_associations=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standardsControlAssociations")
    def standards_control_associations(
        self,
    ) -> Sequence[
        outputs.GetStandardsControlAssociationsStandardsControlAssociationResult
    ]: ...

class AwaitableGetStandardsControlAssociationsResult(
    GetStandardsControlAssociationsResult
):
    def __await__(self): ...

def get_standards_control_associations(
    region: Optional[_builtins.str] = ...,
    security_control_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStandardsControlAssociationsResult: ...
def get_standards_control_associations_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    security_control_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStandardsControlAssociationsResult]: ...
