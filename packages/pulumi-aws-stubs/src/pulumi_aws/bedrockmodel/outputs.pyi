

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InvocationLoggingConfigurationLoggingConfig', ..., ..., ...]
@pulumi.output_type
class InvocationLoggingConfigurationLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_config: Optional[outputs.InvocationLoggingConfigurationLoggingConfigCloudwatchConfig] = ..., embedding_data_delivery_enabled: Optional[_builtins.bool] = ..., image_data_delivery_enabled: Optional[_builtins.bool] = ..., s3_config: Optional[outputs.InvocationLoggingConfigurationLoggingConfigS3Config] = ..., text_data_delivery_enabled: Optional[_builtins.bool] = ..., video_data_delivery_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchConfig")
    def cloudwatch_config(self) -> Optional[outputs.InvocationLoggingConfigurationLoggingConfigCloudwatchConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingDataDeliveryEnabled")
    def embedding_data_delivery_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageDataDeliveryEnabled")
    def image_data_delivery_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> Optional[outputs.InvocationLoggingConfigurationLoggingConfigS3Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textDataDeliveryEnabled")
    def text_data_delivery_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoDataDeliveryEnabled")
    def video_data_delivery_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InvocationLoggingConfigurationLoggingConfigCloudwatchConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name: _builtins.str, role_arn: _builtins.str, large_data_delivery_s3_config: Optional[outputs.InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3Config] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeDataDeliveryS3Config")
    def large_data_delivery_s3_config(self) -> Optional[outputs.InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3Config]:
        
        ...
    


@pulumi.output_type
class InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, key_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InvocationLoggingConfigurationLoggingConfigS3Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, key_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


