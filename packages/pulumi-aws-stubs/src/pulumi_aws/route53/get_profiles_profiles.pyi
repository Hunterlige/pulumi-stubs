import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProfilesProfilesResult",
    "AwaitableGetProfilesProfilesResult",
    "get_profiles_profiles",
    "get_profiles_profiles_output",
]

@pulumi.output_type
class GetProfilesProfilesResult:
    def __init__(__self__, id=..., profiles=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> Sequence[outputs.GetProfilesProfilesProfileResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetProfilesProfilesResult(GetProfilesProfilesResult):
    def __await__(self): ...

def get_profiles_profiles(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetProfilesProfilesResult: ...
def get_profiles_profiles_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProfilesProfilesResult]: ...
