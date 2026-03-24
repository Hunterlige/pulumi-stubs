import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiIndexArgs", "AiIndex"]

@pulumi.input_type
class AiIndexArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        metadata: pulumi.Input[AiIndexMetadataArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[pulumi.Input[AiIndexEncryptionSpecArgs]] = ...,
        index_update_method: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Input[AiIndexMetadataArgs]: ...
    @metadata.setter
    def metadata(self, value: pulumi.Input[AiIndexMetadataArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[AiIndexEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[AiIndexEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="indexUpdateMethod")
    def index_update_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_update_method.setter
    def index_update_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AiIndexState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployed_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AiIndexDeployedIndexArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[pulumi.Input[AiIndexEncryptionSpecArgs]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        index_stats: Optional[
            pulumi.Input[Sequence[pulumi.Input[AiIndexIndexStatArgs]]]
        ] = ...,
        index_update_method: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        metadata: Optional[pulumi.Input[AiIndexMetadataArgs]] = ...,
        metadata_schema_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deployedIndexes")
    def deployed_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexDeployedIndexArgs]]]]: ...
    @deployed_indexes.setter
    def deployed_indexes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexDeployedIndexArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[AiIndexEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[AiIndexEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexStats")
    def index_stats(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexIndexStatArgs]]]]: ...
    @index_stats.setter
    def index_stats(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexIndexStatArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="indexUpdateMethod")
    def index_update_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_update_method.setter
    def index_update_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[AiIndexMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[AiIndexMetadataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataSchemaUri")
    def metadata_schema_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_schema_uri.setter
    def metadata_schema_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:vertex/aiIndex:AiIndex")
class AiIndex(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[AiIndexEncryptionSpecArgs, AiIndexEncryptionSpecArgsDict]
            ]
        ] = ...,
        index_update_method: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        metadata: Optional[
            pulumi.Input[Union[AiIndexMetadataArgs, AiIndexMetadataArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiIndexArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployed_indexes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AiIndexDeployedIndexArgs, AiIndexDeployedIndexArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[AiIndexEncryptionSpecArgs, AiIndexEncryptionSpecArgsDict]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        index_stats: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[AiIndexIndexStatArgs, AiIndexIndexStatArgsDict]]
                ]
            ]
        ] = ...,
        index_update_method: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        metadata: Optional[
            pulumi.Input[Union[AiIndexMetadataArgs, AiIndexMetadataArgsDict]]
        ] = ...,
        metadata_schema_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AiIndex: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deployedIndexes")
    def deployed_indexes(
        self,
    ) -> pulumi.Output[Sequence[outputs.AiIndexDeployedIndex]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.AiIndexEncryptionSpec]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexStats")
    def index_stats(self) -> pulumi.Output[Sequence[outputs.AiIndexIndexStat]]: ...
    @_builtins.property
    @pulumi.getter(name="indexUpdateMethod")
    def index_update_method(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[outputs.AiIndexMetadata]: ...
    @_builtins.property
    @pulumi.getter(name="metadataSchemaUri")
    def metadata_schema_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
