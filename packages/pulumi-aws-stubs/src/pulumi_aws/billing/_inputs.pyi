import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ViewDataFilterExpressionArgs",
    "ViewDataFilterExpressionArgsDict",
    "ViewDataFilterExpressionDimensionsArgs",
    "ViewDataFilterExpressionDimensionsArgsDict",
    "ViewDataFilterExpressionTagArgs",
    "ViewDataFilterExpressionTagArgsDict",
    "ViewDataFilterExpressionTimeRangeArgs",
    "ViewDataFilterExpressionTimeRangeArgsDict",
    "ViewTimeoutsArgs",
    "ViewTimeoutsArgsDict",
]

class ViewDataFilterExpressionArgsDict(TypedDict):
    dimensions: NotRequired[pulumi.Input[ViewDataFilterExpressionDimensionsArgsDict]]
    tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ViewDataFilterExpressionTagArgsDict]]]
    ]
    time_range: NotRequired[pulumi.Input[ViewDataFilterExpressionTimeRangeArgsDict]]
    ...

@pulumi.input_type
class ViewDataFilterExpressionArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            pulumi.Input[ViewDataFilterExpressionDimensionsArgs]
        ] = ...,
        tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[ViewDataFilterExpressionTagArgs]]]
        ] = ...,
        time_range: Optional[pulumi.Input[ViewDataFilterExpressionTimeRangeArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[ViewDataFilterExpressionDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[ViewDataFilterExpressionDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ViewDataFilterExpressionTagArgs]]]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ViewDataFilterExpressionTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(
        self,
    ) -> Optional[pulumi.Input[ViewDataFilterExpressionTimeRangeArgs]]: ...
    @time_range.setter
    def time_range(
        self, value: Optional[pulumi.Input[ViewDataFilterExpressionTimeRangeArgs]]
    ): ...

class ViewDataFilterExpressionDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class ViewDataFilterExpressionDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ViewDataFilterExpressionTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class ViewDataFilterExpressionTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ViewDataFilterExpressionTimeRangeArgsDict(TypedDict):
    begin_date_inclusive: pulumi.Input[_builtins.str]
    end_date_inclusive: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ViewDataFilterExpressionTimeRangeArgs:
    def __init__(
        __self__,
        *,
        begin_date_inclusive: pulumi.Input[_builtins.str],
        end_date_inclusive: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="beginDateInclusive")
    def begin_date_inclusive(self) -> pulumi.Input[_builtins.str]: ...
    @begin_date_inclusive.setter
    def begin_date_inclusive(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endDateInclusive")
    def end_date_inclusive(self) -> pulumi.Input[_builtins.str]: ...
    @end_date_inclusive.setter
    def end_date_inclusive(self, value: pulumi.Input[_builtins.str]): ...

class ViewTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ViewTimeoutsArgs:
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
