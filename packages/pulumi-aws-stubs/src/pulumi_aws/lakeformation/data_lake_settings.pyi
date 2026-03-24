

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
__all__ = ['DataLakeSettingsArgs', 'DataLakeSettings']
@pulumi.input_type
class DataLakeSettingsArgs:
    def __init__(__self__, *, admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_external_data_filtering: Optional[pulumi.Input[_builtins.bool]] = ..., allow_full_table_external_data_access: Optional[pulumi.Input[_builtins.bool]] = ..., authorized_session_tag_value_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., create_database_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]] = ..., create_table_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]] = ..., external_data_filtering_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., read_only_admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trusted_resource_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admins.setter
    def admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExternalDataFiltering")
    def allow_external_data_filtering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_external_data_filtering.setter
    def allow_external_data_filtering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowFullTableExternalDataAccess")
    def allow_full_table_external_data_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_full_table_external_data_access.setter
    def allow_full_table_external_data_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedSessionTagValueLists")
    def authorized_session_tag_value_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorized_session_tag_value_lists.setter
    def authorized_session_tag_value_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]]:
        
        ...
    
    @create_database_default_permissions.setter
    def create_database_default_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]]:
        
        ...
    
    @create_table_default_permissions.setter
    def create_table_default_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataFilteringAllowLists")
    def external_data_filtering_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_data_filtering_allow_lists.setter
    def external_data_filtering_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyAdmins")
    def read_only_admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @read_only_admins.setter
    def read_only_admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedResourceOwners")
    def trusted_resource_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_resource_owners.setter
    def trusted_resource_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DataLakeSettingsState:
    def __init__(__self__, *, admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_external_data_filtering: Optional[pulumi.Input[_builtins.bool]] = ..., allow_full_table_external_data_access: Optional[pulumi.Input[_builtins.bool]] = ..., authorized_session_tag_value_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., create_database_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]] = ..., create_table_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]] = ..., external_data_filtering_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., read_only_admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trusted_resource_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admins.setter
    def admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExternalDataFiltering")
    def allow_external_data_filtering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_external_data_filtering.setter
    def allow_external_data_filtering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowFullTableExternalDataAccess")
    def allow_full_table_external_data_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_full_table_external_data_access.setter
    def allow_full_table_external_data_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedSessionTagValueLists")
    def authorized_session_tag_value_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorized_session_tag_value_lists.setter
    def authorized_session_tag_value_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]]:
        
        ...
    
    @create_database_default_permissions.setter
    def create_database_default_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateDatabaseDefaultPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]]:
        
        ...
    
    @create_table_default_permissions.setter
    def create_table_default_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeSettingsCreateTableDefaultPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataFilteringAllowLists")
    def external_data_filtering_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_data_filtering_allow_lists.setter
    def external_data_filtering_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyAdmins")
    def read_only_admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @read_only_admins.setter
    def read_only_admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedResourceOwners")
    def trusted_resource_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_resource_owners.setter
    def trusted_resource_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DataLakeSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_external_data_filtering: Optional[pulumi.Input[_builtins.bool]] = ..., allow_full_table_external_data_access: Optional[pulumi.Input[_builtins.bool]] = ..., authorized_session_tag_value_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., create_database_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataLakeSettingsCreateDatabaseDefaultPermissionArgs, DataLakeSettingsCreateDatabaseDefaultPermissionArgsDict]]]]] = ..., create_table_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataLakeSettingsCreateTableDefaultPermissionArgs, DataLakeSettingsCreateTableDefaultPermissionArgsDict]]]]] = ..., external_data_filtering_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., read_only_admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trusted_resource_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DataLakeSettingsArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_external_data_filtering: Optional[pulumi.Input[_builtins.bool]] = ..., allow_full_table_external_data_access: Optional[pulumi.Input[_builtins.bool]] = ..., authorized_session_tag_value_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., create_database_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataLakeSettingsCreateDatabaseDefaultPermissionArgs, DataLakeSettingsCreateDatabaseDefaultPermissionArgsDict]]]]] = ..., create_table_default_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataLakeSettingsCreateTableDefaultPermissionArgs, DataLakeSettingsCreateTableDefaultPermissionArgsDict]]]]] = ..., external_data_filtering_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., read_only_admins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trusted_resource_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> DataLakeSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admins(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExternalDataFiltering")
    def allow_external_data_filtering(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowFullTableExternalDataAccess")
    def allow_full_table_external_data_access(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedSessionTagValueLists")
    def authorized_session_tag_value_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(self) -> pulumi.Output[Sequence[outputs.DataLakeSettingsCreateDatabaseDefaultPermission]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(self) -> pulumi.Output[Sequence[outputs.DataLakeSettingsCreateTableDefaultPermission]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataFilteringAllowLists")
    def external_data_filtering_allow_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyAdmins")
    def read_only_admins(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedResourceOwners")
    def trusted_resource_owners(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


