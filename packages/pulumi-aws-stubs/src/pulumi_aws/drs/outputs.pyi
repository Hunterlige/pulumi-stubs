import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ReplicationConfigurationTemplatePitPolicy",
    "ReplicationConfigurationTemplateTimeouts",
]

@pulumi.output_type
class ReplicationConfigurationTemplatePitPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interval: _builtins.int,
        retention_duration: _builtins.int,
        units: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
        rule_id: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def units(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ReplicationConfigurationTemplateTimeouts(dict):
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
