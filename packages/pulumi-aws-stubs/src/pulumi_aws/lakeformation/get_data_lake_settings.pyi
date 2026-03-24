import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataLakeSettingsResult",
    "AwaitableGetDataLakeSettingsResult",
    "get_data_lake_settings",
    "get_data_lake_settings_output",
]

@pulumi.output_type
class GetDataLakeSettingsResult:
    def __init__(
        __self__,
        admins=...,
        allow_external_data_filtering=...,
        allow_full_table_external_data_access=...,
        authorized_session_tag_value_lists=...,
        catalog_id=...,
        create_database_default_permissions=...,
        create_table_default_permissions=...,
        external_data_filtering_allow_lists=...,
        id=...,
        parameters=...,
        read_only_admins=...,
        region=...,
        trusted_resource_owners=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def admins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowExternalDataFiltering")
    def allow_external_data_filtering(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowFullTableExternalDataAccess")
    def allow_full_table_external_data_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="authorizedSessionTagValueLists")
    def authorized_session_tag_value_lists(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(
        self,
    ) -> Sequence[outputs.GetDataLakeSettingsCreateDatabaseDefaultPermissionResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(
        self,
    ) -> Sequence[outputs.GetDataLakeSettingsCreateTableDefaultPermissionResult]: ...
    @_builtins.property
    @pulumi.getter(name="externalDataFilteringAllowLists")
    def external_data_filtering_allow_lists(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readOnlyAdmins")
    def read_only_admins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trustedResourceOwners")
    def trusted_resource_owners(self) -> Sequence[_builtins.str]: ...

class AwaitableGetDataLakeSettingsResult(GetDataLakeSettingsResult):
    def __await__(self): ...

def get_data_lake_settings(
    catalog_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataLakeSettingsResult: ...
def get_data_lake_settings_output(
    catalog_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataLakeSettingsResult]: ...
