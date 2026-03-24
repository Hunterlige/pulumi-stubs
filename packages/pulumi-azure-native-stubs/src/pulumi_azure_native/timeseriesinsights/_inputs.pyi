

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['Gen2StorageConfigurationInputArgs', 'Gen2StorageConfigurationInputArgsDict', 'LocalTimestampTimeZoneOffsetArgs', 'LocalTimestampTimeZoneOffsetArgsDict', 'LocalTimestampArgs', 'LocalTimestampArgsDict', 'ReferenceDataSetKeyPropertyArgs', 'ReferenceDataSetKeyPropertyArgsDict', 'SkuArgs', 'SkuArgsDict', 'TimeSeriesIdPropertyArgs', 'TimeSeriesIdPropertyArgsDict', 'WarmStoreConfigurationPropertiesArgs', 'WarmStoreConfigurationPropertiesArgsDict']
class Gen2StorageConfigurationInputArgsDict(TypedDict):
    
    account_name: pulumi.Input[_builtins.str]
    management_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class Gen2StorageConfigurationInputArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], management_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementKey")
    def management_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @management_key.setter
    def management_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LocalTimestampTimeZoneOffsetArgsDict(TypedDict):
    
    property_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocalTimestampTimeZoneOffsetArgs:
    def __init__(__self__, *, property_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocalTimestampArgsDict(TypedDict):
    
    format: NotRequired[pulumi.Input[Union[_builtins.str, LocalTimestampFormat]]]
    time_zone_offset: NotRequired[pulumi.Input[LocalTimestampTimeZoneOffsetArgsDict]]


@pulumi.input_type
class LocalTimestampArgs:
    def __init__(__self__, *, format: Optional[pulumi.Input[Union[_builtins.str, LocalTimestampFormat]]] = ..., time_zone_offset: Optional[pulumi.Input[LocalTimestampTimeZoneOffsetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[_builtins.str, LocalTimestampFormat]]]:
        
        ...
    
    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[_builtins.str, LocalTimestampFormat]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZoneOffset")
    def time_zone_offset(self) -> Optional[pulumi.Input[LocalTimestampTimeZoneOffsetArgs]]:
        
        ...
    
    @time_zone_offset.setter
    def time_zone_offset(self, value: Optional[pulumi.Input[LocalTimestampTimeZoneOffsetArgs]]): # -> None:
        ...
    


class ReferenceDataSetKeyPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ReferenceDataKeyPropertyType]]]


@pulumi.input_type
class ReferenceDataSetKeyPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ReferenceDataKeyPropertyType]]] = ...) -> None:
        
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
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ReferenceDataKeyPropertyType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ReferenceDataKeyPropertyType]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    capacity: pulumi.Input[_builtins.int]
    name: pulumi.Input[Union[_builtins.str, SkuName]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, capacity: pulumi.Input[_builtins.int], name: pulumi.Input[Union[_builtins.str, SkuName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): # -> None:
        ...
    


class TimeSeriesIdPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, PropertyType]]]


@pulumi.input_type
class TimeSeriesIdPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, PropertyType]]] = ...) -> None:
        
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
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, PropertyType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, PropertyType]]]): # -> None:
        ...
    


class WarmStoreConfigurationPropertiesArgsDict(TypedDict):
    
    data_retention: pulumi.Input[_builtins.str]


@pulumi.input_type
class WarmStoreConfigurationPropertiesArgs:
    def __init__(__self__, *, data_retention: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_retention.setter
    def data_retention(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


