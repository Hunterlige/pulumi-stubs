import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DocumentClassifierInputDataConfig",
    "DocumentClassifierInputDataConfigAugmentedManifest",
    "DocumentClassifierOutputDataConfig",
    "DocumentClassifierVpcConfig",
    "EntityRecognizerInputDataConfig",
    "EntityRecognizerInputDataConfigAnnotations",
    "EntityRecognizerInputDataConfigAugmentedManifest",
    "EntityRecognizerInputDataConfigDocuments",
    "EntityRecognizerInputDataConfigEntityList",
    "EntityRecognizerInputDataConfigEntityType",
    "EntityRecognizerVpcConfig",
]

@pulumi.output_type
class DocumentClassifierInputDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        augmented_manifests: Optional[
            Sequence[outputs.DocumentClassifierInputDataConfigAugmentedManifest]
        ] = ...,
        data_format: Optional[_builtins.str] = ...,
        label_delimiter: Optional[_builtins.str] = ...,
        s3_uri: Optional[_builtins.str] = ...,
        test_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="augmentedManifests")
    def augmented_manifests(
        self,
    ) -> Optional[
        Sequence[outputs.DocumentClassifierInputDataConfigAugmentedManifest]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelDelimiter")
    def label_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DocumentClassifierInputDataConfigAugmentedManifest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_names: Sequence[_builtins.str],
        s3_uri: _builtins.str,
        annotation_data_s3_uri: Optional[_builtins.str] = ...,
        document_type: Optional[_builtins.str] = ...,
        source_documents_s3_uri: Optional[_builtins.str] = ...,
        split: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeNames")
    def attribute_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def split(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DocumentClassifierOutputDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_uri: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
        output_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputS3Uri")
    def output_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DocumentClassifierVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class EntityRecognizerInputDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_types: Sequence[outputs.EntityRecognizerInputDataConfigEntityType],
        annotations: Optional[outputs.EntityRecognizerInputDataConfigAnnotations] = ...,
        augmented_manifests: Optional[
            Sequence[outputs.EntityRecognizerInputDataConfigAugmentedManifest]
        ] = ...,
        data_format: Optional[_builtins.str] = ...,
        documents: Optional[outputs.EntityRecognizerInputDataConfigDocuments] = ...,
        entity_list: Optional[outputs.EntityRecognizerInputDataConfigEntityList] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityTypes")
    def entity_types(
        self,
    ) -> Sequence[outputs.EntityRecognizerInputDataConfigEntityType]: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[outputs.EntityRecognizerInputDataConfigAnnotations]: ...
    @_builtins.property
    @pulumi.getter(name="augmentedManifests")
    def augmented_manifests(
        self,
    ) -> Optional[
        Sequence[outputs.EntityRecognizerInputDataConfigAugmentedManifest]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def documents(
        self,
    ) -> Optional[outputs.EntityRecognizerInputDataConfigDocuments]: ...
    @_builtins.property
    @pulumi.getter(name="entityList")
    def entity_list(
        self,
    ) -> Optional[outputs.EntityRecognizerInputDataConfigEntityList]: ...

@pulumi.output_type
class EntityRecognizerInputDataConfigAnnotations(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, s3_uri: _builtins.str, test_s3_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntityRecognizerInputDataConfigAugmentedManifest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_names: Sequence[_builtins.str],
        s3_uri: _builtins.str,
        annotation_data_s3_uri: Optional[_builtins.str] = ...,
        document_type: Optional[_builtins.str] = ...,
        source_documents_s3_uri: Optional[_builtins.str] = ...,
        split: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeNames")
    def attribute_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def split(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntityRecognizerInputDataConfigDocuments(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_uri: _builtins.str,
        input_format: Optional[_builtins.str] = ...,
        test_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntityRecognizerInputDataConfigEntityList(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class EntityRecognizerInputDataConfigEntityType(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class EntityRecognizerVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
