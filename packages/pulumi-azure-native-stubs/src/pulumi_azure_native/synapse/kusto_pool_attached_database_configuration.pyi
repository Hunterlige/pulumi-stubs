

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KustoPoolAttachedDatabaseConfigurationArgs', 'KustoPoolAttachedDatabaseConfiguration']
@pulumi.input_type
class KustoPoolAttachedDatabaseConfigurationArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], default_principals_modification_kind: pulumi.Input[Union[_builtins.str, DefaultPrincipalsModificationKind]], kusto_pool_name: pulumi.Input[_builtins.str], kusto_pool_resource_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], attached_database_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., table_level_sharing_properties: Optional[pulumi.Input[TableLevelSharingPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPrincipalsModificationKind")
    def default_principals_modification_kind(self) -> pulumi.Input[Union[_builtins.str, DefaultPrincipalsModificationKind]]:
        
        ...
    
    @default_principals_modification_kind.setter
    def default_principals_modification_kind(self, value: pulumi.Input[Union[_builtins.str, DefaultPrincipalsModificationKind]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoPoolName")
    def kusto_pool_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_pool_name.setter
    def kusto_pool_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoPoolResourceId")
    def kusto_pool_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_pool_resource_id.setter
    def kusto_pool_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="attachedDatabaseConfigurationName")
    def attached_database_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attached_database_configuration_name.setter
    def attached_database_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableLevelSharingProperties")
    def table_level_sharing_properties(self) -> Optional[pulumi.Input[TableLevelSharingPropertiesArgs]]:
        
        ...
    
    @table_level_sharing_properties.setter
    def table_level_sharing_properties(self, value: Optional[pulumi.Input[TableLevelSharingPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class KustoPoolAttachedDatabaseConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attached_database_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., default_principals_modification_kind: Optional[pulumi.Input[Union[_builtins.str, DefaultPrincipalsModificationKind]]] = ..., kusto_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., kusto_pool_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_level_sharing_properties: Optional[pulumi.Input[Union[TableLevelSharingPropertiesArgs, TableLevelSharingPropertiesArgsDict]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: KustoPoolAttachedDatabaseConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> KustoPoolAttachedDatabaseConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedDatabaseNames")
    def attached_database_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPrincipalsModificationKind")
    def default_principals_modification_kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoPoolResourceId")
    def kusto_pool_resource_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="tableLevelSharingProperties")
    def table_level_sharing_properties(self) -> pulumi.Output[Optional[outputs.TableLevelSharingPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


