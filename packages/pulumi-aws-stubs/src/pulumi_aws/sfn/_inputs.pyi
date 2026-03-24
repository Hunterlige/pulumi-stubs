import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ActivityEncryptionConfigurationArgs",
    "ActivityEncryptionConfigurationArgsDict",
    "AliasRoutingConfigurationArgs",
    "AliasRoutingConfigurationArgsDict",
    "StateMachineEncryptionConfigurationArgs",
    "StateMachineEncryptionConfigurationArgsDict",
    "StateMachineLoggingConfigurationArgs",
    "StateMachineLoggingConfigurationArgsDict",
    "StateMachineTracingConfigurationArgs",
    "StateMachineTracingConfigurationArgsDict",
]

class ActivityEncryptionConfigurationArgsDict(TypedDict):
    kms_data_key_reuse_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ActivityEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @kms_data_key_reuse_period_seconds.setter
    def kms_data_key_reuse_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AliasRoutingConfigurationArgsDict(TypedDict):
    state_machine_version_arn: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class AliasRoutingConfigurationArgs:
    def __init__(
        __self__,
        *,
        state_machine_version_arn: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> pulumi.Input[_builtins.str]: ...
    @state_machine_version_arn.setter
    def state_machine_version_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...

class StateMachineEncryptionConfigurationArgsDict(TypedDict):
    kms_data_key_reuse_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StateMachineEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @kms_data_key_reuse_period_seconds.setter
    def kms_data_key_reuse_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StateMachineLoggingConfigurationArgsDict(TypedDict):
    include_execution_data: NotRequired[pulumi.Input[_builtins.bool]]
    level: NotRequired[pulumi.Input[_builtins.str]]
    log_destination: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StateMachineLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        include_execution_data: Optional[pulumi.Input[_builtins.bool]] = ...,
        level: Optional[pulumi.Input[_builtins.str]] = ...,
        log_destination: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeExecutionData")
    def include_execution_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_execution_data.setter
    def include_execution_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_destination.setter
    def log_destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StateMachineTracingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class StateMachineTracingConfigurationArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
