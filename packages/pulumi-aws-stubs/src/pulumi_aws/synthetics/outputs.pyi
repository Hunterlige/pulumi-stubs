

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CanaryArtifactConfig', 'CanaryArtifactConfigS3Encryption', 'CanaryRunConfig', 'CanarySchedule', 'CanaryScheduleRetryConfig', 'CanaryTimeline', 'CanaryVpcConfig', 'GetRuntimeVersionsRuntimeVersionResult']
@pulumi.output_type
class CanaryArtifactConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, s3_encryption: Optional[outputs.CanaryArtifactConfigS3Encryption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(self) -> Optional[outputs.CanaryArtifactConfigS3Encryption]:
        
        ...
    


@pulumi.output_type
class CanaryArtifactConfigS3Encryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_mode: Optional[_builtins.str] = ..., kms_key_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CanaryRunConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_tracing: Optional[_builtins.bool] = ..., environment_variables: Optional[Mapping[str, _builtins.str]] = ..., ephemeral_storage: Optional[_builtins.int] = ..., memory_in_mb: Optional[_builtins.int] = ..., timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeTracing")
    def active_tracing(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInMb")
    def memory_in_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CanarySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression: _builtins.str, duration_in_seconds: Optional[_builtins.int] = ..., retry_config: Optional[outputs.CanaryScheduleRetryConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[outputs.CanaryScheduleRetryConfig]:
        
        ...
    


@pulumi.output_type
class CanaryScheduleRetryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_retries: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class CanaryTimeline(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created: Optional[_builtins.str] = ..., last_modified: Optional[_builtins.str] = ..., last_started: Optional[_builtins.str] = ..., last_stopped: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStarted")
    def last_started(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStopped")
    def last_stopped(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CanaryVpcConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ipv6_allowed_for_dual_stack: Optional[_builtins.bool] = ..., security_group_ids: Optional[Sequence[_builtins.str]] = ..., subnet_ids: Optional[Sequence[_builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AllowedForDualStack")
    def ipv6_allowed_for_dual_stack(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRuntimeVersionsRuntimeVersionResult(dict):
    def __init__(__self__, *, deprecation_date: _builtins.str, description: _builtins.str, release_date: _builtins.str, version_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deprecationDate")
    def deprecation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseDate")
    def release_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str:
        
        ...
    


