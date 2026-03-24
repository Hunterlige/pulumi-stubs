import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataRepositoryAssociationArgs", "DataRepositoryAssociation"]

@pulumi.input_type
class DataRepositoryAssociationArgs:
    def __init__(
        __self__,
        *,
        data_repository_path: pulumi.Input[_builtins.str],
        file_system_id: pulumi.Input[_builtins.str],
        file_system_path: pulumi.Input[_builtins.str],
        batch_import_meta_data_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_data_in_filesystem: Optional[pulumi.Input[_builtins.bool]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[pulumi.Input[DataRepositoryAssociationS3Args]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRepositoryPath")
    def data_repository_path(self) -> pulumi.Input[_builtins.str]: ...
    @data_repository_path.setter
    def data_repository_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]: ...
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> pulumi.Input[_builtins.str]: ...
    @file_system_path.setter
    def file_system_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchImportMetaDataOnCreate")
    def batch_import_meta_data_on_create(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_import_meta_data_on_create.setter
    def batch_import_meta_data_on_create(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteDataInFilesystem")
    def delete_data_in_filesystem(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_data_in_filesystem.setter
    def delete_data_in_filesystem(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @imported_file_chunk_size.setter
    def imported_file_chunk_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[DataRepositoryAssociationS3Args]]: ...
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[DataRepositoryAssociationS3Args]]): ...
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
class _DataRepositoryAssociationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        batch_import_meta_data_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_repository_path: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_data_in_filesystem: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[pulumi.Input[DataRepositoryAssociationS3Args]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="batchImportMetaDataOnCreate")
    def batch_import_meta_data_on_create(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_import_meta_data_on_create.setter
    def batch_import_meta_data_on_create(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataRepositoryPath")
    def data_repository_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_repository_path.setter
    def data_repository_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteDataInFilesystem")
    def delete_data_in_filesystem(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_data_in_filesystem.setter
    def delete_data_in_filesystem(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_path.setter
    def file_system_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @imported_file_chunk_size.setter
    def imported_file_chunk_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[DataRepositoryAssociationS3Args]]: ...
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[DataRepositoryAssociationS3Args]]): ...
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

@pulumi.type_token(...)
class DataRepositoryAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        batch_import_meta_data_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_repository_path: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_data_in_filesystem: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[
            pulumi.Input[
                Union[
                    DataRepositoryAssociationS3Args, DataRepositoryAssociationS3ArgsDict
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataRepositoryAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        batch_import_meta_data_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_repository_path: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_data_in_filesystem: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[
            pulumi.Input[
                Union[
                    DataRepositoryAssociationS3Args, DataRepositoryAssociationS3ArgsDict
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DataRepositoryAssociation: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="batchImportMetaDataOnCreate")
    def batch_import_meta_data_on_create(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="dataRepositoryPath")
    def data_repository_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteDataInFilesystem")
    def delete_data_in_filesystem(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Output[outputs.DataRepositoryAssociationS3]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
