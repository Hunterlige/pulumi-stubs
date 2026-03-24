

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoggingConfigurationDestinationConfiguration', ..., ..., 'LoggingConfigurationDestinationConfigurationS3', 'RoomMessageReviewHandler']
@pulumi.output_type
class LoggingConfigurationDestinationConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_logs: Optional[outputs.LoggingConfigurationDestinationConfigurationCloudwatchLogs] = ..., firehose: Optional[outputs.LoggingConfigurationDestinationConfigurationFirehose] = ..., s3: Optional[outputs.LoggingConfigurationDestinationConfigurationS3] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[outputs.LoggingConfigurationDestinationConfigurationCloudwatchLogs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[outputs.LoggingConfigurationDestinationConfigurationFirehose]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.LoggingConfigurationDestinationConfigurationS3]:
        
        ...
    


@pulumi.output_type
class LoggingConfigurationDestinationConfigurationCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LoggingConfigurationDestinationConfigurationFirehose(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delivery_stream_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LoggingConfigurationDestinationConfigurationS3(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RoomMessageReviewHandler(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_result: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackResult")
    def fallback_result(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


