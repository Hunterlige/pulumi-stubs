

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PipelineBufferOptionsArgs', 'PipelineBufferOptionsArgsDict', 'PipelineEncryptionAtRestOptionsArgs', 'PipelineEncryptionAtRestOptionsArgsDict', 'PipelineLogPublishingOptionsArgs', 'PipelineLogPublishingOptionsArgsDict', ..., ..., 'PipelineTimeoutsArgs', 'PipelineTimeoutsArgsDict', 'PipelineVpcOptionsArgs', 'PipelineVpcOptionsArgsDict']
class PipelineBufferOptionsArgsDict(TypedDict):
    persistent_buffer_enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class PipelineBufferOptionsArgs:
    def __init__(__self__, *, persistent_buffer_enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentBufferEnabled")
    def persistent_buffer_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @persistent_buffer_enabled.setter
    def persistent_buffer_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class PipelineEncryptionAtRestOptionsArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class PipelineEncryptionAtRestOptionsArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PipelineLogPublishingOptionsArgsDict(TypedDict):
    cloudwatch_log_destination: NotRequired[pulumi.Input[PipelineLogPublishingOptionsCloudwatchLogDestinationArgsDict]]
    is_logging_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class PipelineLogPublishingOptionsArgs:
    def __init__(__self__, *, cloudwatch_log_destination: Optional[pulumi.Input[PipelineLogPublishingOptionsCloudwatchLogDestinationArgs]] = ..., is_logging_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogDestination")
    def cloudwatch_log_destination(self) -> Optional[pulumi.Input[PipelineLogPublishingOptionsCloudwatchLogDestinationArgs]]:
        
        ...
    
    @cloudwatch_log_destination.setter
    def cloudwatch_log_destination(self, value: Optional[pulumi.Input[PipelineLogPublishingOptionsCloudwatchLogDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLoggingEnabled")
    def is_logging_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_logging_enabled.setter
    def is_logging_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class PipelineLogPublishingOptionsCloudwatchLogDestinationArgsDict(TypedDict):
    log_group: pulumi.Input[_builtins.str]


@pulumi.input_type
class PipelineLogPublishingOptionsCloudwatchLogDestinationArgs:
    def __init__(__self__, *, log_group: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group.setter
    def log_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PipelineTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PipelineTimeoutsArgs:
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
    


class PipelineVpcOptionsArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_endpoint_management: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PipelineVpcOptionsArgs:
    def __init__(__self__, *, subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_endpoint_management: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointManagement")
    def vpc_endpoint_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_management.setter
    def vpc_endpoint_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


