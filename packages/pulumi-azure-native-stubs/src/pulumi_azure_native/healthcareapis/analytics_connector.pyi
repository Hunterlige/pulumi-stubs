

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalyticsConnectorArgs', 'AnalyticsConnector']
@pulumi.input_type
class AnalyticsConnectorArgs:
    def __init__(__self__, *, data_destination_configuration: pulumi.Input[AnalyticsConnectorDataLakeDataDestinationArgs], data_mapping_configuration: pulumi.Input[AnalyticsConnectorFhirToParquetMappingArgs], data_source_configuration: pulumi.Input[AnalyticsConnectorFhirServiceDataSourceArgs], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], analytics_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDestinationConfiguration")
    def data_destination_configuration(self) -> pulumi.Input[AnalyticsConnectorDataLakeDataDestinationArgs]:
        
        ...
    
    @data_destination_configuration.setter
    def data_destination_configuration(self, value: pulumi.Input[AnalyticsConnectorDataLakeDataDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataMappingConfiguration")
    def data_mapping_configuration(self) -> pulumi.Input[AnalyticsConnectorFhirToParquetMappingArgs]:
        
        ...
    
    @data_mapping_configuration.setter
    def data_mapping_configuration(self, value: pulumi.Input[AnalyticsConnectorFhirToParquetMappingArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> pulumi.Input[AnalyticsConnectorFhirServiceDataSourceArgs]:
        
        ...
    
    @data_source_configuration.setter
    def data_source_configuration(self, value: pulumi.Input[AnalyticsConnectorFhirServiceDataSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsConnectorName")
    def analytics_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analytics_connector_name.setter
    def analytics_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]): # -> None:
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
    


@pulumi.type_token("azure-native:healthcareapis:AnalyticsConnector")
class AnalyticsConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., analytics_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., data_destination_configuration: Optional[pulumi.Input[Union[AnalyticsConnectorDataLakeDataDestinationArgs, AnalyticsConnectorDataLakeDataDestinationArgsDict]]] = ..., data_mapping_configuration: Optional[pulumi.Input[Union[AnalyticsConnectorFhirToParquetMappingArgs, AnalyticsConnectorFhirToParquetMappingArgsDict]]] = ..., data_source_configuration: Optional[pulumi.Input[Union[AnalyticsConnectorFhirServiceDataSourceArgs, AnalyticsConnectorFhirServiceDataSourceArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[ServiceManagedIdentityIdentityArgs, ServiceManagedIdentityIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AnalyticsConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AnalyticsConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDestinationConfiguration")
    def data_destination_configuration(self) -> pulumi.Output[outputs.AnalyticsConnectorDataLakeDataDestinationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataMappingConfiguration")
    def data_mapping_configuration(self) -> pulumi.Output[outputs.AnalyticsConnectorFhirToParquetMappingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> pulumi.Output[outputs.AnalyticsConnectorFhirServiceDataSourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ServiceManagedIdentityResponseIdentity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


