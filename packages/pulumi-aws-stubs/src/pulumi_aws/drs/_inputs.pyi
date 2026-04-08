import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ReplicationConfigurationTemplatePitPolicyArgs",
    "ReplicationConfigurationTemplatePitPolicyArgsDict",
    "ReplicationConfigurationTemplateTimeoutsArgs",
    "ReplicationConfigurationTemplateTimeoutsArgsDict",
]

class ReplicationConfigurationTemplatePitPolicyArgsDict(TypedDict):
    interval: pulumi.Input[_builtins.int]
    retention_duration: pulumi.Input[_builtins.int]
    units: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    rule_id: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ReplicationConfigurationTemplatePitPolicyArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.int],
        retention_duration: pulumi.Input[_builtins.int],
        units: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> pulumi.Input[_builtins.int]: ...
    @retention_duration.setter
    def retention_duration(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def units(self) -> pulumi.Input[_builtins.str]: ...
    @units.setter
    def units(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ReplicationConfigurationTemplateTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReplicationConfigurationTemplateTimeoutsArgs:
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
