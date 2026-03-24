

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
__all__ = ['DataLakeConnectorArgs', 'DataLakeConnector']
@pulumi.input_type
class DataLakeConnectorArgs:
    def __init__(__self__, *, database_format: pulumi.Input[Union[_builtins.str, DataLakeDatabaseFormat]], extended_location: pulumi.Input[ExtendedLocationPropertyArgs], image: pulumi.Input[ContainerImageArgs], mq_name: pulumi.Input[_builtins.str], protocol: pulumi.Input[Union[_builtins.str, MqttProtocol]], resource_group_name: pulumi.Input[_builtins.str], target: pulumi.Input[DataLakeTargetStorageArgs], data_lake_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., instances: Optional[pulumi.Input[_builtins.int]] = ..., local_broker_connection: Optional[pulumi.Input[LocalBrokerConnectionSpecArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ..., node_tolerations: Optional[pulumi.Input[NodeTolerationsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFormat")
    def database_format(self) -> pulumi.Input[Union[_builtins.str, DataLakeDatabaseFormat]]:
        
        ...
    
    @database_format.setter
    def database_format(self, value: pulumi.Input[Union[_builtins.str, DataLakeDatabaseFormat]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationPropertyArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationPropertyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[ContainerImageArgs]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[ContainerImageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mq_name.setter
    def mq_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, MqttProtocol]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, MqttProtocol]]): # -> None:
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
    def target(self) -> pulumi.Input[DataLakeTargetStorageArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[DataLakeTargetStorageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLakeConnectorName")
    def data_lake_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_lake_connector_name.setter
    def data_lake_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instances.setter
    def instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(self) -> Optional[pulumi.Input[LocalBrokerConnectionSpecArgs]]:
        
        ...
    
    @local_broker_connection.setter
    def local_broker_connection(self, value: Optional[pulumi.Input[LocalBrokerConnectionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(self) -> Optional[pulumi.Input[NodeTolerationsArgs]]:
        
        ...
    
    @node_tolerations.setter
    def node_tolerations(self, value: Optional[pulumi.Input[NodeTolerationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotoperationsmq:DataLakeConnector")
class DataLakeConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_lake_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., database_format: Optional[pulumi.Input[Union[_builtins.str, DataLakeDatabaseFormat]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationPropertyArgs, ExtendedLocationPropertyArgsDict]]] = ..., image: Optional[pulumi.Input[Union[ContainerImageArgs, ContainerImageArgsDict]]] = ..., instances: Optional[pulumi.Input[_builtins.int]] = ..., local_broker_connection: Optional[pulumi.Input[Union[LocalBrokerConnectionSpecArgs, LocalBrokerConnectionSpecArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ..., mq_name: Optional[pulumi.Input[_builtins.str]] = ..., node_tolerations: Optional[pulumi.Input[Union[NodeTolerationsArgs, NodeTolerationsArgsDict]]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, MqttProtocol]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target: Optional[pulumi.Input[Union[DataLakeTargetStorageArgs, DataLakeTargetStorageArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataLakeConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DataLakeConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFormat")
    def database_format(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Output[outputs.ContainerImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(self) -> pulumi.Output[Optional[outputs.LocalBrokerConnectionSpecResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(self) -> pulumi.Output[Optional[outputs.NodeTolerationsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]:
        
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
    def target(self) -> pulumi.Output[outputs.DataLakeTargetStorageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


