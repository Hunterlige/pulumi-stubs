import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAnnouncementsResult",
    "AwaitableGetAnnouncementsResult",
    "get_announcements",
    "get_announcements_output",
]

@pulumi.output_type
class GetAnnouncementsResult:
    def __init__(__self__, announcements=..., id=..., name=..., parent=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def announcements(self) -> Sequence[outputs.GetAnnouncementsAnnouncementResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...

class AwaitableGetAnnouncementsResult(GetAnnouncementsResult):
    def __await__(self): ...

def get_announcements(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAnnouncementsResult: ...
def get_announcements_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAnnouncementsResult]: ...
