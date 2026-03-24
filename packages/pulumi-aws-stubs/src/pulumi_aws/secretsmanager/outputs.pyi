import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SecretReplica",
    "SecretRotationRotationRules",
    "GetSecretRotationRotationRuleResult",
    "GetSecretVersionsVersionResult",
    "GetSecretsFilterResult",
]

@pulumi.output_type
class SecretReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
        last_accessed_date: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        status_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastAccessedDate")
    def last_accessed_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecretRotationRotationRules(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        automatically_after_days: Optional[_builtins.int] = ...,
        duration: Optional[_builtins.str] = ...,
        schedule_expression: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticallyAfterDays")
    def automatically_after_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetSecretRotationRotationRuleResult(dict):
    def __init__(
        __self__,
        *,
        automatically_after_days: _builtins.int,
        duration: _builtins.str,
        schedule_expression: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticallyAfterDays")
    def automatically_after_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetSecretVersionsVersionResult(dict):
    def __init__(
        __self__,
        *,
        created_time: _builtins.str,
        last_accessed_date: _builtins.str,
        version_id: _builtins.str,
        version_stages: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastAccessedDate")
    def last_accessed_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionStages")
    def version_stages(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetSecretsFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
