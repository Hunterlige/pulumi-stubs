import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PermissionsArgs", "Permissions"]

@pulumi.input_type
class PermissionsArgs:
    def __init__(
        __self__,
        *,
        permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_cells_filter: Optional[pulumi.Input[PermissionsDataCellsFilterArgs]] = ...,
        data_location: Optional[pulumi.Input[PermissionsDataLocationArgs]] = ...,
        database: Optional[pulumi.Input[PermissionsDatabaseArgs]] = ...,
        lf_tag: Optional[pulumi.Input[PermissionsLfTagArgs]] = ...,
        lf_tag_policy: Optional[pulumi.Input[PermissionsLfTagPolicyArgs]] = ...,
        permissions_with_grant_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[PermissionsTableArgs]] = ...,
        table_with_columns: Optional[
            pulumi.Input[PermissionsTableWithColumnsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @permissions.setter
    def permissions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogResource")
    def catalog_resource(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @catalog_resource.setter
    def catalog_resource(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCellsFilter")
    def data_cells_filter(
        self,
    ) -> Optional[pulumi.Input[PermissionsDataCellsFilterArgs]]: ...
    @data_cells_filter.setter
    def data_cells_filter(
        self, value: Optional[pulumi.Input[PermissionsDataCellsFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> Optional[pulumi.Input[PermissionsDataLocationArgs]]: ...
    @data_location.setter
    def data_location(
        self, value: Optional[pulumi.Input[PermissionsDataLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[PermissionsDatabaseArgs]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[PermissionsDatabaseArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> Optional[pulumi.Input[PermissionsLfTagArgs]]: ...
    @lf_tag.setter
    def lf_tag(self, value: Optional[pulumi.Input[PermissionsLfTagArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTagPolicy")
    def lf_tag_policy(self) -> Optional[pulumi.Input[PermissionsLfTagPolicyArgs]]: ...
    @lf_tag_policy.setter
    def lf_tag_policy(
        self, value: Optional[pulumi.Input[PermissionsLfTagPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permissionsWithGrantOptions")
    def permissions_with_grant_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions_with_grant_options.setter
    def permissions_with_grant_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[PermissionsTableArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[PermissionsTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> Optional[pulumi.Input[PermissionsTableWithColumnsArgs]]: ...
    @table_with_columns.setter
    def table_with_columns(
        self, value: Optional[pulumi.Input[PermissionsTableWithColumnsArgs]]
    ): ...

@pulumi.input_type
class _PermissionsState:
    def __init__(
        __self__,
        *,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_cells_filter: Optional[pulumi.Input[PermissionsDataCellsFilterArgs]] = ...,
        data_location: Optional[pulumi.Input[PermissionsDataLocationArgs]] = ...,
        database: Optional[pulumi.Input[PermissionsDatabaseArgs]] = ...,
        lf_tag: Optional[pulumi.Input[PermissionsLfTagArgs]] = ...,
        lf_tag_policy: Optional[pulumi.Input[PermissionsLfTagPolicyArgs]] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permissions_with_grant_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[PermissionsTableArgs]] = ...,
        table_with_columns: Optional[
            pulumi.Input[PermissionsTableWithColumnsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogResource")
    def catalog_resource(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @catalog_resource.setter
    def catalog_resource(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCellsFilter")
    def data_cells_filter(
        self,
    ) -> Optional[pulumi.Input[PermissionsDataCellsFilterArgs]]: ...
    @data_cells_filter.setter
    def data_cells_filter(
        self, value: Optional[pulumi.Input[PermissionsDataCellsFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> Optional[pulumi.Input[PermissionsDataLocationArgs]]: ...
    @data_location.setter
    def data_location(
        self, value: Optional[pulumi.Input[PermissionsDataLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[PermissionsDatabaseArgs]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[PermissionsDatabaseArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> Optional[pulumi.Input[PermissionsLfTagArgs]]: ...
    @lf_tag.setter
    def lf_tag(self, value: Optional[pulumi.Input[PermissionsLfTagArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTagPolicy")
    def lf_tag_policy(self) -> Optional[pulumi.Input[PermissionsLfTagPolicyArgs]]: ...
    @lf_tag_policy.setter
    def lf_tag_policy(
        self, value: Optional[pulumi.Input[PermissionsLfTagPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permissionsWithGrantOptions")
    def permissions_with_grant_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions_with_grant_options.setter
    def permissions_with_grant_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[PermissionsTableArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[PermissionsTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> Optional[pulumi.Input[PermissionsTableWithColumnsArgs]]: ...
    @table_with_columns.setter
    def table_with_columns(
        self, value: Optional[pulumi.Input[PermissionsTableWithColumnsArgs]]
    ): ...

@pulumi.type_token("aws:lakeformation/permissions:Permissions")
class Permissions(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_cells_filter: Optional[
            pulumi.Input[
                Union[
                    PermissionsDataCellsFilterArgs, PermissionsDataCellsFilterArgsDict
                ]
            ]
        ] = ...,
        data_location: Optional[
            pulumi.Input[
                Union[PermissionsDataLocationArgs, PermissionsDataLocationArgsDict]
            ]
        ] = ...,
        database: Optional[
            pulumi.Input[Union[PermissionsDatabaseArgs, PermissionsDatabaseArgsDict]]
        ] = ...,
        lf_tag: Optional[
            pulumi.Input[Union[PermissionsLfTagArgs, PermissionsLfTagArgsDict]]
        ] = ...,
        lf_tag_policy: Optional[
            pulumi.Input[
                Union[PermissionsLfTagPolicyArgs, PermissionsLfTagPolicyArgsDict]
            ]
        ] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permissions_with_grant_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[
            pulumi.Input[Union[PermissionsTableArgs, PermissionsTableArgsDict]]
        ] = ...,
        table_with_columns: Optional[
            pulumi.Input[
                Union[
                    PermissionsTableWithColumnsArgs, PermissionsTableWithColumnsArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PermissionsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_cells_filter: Optional[
            pulumi.Input[
                Union[
                    PermissionsDataCellsFilterArgs, PermissionsDataCellsFilterArgsDict
                ]
            ]
        ] = ...,
        data_location: Optional[
            pulumi.Input[
                Union[PermissionsDataLocationArgs, PermissionsDataLocationArgsDict]
            ]
        ] = ...,
        database: Optional[
            pulumi.Input[Union[PermissionsDatabaseArgs, PermissionsDatabaseArgsDict]]
        ] = ...,
        lf_tag: Optional[
            pulumi.Input[Union[PermissionsLfTagArgs, PermissionsLfTagArgsDict]]
        ] = ...,
        lf_tag_policy: Optional[
            pulumi.Input[
                Union[PermissionsLfTagPolicyArgs, PermissionsLfTagPolicyArgsDict]
            ]
        ] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permissions_with_grant_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[
            pulumi.Input[Union[PermissionsTableArgs, PermissionsTableArgsDict]]
        ] = ...,
        table_with_columns: Optional[
            pulumi.Input[
                Union[
                    PermissionsTableWithColumnsArgs, PermissionsTableWithColumnsArgsDict
                ]
            ]
        ] = ...,
    ) -> Permissions: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="catalogResource")
    def catalog_resource(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="dataCellsFilter")
    def data_cells_filter(
        self,
    ) -> pulumi.Output[Optional[outputs.PermissionsDataCellsFilter]]: ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[outputs.PermissionsDataLocation]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[outputs.PermissionsDatabase]: ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> pulumi.Output[outputs.PermissionsLfTag]: ...
    @_builtins.property
    @pulumi.getter(name="lfTagPolicy")
    def lf_tag_policy(self) -> pulumi.Output[outputs.PermissionsLfTagPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permissionsWithGrantOptions")
    def permissions_with_grant_options(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Output[outputs.PermissionsTable]: ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> pulumi.Output[outputs.PermissionsTableWithColumns]: ...
