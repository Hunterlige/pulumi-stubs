import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MapConfiguration",
    "PlaceIndexDataSourceConfiguration",
    "GetMapConfigurationResult",
    "GetPlaceIndexDataSourceConfigurationResult",
]

@pulumi.output_type
class MapConfiguration(dict):
    def __init__(__self__, *, style: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def style(self) -> _builtins.str: ...

@pulumi.output_type
class PlaceIndexDataSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, intended_use: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intendedUse")
    def intended_use(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetMapConfigurationResult(dict):
    def __init__(__self__, *, style: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def style(self) -> _builtins.str: ...

@pulumi.output_type
class GetPlaceIndexDataSourceConfigurationResult(dict):
    def __init__(__self__, *, intended_use: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intendedUse")
    def intended_use(self) -> _builtins.str: ...
