import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrincipalsArgs", "PrincipalsArgsDict"]

class PrincipalsArgsDict(TypedDict):
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    upn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrincipalsArgs:
    def __init__(
        __self__,
        *,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        upn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def upn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upn.setter
    def upn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
