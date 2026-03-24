

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['Gen2EnvironmentArgs', 'Gen2Environment']
@pulumi.input_type
class Gen2EnvironmentArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], sku: pulumi.Input[SkuArgs], storage_configuration: pulumi.Input[Gen2StorageConfigurationInputArgs], time_series_id_properties: pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]], environment_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., warm_store_configuration: Optional[pulumi.Input[WarmStoreConfigurationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> pulumi.Input[Gen2StorageConfigurationInputArgs]:
        
        ...
    
    @storage_configuration.setter
    def storage_configuration(self, value: pulumi.Input[Gen2StorageConfigurationInputArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesIdProperties")
    def time_series_id_properties(self) -> pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]]:
        
        ...
    
    @time_series_id_properties.setter
    def time_series_id_properties(self, value: pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmStoreConfiguration")
    def warm_store_configuration(self) -> Optional[pulumi.Input[WarmStoreConfigurationPropertiesArgs]]:
        
        ...
    
    @warm_store_configuration.setter
    def warm_store_configuration(self, value: Optional[pulumi.Input[WarmStoreConfigurationPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:timeseriesinsights:Gen2Environment")
class Gen2Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., storage_configuration: Optional[pulumi.Input[Union[Gen2StorageConfigurationInputArgs, Gen2StorageConfigurationInputArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_series_id_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TimeSeriesIdPropertyArgs, TimeSeriesIdPropertyArgsDict]]]]] = ..., warm_store_configuration: Optional[pulumi.Input[Union[WarmStoreConfigurationPropertiesArgs, WarmStoreConfigurationPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Gen2EnvironmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Gen2Environment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.EnvironmentStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> pulumi.Output[outputs.Gen2StorageConfigurationOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesIdProperties")
    def time_series_id_properties(self) -> pulumi.Output[Sequence[outputs.TimeSeriesIdPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmStoreConfiguration")
    def warm_store_configuration(self) -> pulumi.Output[Optional[outputs.WarmStoreConfigurationPropertiesResponse]]:
        
        ...
    


