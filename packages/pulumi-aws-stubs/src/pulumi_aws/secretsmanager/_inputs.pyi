import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SecretReplicaArgs",
    "SecretReplicaArgsDict",
    "SecretRotationRotationRulesArgs",
    "SecretRotationRotationRulesArgsDict",
    "GetSecretsFilterArgs",
    "GetSecretsFilterArgsDict",
]

class SecretReplicaArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    last_accessed_date: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    status_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretReplicaArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_accessed_date: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastAccessedDate")
    def last_accessed_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_accessed_date.setter
    def last_accessed_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecretRotationRotationRulesArgsDict(TypedDict):
    automatically_after_days: NotRequired[pulumi.Input[_builtins.int]]
    duration: NotRequired[pulumi.Input[_builtins.str]]
    schedule_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretRotationRotationRulesArgs:
    def __init__(
        __self__,
        *,
        automatically_after_days: Optional[pulumi.Input[_builtins.int]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticallyAfterDays")
    def automatically_after_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automatically_after_days.setter
    def automatically_after_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetSecretsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetSecretsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
