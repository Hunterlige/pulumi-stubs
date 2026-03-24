import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "TableMagneticStoreWritePropertiesArgs",
    "TableMagneticStoreWritePropertiesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "TableRetentionPropertiesArgs",
    "TableRetentionPropertiesArgsDict",
    "TableSchemaArgs",
    "TableSchemaArgsDict",
    "TableSchemaCompositePartitionKeyArgs",
    "TableSchemaCompositePartitionKeyArgsDict",
]

class TableMagneticStoreWritePropertiesArgsDict(TypedDict):
    enable_magnetic_store_writes: NotRequired[pulumi.Input[_builtins.bool]]
    magnetic_store_rejected_data_location: NotRequired[
        pulumi.Input[
            TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class TableMagneticStoreWritePropertiesArgs:
    def __init__(
        __self__,
        *,
        enable_magnetic_store_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        magnetic_store_rejected_data_location: Optional[
            pulumi.Input[
                TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_magnetic_store_writes.setter
    def enable_magnetic_store_writes(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRejectedDataLocation")
    def magnetic_store_rejected_data_location(
        self,
    ) -> Optional[
        pulumi.Input[
            TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgs
        ]
    ]: ...
    @magnetic_store_rejected_data_location.setter
    def magnetic_store_rejected_data_location(
        self,
        value: Optional[
            pulumi.Input[
                TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgs
            ]
        ],
    ): ...

class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgsDict(
    TypedDict
):
    s3_configuration: NotRequired[
        pulumi.Input[
            TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationArgs:
    def __init__(
        __self__,
        *,
        s3_configuration: Optional[
            pulumi.Input[
                TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgs
        ]
    ]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: Optional[
            pulumi.Input[
                TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgs
            ]
        ],
    ): ...

class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgsDict(
    TypedDict
):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    encryption_option: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    object_key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_option: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        object_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_option.setter
    def encryption_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_key_prefix.setter
    def object_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableRetentionPropertiesArgsDict(TypedDict):
    magnetic_store_retention_period_in_days: pulumi.Input[_builtins.int]
    memory_store_retention_period_in_hours: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class TableRetentionPropertiesArgs:
    def __init__(
        __self__,
        *,
        magnetic_store_retention_period_in_days: pulumi.Input[_builtins.int],
        memory_store_retention_period_in_hours: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(
        self,
    ) -> pulumi.Input[_builtins.int]: ...
    @magnetic_store_retention_period_in_days.setter
    def magnetic_store_retention_period_in_days(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> pulumi.Input[_builtins.int]: ...
    @memory_store_retention_period_in_hours.setter
    def memory_store_retention_period_in_hours(
        self, value: pulumi.Input[_builtins.int]
    ): ...

class TableSchemaArgsDict(TypedDict):
    composite_partition_key: NotRequired[
        pulumi.Input[TableSchemaCompositePartitionKeyArgsDict]
    ]
    ...

@pulumi.input_type
class TableSchemaArgs:
    def __init__(
        __self__,
        *,
        composite_partition_key: Optional[
            pulumi.Input[TableSchemaCompositePartitionKeyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compositePartitionKey")
    def composite_partition_key(
        self,
    ) -> Optional[pulumi.Input[TableSchemaCompositePartitionKeyArgs]]: ...
    @composite_partition_key.setter
    def composite_partition_key(
        self, value: Optional[pulumi.Input[TableSchemaCompositePartitionKeyArgs]]
    ): ...

class TableSchemaCompositePartitionKeyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    enforcement_in_record: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableSchemaCompositePartitionKeyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        enforcement_in_record: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enforcementInRecord")
    def enforcement_in_record(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforcement_in_record.setter
    def enforcement_in_record(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
