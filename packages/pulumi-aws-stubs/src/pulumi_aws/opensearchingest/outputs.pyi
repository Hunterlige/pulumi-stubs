

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PipelineBufferOptions', 'PipelineEncryptionAtRestOptions', 'PipelineLogPublishingOptions', ..., 'PipelineTimeouts', 'PipelineVpcOptions']
@pulumi.output_type
class PipelineBufferOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, persistent_buffer_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentBufferEnabled")
    def persistent_buffer_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class PipelineEncryptionAtRestOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipelineLogPublishingOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_log_destination: Optional[outputs.PipelineLogPublishingOptionsCloudwatchLogDestination] = ..., is_logging_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogDestination")
    def cloudwatch_log_destination(self) -> Optional[outputs.PipelineLogPublishingOptionsCloudwatchLogDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLoggingEnabled")
    def is_logging_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PipelineLogPublishingOptionsCloudwatchLogDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipelineTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineVpcOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_ids: Sequence[_builtins.str], security_group_ids: Optional[Sequence[_builtins.str]] = ..., vpc_endpoint_management: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointManagement")
    def vpc_endpoint_management(self) -> Optional[_builtins.str]:
        
        ...
    


