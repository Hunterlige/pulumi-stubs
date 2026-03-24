

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
__all__ = ['AgentDataSourceArgs', 'AgentDataSource']
@pulumi.input_type
class AgentDataSourceArgs:
    def __init__(__self__, *, data_source_configuration: pulumi.Input[AgentDataSourceDataSourceConfigurationArgs], knowledge_base_id: pulumi.Input[_builtins.str], data_deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]] = ..., timeouts: Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]] = ..., vector_ingestion_configuration: Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> pulumi.Input[AgentDataSourceDataSourceConfigurationArgs]:
        
        ...
    
    @data_source_configuration.setter
    def data_source_configuration(self, value: pulumi.Input[AgentDataSourceDataSourceConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @knowledge_base_id.setter
    def knowledge_base_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDeletionPolicy")
    def data_deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_deletion_policy.setter
    def data_deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIngestionConfiguration")
    def vector_ingestion_configuration(self) -> Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]]:
        
        ...
    
    @vector_ingestion_configuration.setter
    def vector_ingestion_configuration(self, value: Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentDataSourceState:
    def __init__(__self__, *, data_deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., data_source_configuration: Optional[pulumi.Input[AgentDataSourceDataSourceConfigurationArgs]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]] = ..., timeouts: Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]] = ..., vector_ingestion_configuration: Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDeletionPolicy")
    def data_deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_deletion_policy.setter
    def data_deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> Optional[pulumi.Input[AgentDataSourceDataSourceConfigurationArgs]]:
        
        ...
    
    @data_source_configuration.setter
    def data_source_configuration(self, value: Optional[pulumi.Input[AgentDataSourceDataSourceConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @knowledge_base_id.setter
    def knowledge_base_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[AgentDataSourceServerSideEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentDataSourceTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIngestionConfiguration")
    def vector_ingestion_configuration(self) -> Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]]:
        
        ...
    
    @vector_ingestion_configuration.setter
    def vector_ingestion_configuration(self, value: Optional[pulumi.Input[AgentDataSourceVectorIngestionConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:bedrock/agentDataSource:AgentDataSource")
class AgentDataSource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., data_source_configuration: Optional[pulumi.Input[Union[AgentDataSourceDataSourceConfigurationArgs, AgentDataSourceDataSourceConfigurationArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[AgentDataSourceServerSideEncryptionConfigurationArgs, AgentDataSourceServerSideEncryptionConfigurationArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentDataSourceTimeoutsArgs, AgentDataSourceTimeoutsArgsDict]]] = ..., vector_ingestion_configuration: Optional[pulumi.Input[Union[AgentDataSourceVectorIngestionConfigurationArgs, AgentDataSourceVectorIngestionConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentDataSourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., data_deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., data_source_configuration: Optional[pulumi.Input[Union[AgentDataSourceDataSourceConfigurationArgs, AgentDataSourceDataSourceConfigurationArgsDict]]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[AgentDataSourceServerSideEncryptionConfigurationArgs, AgentDataSourceServerSideEncryptionConfigurationArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentDataSourceTimeoutsArgs, AgentDataSourceTimeoutsArgsDict]]] = ..., vector_ingestion_configuration: Optional[pulumi.Input[Union[AgentDataSourceVectorIngestionConfigurationArgs, AgentDataSourceVectorIngestionConfigurationArgsDict]]] = ...) -> AgentDataSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDeletionPolicy")
    def data_deletion_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> pulumi.Output[outputs.AgentDataSourceDataSourceConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(self) -> pulumi.Output[Optional[outputs.AgentDataSourceServerSideEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentDataSourceTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIngestionConfiguration")
    def vector_ingestion_configuration(self) -> pulumi.Output[Optional[outputs.AgentDataSourceVectorIngestionConfiguration]]:
        
        ...
    


