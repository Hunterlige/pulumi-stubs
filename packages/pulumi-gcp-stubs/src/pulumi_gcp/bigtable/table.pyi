import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TableArgs", "Table"]

@pulumi.input_type
class TableArgs:
    def __init__(
        __self__,
        *,
        instance_name: pulumi.Input[_builtins.str],
        automated_backup_policy: Optional[
            pulumi.Input[TableAutomatedBackupPolicyArgs]
        ] = ...,
        change_stream_retention: Optional[pulumi.Input[_builtins.str]] = ...,
        column_families: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_key_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        split_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> Optional[pulumi.Input[TableAutomatedBackupPolicyArgs]]: ...
    @automated_backup_policy.setter
    def automated_backup_policy(
        self, value: Optional[pulumi.Input[TableAutomatedBackupPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="changeStreamRetention")
    def change_stream_retention(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @change_stream_retention.setter
    def change_stream_retention(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]]: ...
    @column_families.setter
    def column_families(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowKeySchema")
    def row_key_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_key_schema.setter
    def row_key_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="splitKeys")
    def split_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @split_keys.setter
    def split_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _TableState:
    def __init__(
        __self__,
        *,
        automated_backup_policy: Optional[
            pulumi.Input[TableAutomatedBackupPolicyArgs]
        ] = ...,
        change_stream_retention: Optional[pulumi.Input[_builtins.str]] = ...,
        column_families: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_key_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        split_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> Optional[pulumi.Input[TableAutomatedBackupPolicyArgs]]: ...
    @automated_backup_policy.setter
    def automated_backup_policy(
        self, value: Optional[pulumi.Input[TableAutomatedBackupPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="changeStreamRetention")
    def change_stream_retention(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @change_stream_retention.setter
    def change_stream_retention(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]]: ...
    @column_families.setter
    def column_families(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TableColumnFamilyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowKeySchema")
    def row_key_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_key_schema.setter
    def row_key_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="splitKeys")
    def split_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @split_keys.setter
    def split_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:bigtable/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[
                Union[
                    TableAutomatedBackupPolicyArgs, TableAutomatedBackupPolicyArgsDict
                ]
            ]
        ] = ...,
        change_stream_retention: Optional[pulumi.Input[_builtins.str]] = ...,
        column_families: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TableColumnFamilyArgs, TableColumnFamilyArgsDict]
                    ]
                ]
            ]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_key_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        split_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TableArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[
                Union[
                    TableAutomatedBackupPolicyArgs, TableAutomatedBackupPolicyArgsDict
                ]
            ]
        ] = ...,
        change_stream_retention: Optional[pulumi.Input[_builtins.str]] = ...,
        column_families: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TableColumnFamilyArgs, TableColumnFamilyArgsDict]
                    ]
                ]
            ]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_key_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        split_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> Table: ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> pulumi.Output[outputs.TableAutomatedBackupPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="changeStreamRetention")
    def change_stream_retention(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TableColumnFamily]]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rowKeySchema")
    def row_key_schema(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="splitKeys")
    def split_keys(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
