import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupScheduleDailyRecurrenceArgs",
    "BackupScheduleDailyRecurrenceArgsDict",
    "BackupScheduleWeeklyRecurrenceArgs",
    "BackupScheduleWeeklyRecurrenceArgsDict",
    "DatabaseCmekConfigArgs",
    "DatabaseCmekConfigArgsDict",
    "FieldIndexConfigArgs",
    "FieldIndexConfigArgsDict",
    "FieldIndexConfigIndexArgs",
    "FieldIndexConfigIndexArgsDict",
    "FieldTtlConfigArgs",
    "FieldTtlConfigArgsDict",
    "IndexFieldArgs",
    "IndexFieldArgsDict",
    "IndexFieldVectorConfigArgs",
    "IndexFieldVectorConfigArgsDict",
    "IndexFieldVectorConfigFlatArgs",
    "IndexFieldVectorConfigFlatArgsDict",
    "UserCredsResourceIdentityArgs",
    "UserCredsResourceIdentityArgsDict",
]

class BackupScheduleDailyRecurrenceArgsDict(TypedDict): ...

@pulumi.input_type
class BackupScheduleDailyRecurrenceArgs:
    def __init__(__self__) -> None: ...

class BackupScheduleWeeklyRecurrenceArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BackupScheduleWeeklyRecurrenceArgs:
    def __init__(
        __self__, *, day: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatabaseCmekConfigArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    active_key_versions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class DatabaseCmekConfigArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        active_key_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activeKeyVersions")
    def active_key_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @active_key_versions.setter
    def active_key_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FieldIndexConfigArgsDict(TypedDict):
    indexes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FieldIndexConfigIndexArgsDict]]]
    ]
    ...

@pulumi.input_type
class FieldIndexConfigArgs:
    def __init__(
        __self__,
        *,
        indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[FieldIndexConfigIndexArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FieldIndexConfigIndexArgs]]]]: ...
    @indexes.setter
    def indexes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FieldIndexConfigIndexArgs]]]
        ],
    ): ...

class FieldIndexConfigIndexArgsDict(TypedDict):
    array_config: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.str]]
    query_scope: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FieldIndexConfigIndexArgs:
    def __init__(
        __self__,
        *,
        array_config: Optional[pulumi.Input[_builtins.str]] = ...,
        order: Optional[pulumi.Input[_builtins.str]] = ...,
        query_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arrayConfig")
    def array_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @array_config.setter
    def array_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_scope.setter
    def query_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FieldTtlConfigArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FieldTtlConfigArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexFieldArgsDict(TypedDict):
    array_config: NotRequired[pulumi.Input[_builtins.str]]
    field_path: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.str]]
    vector_config: NotRequired[pulumi.Input[IndexFieldVectorConfigArgsDict]]
    ...

@pulumi.input_type
class IndexFieldArgs:
    def __init__(
        __self__,
        *,
        array_config: Optional[pulumi.Input[_builtins.str]] = ...,
        field_path: Optional[pulumi.Input[_builtins.str]] = ...,
        order: Optional[pulumi.Input[_builtins.str]] = ...,
        vector_config: Optional[pulumi.Input[IndexFieldVectorConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arrayConfig")
    def array_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @array_config.setter
    def array_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_path.setter
    def field_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorConfig")
    def vector_config(self) -> Optional[pulumi.Input[IndexFieldVectorConfigArgs]]: ...
    @vector_config.setter
    def vector_config(
        self, value: Optional[pulumi.Input[IndexFieldVectorConfigArgs]]
    ): ...

class IndexFieldVectorConfigArgsDict(TypedDict):
    dimension: NotRequired[pulumi.Input[_builtins.int]]
    flat: NotRequired[pulumi.Input[IndexFieldVectorConfigFlatArgsDict]]
    ...

@pulumi.input_type
class IndexFieldVectorConfigArgs:
    def __init__(
        __self__,
        *,
        dimension: Optional[pulumi.Input[_builtins.int]] = ...,
        flat: Optional[pulumi.Input[IndexFieldVectorConfigFlatArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def flat(self) -> Optional[pulumi.Input[IndexFieldVectorConfigFlatArgs]]: ...
    @flat.setter
    def flat(self, value: Optional[pulumi.Input[IndexFieldVectorConfigFlatArgs]]): ...

class IndexFieldVectorConfigFlatArgsDict(TypedDict): ...

@pulumi.input_type
class IndexFieldVectorConfigFlatArgs:
    def __init__(__self__) -> None: ...

class UserCredsResourceIdentityArgsDict(TypedDict):
    principal: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class UserCredsResourceIdentityArgs:
    def __init__(
        __self__, *, principal: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
