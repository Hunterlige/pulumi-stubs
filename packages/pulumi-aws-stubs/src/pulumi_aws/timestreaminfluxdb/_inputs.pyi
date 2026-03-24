

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DbClusterLogDeliveryConfigurationArgs', 'DbClusterLogDeliveryConfigurationArgsDict', ..., ..., 'DbClusterTimeoutsArgs', 'DbClusterTimeoutsArgsDict', 'DbInstanceLogDeliveryConfigurationArgs', 'DbInstanceLogDeliveryConfigurationArgsDict', ..., ..., 'DbInstanceTimeoutsArgs', 'DbInstanceTimeoutsArgsDict']
class DbClusterLogDeliveryConfigurationArgsDict(TypedDict):
    s3_configuration: NotRequired[pulumi.Input[DbClusterLogDeliveryConfigurationS3ConfigurationArgsDict]]


@pulumi.input_type
class DbClusterLogDeliveryConfigurationArgs:
    def __init__(__self__, *, s3_configuration: Optional[pulumi.Input[DbClusterLogDeliveryConfigurationS3ConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[pulumi.Input[DbClusterLogDeliveryConfigurationS3ConfigurationArgs]]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: Optional[pulumi.Input[DbClusterLogDeliveryConfigurationS3ConfigurationArgs]]): # -> None:
        ...
    


class DbClusterLogDeliveryConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class DbClusterLogDeliveryConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class DbClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DbClusterTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DbInstanceLogDeliveryConfigurationArgsDict(TypedDict):
    s3_configuration: NotRequired[pulumi.Input[DbInstanceLogDeliveryConfigurationS3ConfigurationArgsDict]]


@pulumi.input_type
class DbInstanceLogDeliveryConfigurationArgs:
    def __init__(__self__, *, s3_configuration: Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationS3ConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationS3ConfigurationArgs]]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationS3ConfigurationArgs]]): # -> None:
        ...
    


class DbInstanceLogDeliveryConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class DbInstanceLogDeliveryConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class DbInstanceTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DbInstanceTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


