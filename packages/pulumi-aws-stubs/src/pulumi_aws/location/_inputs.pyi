import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MapConfigurationArgs",
    "MapConfigurationArgsDict",
    "PlaceIndexDataSourceConfigurationArgs",
    "PlaceIndexDataSourceConfigurationArgsDict",
]

class MapConfigurationArgsDict(TypedDict):
    style: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class MapConfigurationArgs:
    def __init__(__self__, *, style: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def style(self) -> pulumi.Input[_builtins.str]: ...
    @style.setter
    def style(self, value: pulumi.Input[_builtins.str]): ...

class PlaceIndexDataSourceConfigurationArgsDict(TypedDict):
    intended_use: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlaceIndexDataSourceConfigurationArgs:
    def __init__(
        __self__, *, intended_use: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intendedUse")
    def intended_use(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @intended_use.setter
    def intended_use(self, value: Optional[pulumi.Input[_builtins.str]]): ...
