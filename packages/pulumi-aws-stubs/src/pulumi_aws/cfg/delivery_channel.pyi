

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeliveryChannelArgs', 'DeliveryChannel']
@pulumi.input_type
class DeliveryChannelArgs:
    def __init__(__self__, *, s3_bucket_name: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_delivery_properties: Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_arn.setter
    def s3_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDeliveryProperties")
    def snapshot_delivery_properties(self) -> Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]]:
        
        ...
    
    @snapshot_delivery_properties.setter
    def snapshot_delivery_properties(self, value: Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DeliveryChannelState:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_delivery_properties: Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_arn.setter
    def s3_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDeliveryProperties")
    def snapshot_delivery_properties(self) -> Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]]:
        
        ...
    
    @snapshot_delivery_properties.setter
    def snapshot_delivery_properties(self, value: Optional[pulumi.Input[DeliveryChannelSnapshotDeliveryPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cfg/deliveryChannel:DeliveryChannel")
class DeliveryChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_delivery_properties: Optional[pulumi.Input[Union[DeliveryChannelSnapshotDeliveryPropertiesArgs, DeliveryChannelSnapshotDeliveryPropertiesArgsDict]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeliveryChannelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_delivery_properties: Optional[pulumi.Input[Union[DeliveryChannelSnapshotDeliveryPropertiesArgs, DeliveryChannelSnapshotDeliveryPropertiesArgsDict]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> DeliveryChannel:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDeliveryProperties")
    def snapshot_delivery_properties(self) -> pulumi.Output[Optional[outputs.DeliveryChannelSnapshotDeliveryProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


