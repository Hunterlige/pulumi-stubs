import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
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
        format: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        table_bucket_arn: pulumi.Input[_builtins.str],
        encryption_configuration: Optional[
            pulumi.Input[TableEncryptionConfigurationArgs]
        ] = ...,
        maintenance_configuration: Optional[
            pulumi.Input[TableMaintenanceConfigurationArgs]
        ] = ...,
        metadata: Optional[pulumi.Input[TableMetadataArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Input[_builtins.str]: ...
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[TableEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[TableEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(
        self,
    ) -> Optional[pulumi.Input[TableMaintenanceConfigurationArgs]]: ...
    @maintenance_configuration.setter
    def maintenance_configuration(
        self, value: Optional[pulumi.Input[TableMaintenanceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[TableMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[TableMetadataArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _TableState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[TableEncryptionConfigurationArgs]
        ] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_configuration: Optional[
            pulumi.Input[TableMaintenanceConfigurationArgs]
        ] = ...,
        metadata: Optional[pulumi.Input[TableMetadataArgs]] = ...,
        metadata_location: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_by: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_token: Optional[pulumi.Input[_builtins.str]] = ...,
        warehouse_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[TableEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[TableEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(
        self,
    ) -> Optional[pulumi.Input[TableMaintenanceConfigurationArgs]]: ...
    @maintenance_configuration.setter
    def maintenance_configuration(
        self, value: Optional[pulumi.Input[TableMaintenanceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[TableMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[TableMetadataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataLocation")
    def metadata_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_location.setter
    def metadata_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modified_by.setter
    def modified_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_token.setter
    def version_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warehouseLocation")
    def warehouse_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warehouse_location.setter
    def warehouse_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:s3tables/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    TableEncryptionConfigurationArgs,
                    TableEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_configuration: Optional[
            pulumi.Input[
                Union[
                    TableMaintenanceConfigurationArgs,
                    TableMaintenanceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Union[TableMetadataArgs, TableMetadataArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    TableEncryptionConfigurationArgs,
                    TableEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_configuration: Optional[
            pulumi.Input[
                Union[
                    TableMaintenanceConfigurationArgs,
                    TableMaintenanceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Union[TableMetadataArgs, TableMetadataArgsDict]]
        ] = ...,
        metadata_location: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_by: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_token: Optional[pulumi.Input[_builtins.str]] = ...,
        warehouse_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Table: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> pulumi.Output[outputs.TableEncryptionConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfiguration")
    def maintenance_configuration(
        self,
    ) -> pulumi.Output[outputs.TableMaintenanceConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[outputs.TableMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="metadataLocation")
    def metadata_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="warehouseLocation")
    def warehouse_location(self) -> pulumi.Output[_builtins.str]: ...
