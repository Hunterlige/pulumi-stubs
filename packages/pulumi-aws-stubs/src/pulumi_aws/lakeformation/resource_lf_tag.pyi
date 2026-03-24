import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResourceLfTagArgs", "ResourceLfTag"]

@pulumi.input_type
class ResourceLfTagArgs:
    def __init__(
        __self__,
        *,
        lf_tag: pulumi.Input[ResourceLfTagLfTagArgs],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[ResourceLfTagDatabaseArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[ResourceLfTagTableArgs]] = ...,
        table_with_columns: Optional[
            pulumi.Input[ResourceLfTagTableWithColumnsArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> pulumi.Input[ResourceLfTagLfTagArgs]: ...
    @lf_tag.setter
    def lf_tag(self, value: pulumi.Input[ResourceLfTagLfTagArgs]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[ResourceLfTagDatabaseArgs]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[ResourceLfTagDatabaseArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[ResourceLfTagTableArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[ResourceLfTagTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> Optional[pulumi.Input[ResourceLfTagTableWithColumnsArgs]]: ...
    @table_with_columns.setter
    def table_with_columns(
        self, value: Optional[pulumi.Input[ResourceLfTagTableWithColumnsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]]): ...

@pulumi.input_type
class _ResourceLfTagState:
    def __init__(
        __self__,
        *,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[ResourceLfTagDatabaseArgs]] = ...,
        lf_tag: Optional[pulumi.Input[ResourceLfTagLfTagArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[ResourceLfTagTableArgs]] = ...,
        table_with_columns: Optional[
            pulumi.Input[ResourceLfTagTableWithColumnsArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[ResourceLfTagDatabaseArgs]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[ResourceLfTagDatabaseArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> Optional[pulumi.Input[ResourceLfTagLfTagArgs]]: ...
    @lf_tag.setter
    def lf_tag(self, value: Optional[pulumi.Input[ResourceLfTagLfTagArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[ResourceLfTagTableArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[ResourceLfTagTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> Optional[pulumi.Input[ResourceLfTagTableWithColumnsArgs]]: ...
    @table_with_columns.setter
    def table_with_columns(
        self, value: Optional[pulumi.Input[ResourceLfTagTableWithColumnsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ResourceLfTagTimeoutsArgs]]): ...

@pulumi.type_token("aws:lakeformation/resourceLfTag:ResourceLfTag")
class ResourceLfTag(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[
            pulumi.Input[
                Union[ResourceLfTagDatabaseArgs, ResourceLfTagDatabaseArgsDict]
            ]
        ] = ...,
        lf_tag: Optional[
            pulumi.Input[Union[ResourceLfTagLfTagArgs, ResourceLfTagLfTagArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[
            pulumi.Input[Union[ResourceLfTagTableArgs, ResourceLfTagTableArgsDict]]
        ] = ...,
        table_with_columns: Optional[
            pulumi.Input[
                Union[
                    ResourceLfTagTableWithColumnsArgs,
                    ResourceLfTagTableWithColumnsArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[ResourceLfTagTimeoutsArgs, ResourceLfTagTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResourceLfTagArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[
            pulumi.Input[
                Union[ResourceLfTagDatabaseArgs, ResourceLfTagDatabaseArgsDict]
            ]
        ] = ...,
        lf_tag: Optional[
            pulumi.Input[Union[ResourceLfTagLfTagArgs, ResourceLfTagLfTagArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[
            pulumi.Input[Union[ResourceLfTagTableArgs, ResourceLfTagTableArgsDict]]
        ] = ...,
        table_with_columns: Optional[
            pulumi.Input[
                Union[
                    ResourceLfTagTableWithColumnsArgs,
                    ResourceLfTagTableWithColumnsArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[ResourceLfTagTimeoutsArgs, ResourceLfTagTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> ResourceLfTag: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[Optional[outputs.ResourceLfTagDatabase]]: ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> pulumi.Output[outputs.ResourceLfTagLfTag]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Output[Optional[outputs.ResourceLfTagTable]]: ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceLfTagTableWithColumns]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ResourceLfTagTimeouts]]: ...
