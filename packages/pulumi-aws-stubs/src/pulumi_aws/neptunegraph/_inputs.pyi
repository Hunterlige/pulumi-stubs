import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GraphTimeoutsArgs",
    "GraphTimeoutsArgsDict",
    "GraphVectorSearchConfigurationArgs",
    "GraphVectorSearchConfigurationArgsDict",
]

class GraphTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GraphTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GraphVectorSearchConfigurationArgsDict(TypedDict):
    vector_search_dimension: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GraphVectorSearchConfigurationArgs:
    def __init__(
        __self__,
        *,
        vector_search_dimension: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchDimension")
    def vector_search_dimension(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vector_search_dimension.setter
    def vector_search_dimension(self, value: Optional[pulumi.Input[_builtins.int]]): ...
