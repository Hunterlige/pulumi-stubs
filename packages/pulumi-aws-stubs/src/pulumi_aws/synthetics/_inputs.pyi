

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CanaryArtifactConfigArgs', 'CanaryArtifactConfigArgsDict', 'CanaryArtifactConfigS3EncryptionArgs', 'CanaryArtifactConfigS3EncryptionArgsDict', 'CanaryRunConfigArgs', 'CanaryRunConfigArgsDict', 'CanaryScheduleArgs', 'CanaryScheduleArgsDict', 'CanaryScheduleRetryConfigArgs', 'CanaryScheduleRetryConfigArgsDict', 'CanaryTimelineArgs', 'CanaryTimelineArgsDict', 'CanaryVpcConfigArgs', 'CanaryVpcConfigArgsDict']
class CanaryArtifactConfigArgsDict(TypedDict):
    s3_encryption: NotRequired[pulumi.Input[CanaryArtifactConfigS3EncryptionArgsDict]]


@pulumi.input_type
class CanaryArtifactConfigArgs:
    def __init__(__self__, *, s3_encryption: Optional[pulumi.Input[CanaryArtifactConfigS3EncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(self) -> Optional[pulumi.Input[CanaryArtifactConfigS3EncryptionArgs]]:
        
        ...
    
    @s3_encryption.setter
    def s3_encryption(self, value: Optional[pulumi.Input[CanaryArtifactConfigS3EncryptionArgs]]): # -> None:
        ...
    


class CanaryArtifactConfigS3EncryptionArgsDict(TypedDict):
    encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CanaryArtifactConfigS3EncryptionArgs:
    def __init__(__self__, *, encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CanaryRunConfigArgsDict(TypedDict):
    active_tracing: NotRequired[pulumi.Input[_builtins.bool]]
    environment_variables: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ephemeral_storage: NotRequired[pulumi.Input[_builtins.int]]
    memory_in_mb: NotRequired[pulumi.Input[_builtins.int]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CanaryRunConfigArgs:
    def __init__(__self__, *, active_tracing: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ephemeral_storage: Optional[pulumi.Input[_builtins.int]] = ..., memory_in_mb: Optional[pulumi.Input[_builtins.int]] = ..., timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeTracing")
    def active_tracing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @active_tracing.setter
    def active_tracing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInMb")
    def memory_in_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_in_mb.setter
    def memory_in_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CanaryScheduleArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    duration_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    retry_config: NotRequired[pulumi.Input[CanaryScheduleRetryConfigArgsDict]]


@pulumi.input_type
class CanaryScheduleArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., retry_config: Optional[pulumi.Input[CanaryScheduleRetryConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration_in_seconds.setter
    def duration_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[pulumi.Input[CanaryScheduleRetryConfigArgs]]:
        
        ...
    
    @retry_config.setter
    def retry_config(self, value: Optional[pulumi.Input[CanaryScheduleRetryConfigArgs]]): # -> None:
        ...
    


class CanaryScheduleRetryConfigArgsDict(TypedDict):
    max_retries: pulumi.Input[_builtins.int]


@pulumi.input_type
class CanaryScheduleRetryConfigArgs:
    def __init__(__self__, *, max_retries: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_retries.setter
    def max_retries(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class CanaryTimelineArgsDict(TypedDict):
    created: NotRequired[pulumi.Input[_builtins.str]]
    last_modified: NotRequired[pulumi.Input[_builtins.str]]
    last_started: NotRequired[pulumi.Input[_builtins.str]]
    last_stopped: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CanaryTimelineArgs:
    def __init__(__self__, *, created: Optional[pulumi.Input[_builtins.str]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., last_started: Optional[pulumi.Input[_builtins.str]] = ..., last_stopped: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created.setter
    def created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStarted")
    def last_started(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_started.setter
    def last_started(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStopped")
    def last_stopped(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_stopped.setter
    def last_stopped(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CanaryVpcConfigArgsDict(TypedDict):
    ipv6_allowed_for_dual_stack: NotRequired[pulumi.Input[_builtins.bool]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CanaryVpcConfigArgs:
    def __init__(__self__, *, ipv6_allowed_for_dual_stack: Optional[pulumi.Input[_builtins.bool]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AllowedForDualStack")
    def ipv6_allowed_for_dual_stack(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv6_allowed_for_dual_stack.setter
    def ipv6_allowed_for_dual_stack(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


