import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAttachmentsResult",
    "AwaitableGetAttachmentsResult",
    "get_attachments",
    "get_attachments_output",
]

@pulumi.output_type
class GetAttachmentsResult:
    def __init__(
        __self__, filters=..., id=..., ids=..., region=..., tags=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAttachmentsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetAttachmentsResult(GetAttachmentsResult):
    def __await__(self): ...

def get_attachments(
    filters: Optional[
        Sequence[Union[GetAttachmentsFilterArgs, GetAttachmentsFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAttachmentsResult: ...
def get_attachments_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetAttachmentsFilterArgs, GetAttachmentsFilterArgsDict]]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAttachmentsResult]: ...
