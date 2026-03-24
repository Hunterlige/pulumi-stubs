

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
__all__ = ['IndexArgs', 'Index']
@pulumi.input_type
class IndexArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], capacity_units: Optional[pulumi.Input[IndexCapacityUnitsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., document_metadata_configuration_updates: Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_context_policy: Optional[pulumi.Input[_builtins.str]] = ..., user_group_resolution_configuration: Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]] = ..., user_token_configurations: Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> Optional[pulumi.Input[IndexCapacityUnitsArgs]]:
        
        ...
    
    @capacity_units.setter
    def capacity_units(self, value: Optional[pulumi.Input[IndexCapacityUnitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]]:
        
        ...
    
    @document_metadata_configuration_updates.setter
    def document_metadata_configuration_updates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userContextPolicy")
    def user_context_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_context_policy.setter
    def user_context_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionConfiguration")
    def user_group_resolution_configuration(self) -> Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]]:
        
        ...
    
    @user_group_resolution_configuration.setter
    def user_group_resolution_configuration(self, value: Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenConfigurations")
    def user_token_configurations(self) -> Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]]:
        
        ...
    
    @user_token_configurations.setter
    def user_token_configurations(self, value: Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _IndexState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_units: Optional[pulumi.Input[IndexCapacityUnitsArgs]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., document_metadata_configuration_updates: Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ..., index_statistics: Optional[pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ..., user_context_policy: Optional[pulumi.Input[_builtins.str]] = ..., user_group_resolution_configuration: Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]] = ..., user_token_configurations: Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> Optional[pulumi.Input[IndexCapacityUnitsArgs]]:
        
        ...
    
    @capacity_units.setter
    def capacity_units(self, value: Optional[pulumi.Input[IndexCapacityUnitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]]:
        
        ...
    
    @document_metadata_configuration_updates.setter
    def document_metadata_configuration_updates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexDocumentMetadataConfigurationUpdateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexStatistics")
    def index_statistics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticArgs]]]]:
        
        ...
    
    @index_statistics.setter
    def index_statistics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexIndexStatisticArgs]]]]): # -> None:
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
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[IndexServerSideEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userContextPolicy")
    def user_context_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_context_policy.setter
    def user_context_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionConfiguration")
    def user_group_resolution_configuration(self) -> Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]]:
        
        ...
    
    @user_group_resolution_configuration.setter
    def user_group_resolution_configuration(self, value: Optional[pulumi.Input[IndexUserGroupResolutionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenConfigurations")
    def user_token_configurations(self) -> Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]]:
        
        ...
    
    @user_token_configurations.setter
    def user_token_configurations(self, value: Optional[pulumi.Input[IndexUserTokenConfigurationsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:kendra/index:Index")
class Index(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity_units: Optional[pulumi.Input[Union[IndexCapacityUnitsArgs, IndexCapacityUnitsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., document_metadata_configuration_updates: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IndexDocumentMetadataConfigurationUpdateArgs, IndexDocumentMetadataConfigurationUpdateArgsDict]]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[IndexServerSideEncryptionConfigurationArgs, IndexServerSideEncryptionConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_context_policy: Optional[pulumi.Input[_builtins.str]] = ..., user_group_resolution_configuration: Optional[pulumi.Input[Union[IndexUserGroupResolutionConfigurationArgs, IndexUserGroupResolutionConfigurationArgsDict]]] = ..., user_token_configurations: Optional[pulumi.Input[Union[IndexUserTokenConfigurationsArgs, IndexUserTokenConfigurationsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IndexArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_units: Optional[pulumi.Input[Union[IndexCapacityUnitsArgs, IndexCapacityUnitsArgsDict]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., document_metadata_configuration_updates: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IndexDocumentMetadataConfigurationUpdateArgs, IndexDocumentMetadataConfigurationUpdateArgsDict]]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ..., index_statistics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IndexIndexStatisticArgs, IndexIndexStatisticArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[IndexServerSideEncryptionConfigurationArgs, IndexServerSideEncryptionConfigurationArgsDict]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ..., user_context_policy: Optional[pulumi.Input[_builtins.str]] = ..., user_group_resolution_configuration: Optional[pulumi.Input[Union[IndexUserGroupResolutionConfigurationArgs, IndexUserGroupResolutionConfigurationArgsDict]]] = ..., user_token_configurations: Optional[pulumi.Input[Union[IndexUserTokenConfigurationsArgs, IndexUserTokenConfigurationsArgsDict]]] = ...) -> Index:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> pulumi.Output[outputs.IndexCapacityUnits]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(self) -> pulumi.Output[Sequence[outputs.IndexDocumentMetadataConfigurationUpdate]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexStatistics")
    def index_statistics(self) -> pulumi.Output[Sequence[outputs.IndexIndexStatistic]]:
        
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
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(self) -> pulumi.Output[Optional[outputs.IndexServerSideEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userContextPolicy")
    def user_context_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionConfiguration")
    def user_group_resolution_configuration(self) -> pulumi.Output[Optional[outputs.IndexUserGroupResolutionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenConfigurations")
    def user_token_configurations(self) -> pulumi.Output[Optional[outputs.IndexUserTokenConfigurations]]:
        
        ...
    


