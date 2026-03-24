

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataStoreArgs', 'DataStore']
@pulumi.input_type
class DataStoreArgs:
    def __init__(__self__, *, data_store_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], industry_vertical: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], advanced_site_search_config: Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]] = ..., content_config: Optional[pulumi.Input[_builtins.str]] = ..., create_advanced_site_search: Optional[pulumi.Input[_builtins.bool]] = ..., document_processing_config: Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_default_schema_creation: Optional[pulumi.Input[_builtins.bool]] = ..., solution_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_store_id.setter
    def data_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSiteSearchConfig")
    def advanced_site_search_config(self) -> Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]]:
        
        ...
    
    @advanced_site_search_config.setter
    def advanced_site_search_config(self, value: Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_config.setter
    def content_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAdvancedSiteSearch")
    def create_advanced_site_search(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_advanced_site_search.setter
    def create_advanced_site_search(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingConfig")
    def document_processing_config(self) -> Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]]:
        
        ...
    
    @document_processing_config.setter
    def document_processing_config(self, value: Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDefaultSchemaCreation")
    def skip_default_schema_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_default_schema_creation.setter
    def skip_default_schema_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionTypes")
    def solution_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @solution_types.setter
    def solution_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DataStoreState:
    def __init__(__self__, *, advanced_site_search_config: Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]] = ..., content_config: Optional[pulumi.Input[_builtins.str]] = ..., create_advanced_site_search: Optional[pulumi.Input[_builtins.bool]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_id: Optional[pulumi.Input[_builtins.str]] = ..., default_schema_id: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_config: Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_default_schema_creation: Optional[pulumi.Input[_builtins.bool]] = ..., solution_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSiteSearchConfig")
    def advanced_site_search_config(self) -> Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]]:
        
        ...
    
    @advanced_site_search_config.setter
    def advanced_site_search_config(self, value: Optional[pulumi.Input[DataStoreAdvancedSiteSearchConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_config.setter
    def content_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAdvancedSiteSearch")
    def create_advanced_site_search(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_advanced_site_search.setter
    def create_advanced_site_search(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store_id.setter
    def data_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSchemaId")
    def default_schema_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_schema_id.setter
    def default_schema_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingConfig")
    def document_processing_config(self) -> Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]]:
        
        ...
    
    @document_processing_config.setter
    def document_processing_config(self, value: Optional[pulumi.Input[DataStoreDocumentProcessingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDefaultSchemaCreation")
    def skip_default_schema_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_default_schema_creation.setter
    def skip_default_schema_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionTypes")
    def solution_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @solution_types.setter
    def solution_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/dataStore:DataStore")
class DataStore(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., advanced_site_search_config: Optional[pulumi.Input[Union[DataStoreAdvancedSiteSearchConfigArgs, DataStoreAdvancedSiteSearchConfigArgsDict]]] = ..., content_config: Optional[pulumi.Input[_builtins.str]] = ..., create_advanced_site_search: Optional[pulumi.Input[_builtins.bool]] = ..., data_store_id: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_config: Optional[pulumi.Input[Union[DataStoreDocumentProcessingConfigArgs, DataStoreDocumentProcessingConfigArgsDict]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_default_schema_creation: Optional[pulumi.Input[_builtins.bool]] = ..., solution_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataStoreArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., advanced_site_search_config: Optional[pulumi.Input[Union[DataStoreAdvancedSiteSearchConfigArgs, DataStoreAdvancedSiteSearchConfigArgsDict]]] = ..., content_config: Optional[pulumi.Input[_builtins.str]] = ..., create_advanced_site_search: Optional[pulumi.Input[_builtins.bool]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_id: Optional[pulumi.Input[_builtins.str]] = ..., default_schema_id: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_config: Optional[pulumi.Input[Union[DataStoreDocumentProcessingConfigArgs, DataStoreDocumentProcessingConfigArgsDict]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_default_schema_creation: Optional[pulumi.Input[_builtins.bool]] = ..., solution_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> DataStore:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSiteSearchConfig")
    def advanced_site_search_config(self) -> pulumi.Output[outputs.DataStoreAdvancedSiteSearchConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAdvancedSiteSearch")
    def create_advanced_site_search(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreId")
    def data_store_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSchemaId")
    def default_schema_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingConfig")
    def document_processing_config(self) -> pulumi.Output[Optional[outputs.DataStoreDocumentProcessingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDefaultSchemaCreation")
    def skip_default_schema_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionTypes")
    def solution_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


