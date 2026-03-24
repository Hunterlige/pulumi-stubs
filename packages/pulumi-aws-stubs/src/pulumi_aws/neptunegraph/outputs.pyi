import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GraphTimeouts", "GraphVectorSearchConfiguration"]

@pulumi.output_type
class GraphTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GraphVectorSearchConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, vector_search_dimension: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchDimension")
    def vector_search_dimension(self) -> Optional[_builtins.int]: ...
