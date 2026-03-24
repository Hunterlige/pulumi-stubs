

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RecordingConfigurationDestinationConfiguration', 'RecordingConfigurationDestinationConfigurationS3', 'RecordingConfigurationThumbnailConfiguration']
@pulumi.output_type
class RecordingConfigurationDestinationConfiguration(dict):
    def __init__(__self__, *, s3: outputs.RecordingConfigurationDestinationConfigurationS3) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> outputs.RecordingConfigurationDestinationConfigurationS3:
        
        ...
    


@pulumi.output_type
class RecordingConfigurationDestinationConfigurationS3(dict):
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
class RecordingConfigurationThumbnailConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recording_mode: Optional[_builtins.str] = ..., target_interval_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIntervalSeconds")
    def target_interval_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


