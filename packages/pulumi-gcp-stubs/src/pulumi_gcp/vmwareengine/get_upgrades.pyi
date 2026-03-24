import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUpgradesResult",
    "AwaitableGetUpgradesResult",
    "get_upgrades",
    "get_upgrades_output",
]

@pulumi.output_type
class GetUpgradesResult:
    def __init__(__self__, id=..., name=..., parent=..., upgrades=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def upgrades(self) -> Sequence[outputs.GetUpgradesUpgradeResult]: ...

class AwaitableGetUpgradesResult(GetUpgradesResult):
    def __await__(self): ...

def get_upgrades(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUpgradesResult: ...
def get_upgrades_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUpgradesResult]: ...
