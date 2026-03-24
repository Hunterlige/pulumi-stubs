import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrganizationalUnitResult",
    "AwaitableGetOrganizationalUnitResult",
    "get_organizational_unit",
    "get_organizational_unit_output",
]

@pulumi.output_type
class GetOrganizationalUnitResult:
    def __init__(__self__, arn=..., id=..., name=..., parent_id=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str: ...

class AwaitableGetOrganizationalUnitResult(GetOrganizationalUnitResult):
    def __await__(self): ...

def get_organizational_unit(
    name: Optional[_builtins.str] = ...,
    parent_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrganizationalUnitResult: ...
def get_organizational_unit_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrganizationalUnitResult]: ...
