

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ActivityEncryptionConfiguration', 'AliasRoutingConfiguration', 'StateMachineEncryptionConfiguration', 'StateMachineLoggingConfiguration', 'StateMachineTracingConfiguration', 'GetAliasRoutingConfigurationResult']
@pulumi.output_type
class ActivityEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_data_key_reuse_period_seconds: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AliasRoutingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state_machine_version_arn: _builtins.str, weight: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class StateMachineEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_data_key_reuse_period_seconds: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StateMachineLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_execution_data: Optional[_builtins.bool] = ..., level: Optional[_builtins.str] = ..., log_destination: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeExecutionData")
    def include_execution_data(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StateMachineTracingConfiguration(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GetAliasRoutingConfigurationResult(dict):
    def __init__(__self__, *, state_machine_version_arn: _builtins.str, weight: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        ...
    


