

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InvocationLoggingConfigurationLoggingConfigArgs', ..., ..., ..., ..., ..., ..., ...]
class InvocationLoggingConfigurationLoggingConfigArgsDict(TypedDict):
    cloudwatch_config: NotRequired[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgsDict]]
    embedding_data_delivery_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    image_data_delivery_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    s3_config: NotRequired[pulumi.Input[InvocationLoggingConfigurationLoggingConfigS3ConfigArgsDict]]
    text_data_delivery_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    video_data_delivery_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class InvocationLoggingConfigurationLoggingConfigArgs:
    def __init__(__self__, *, cloudwatch_config: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgs]] = ..., embedding_data_delivery_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., image_data_delivery_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., s3_config: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigS3ConfigArgs]] = ..., text_data_delivery_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., video_data_delivery_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchConfig")
    def cloudwatch_config(self) -> Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgs]]:
        
        ...
    
    @cloudwatch_config.setter
    def cloudwatch_config(self, value: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingDataDeliveryEnabled")
    def embedding_data_delivery_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @embedding_data_delivery_enabled.setter
    def embedding_data_delivery_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageDataDeliveryEnabled")
    def image_data_delivery_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @image_data_delivery_enabled.setter
    def image_data_delivery_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigS3ConfigArgs]]:
        
        ...
    
    @s3_config.setter
    def s3_config(self, value: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigS3ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textDataDeliveryEnabled")
    def text_data_delivery_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @text_data_delivery_enabled.setter
    def text_data_delivery_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoDataDeliveryEnabled")
    def video_data_delivery_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @video_data_delivery_enabled.setter
    def video_data_delivery_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    large_data_delivery_s3_config: NotRequired[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgsDict]]


@pulumi.input_type
class InvocationLoggingConfigurationLoggingConfigCloudwatchConfigArgs:
    def __init__(__self__, *, log_group_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], large_data_delivery_s3_config: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeDataDeliveryS3Config")
    def large_data_delivery_s3_config(self) -> Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgs]]:
        
        ...
    
    @large_data_delivery_s3_config.setter
    def large_data_delivery_s3_config(self, value: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgs]]): # -> None:
        ...
    


class InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InvocationLoggingConfigurationLoggingConfigCloudwatchConfigLargeDataDeliveryS3ConfigArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InvocationLoggingConfigurationLoggingConfigS3ConfigArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InvocationLoggingConfigurationLoggingConfigS3ConfigArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


