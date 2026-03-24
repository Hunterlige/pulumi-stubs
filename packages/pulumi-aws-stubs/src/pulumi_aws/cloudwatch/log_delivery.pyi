

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogDeliveryArgs', 'LogDelivery']
@pulumi.input_type
class LogDeliveryArgs:
    def __init__(__self__, *, delivery_destination_arn: pulumi.Input[_builtins.str], delivery_source_name: pulumi.Input[_builtins.str], field_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., record_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_delivery_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationArn")
    def delivery_destination_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @delivery_destination_arn.setter
    def delivery_destination_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverySourceName")
    def delivery_source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @delivery_source_name.setter
    def delivery_source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFields")
    def record_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @record_fields.setter
    def record_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DeliveryConfigurations")
    def s3_delivery_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]]:
        
        ...
    
    @s3_delivery_configurations.setter
    def s3_delivery_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _LogDeliveryState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., delivery_destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., delivery_source_name: Optional[pulumi.Input[_builtins.str]] = ..., field_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., record_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_delivery_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationArn")
    def delivery_destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_destination_arn.setter
    def delivery_destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverySourceName")
    def delivery_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_source_name.setter
    def delivery_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFields")
    def record_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @record_fields.setter
    def record_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DeliveryConfigurations")
    def s3_delivery_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]]:
        
        ...
    
    @s3_delivery_configurations.setter
    def s3_delivery_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LogDeliveryS3DeliveryConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/logDelivery:LogDelivery")
class LogDelivery(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delivery_destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., delivery_source_name: Optional[pulumi.Input[_builtins.str]] = ..., field_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., record_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_delivery_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LogDeliveryS3DeliveryConfigurationArgs, LogDeliveryS3DeliveryConfigurationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LogDeliveryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., delivery_destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., delivery_source_name: Optional[pulumi.Input[_builtins.str]] = ..., field_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., record_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_delivery_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LogDeliveryS3DeliveryConfigurationArgs, LogDeliveryS3DeliveryConfigurationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> LogDelivery:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryDestinationArn")
    def delivery_destination_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliverySourceName")
    def delivery_source_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFields")
    def record_fields(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DeliveryConfigurations")
    def s3_delivery_configurations(self) -> pulumi.Output[Sequence[outputs.LogDeliveryS3DeliveryConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


