

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DocumentClassifierInputDataConfigArgs', 'DocumentClassifierInputDataConfigArgsDict', ..., ..., 'DocumentClassifierOutputDataConfigArgs', 'DocumentClassifierOutputDataConfigArgsDict', 'DocumentClassifierVpcConfigArgs', 'DocumentClassifierVpcConfigArgsDict', 'EntityRecognizerInputDataConfigArgs', 'EntityRecognizerInputDataConfigArgsDict', 'EntityRecognizerInputDataConfigAnnotationsArgs', 'EntityRecognizerInputDataConfigAnnotationsArgsDict', ..., ..., 'EntityRecognizerInputDataConfigDocumentsArgs', 'EntityRecognizerInputDataConfigDocumentsArgsDict', 'EntityRecognizerInputDataConfigEntityListArgs', 'EntityRecognizerInputDataConfigEntityListArgsDict', 'EntityRecognizerInputDataConfigEntityTypeArgs', 'EntityRecognizerInputDataConfigEntityTypeArgsDict', 'EntityRecognizerVpcConfigArgs', 'EntityRecognizerVpcConfigArgsDict']
class DocumentClassifierInputDataConfigArgsDict(TypedDict):
    augmented_manifests: NotRequired[pulumi.Input[Sequence[pulumi.Input[DocumentClassifierInputDataConfigAugmentedManifestArgsDict]]]]
    data_format: NotRequired[pulumi.Input[_builtins.str]]
    label_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    s3_uri: NotRequired[pulumi.Input[_builtins.str]]
    test_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DocumentClassifierInputDataConfigArgs:
    def __init__(__self__, *, augmented_manifests: Optional[pulumi.Input[Sequence[pulumi.Input[DocumentClassifierInputDataConfigAugmentedManifestArgs]]]] = ..., data_format: Optional[pulumi.Input[_builtins.str]] = ..., label_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., s3_uri: Optional[pulumi.Input[_builtins.str]] = ..., test_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="augmentedManifests")
    def augmented_manifests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DocumentClassifierInputDataConfigAugmentedManifestArgs]]]]:
        
        ...
    
    @augmented_manifests.setter
    def augmented_manifests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DocumentClassifierInputDataConfigAugmentedManifestArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelDelimiter")
    def label_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label_delimiter.setter
    def label_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @test_s3_uri.setter
    def test_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DocumentClassifierInputDataConfigAugmentedManifestArgsDict(TypedDict):
    attribute_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    s3_uri: pulumi.Input[_builtins.str]
    annotation_data_s3_uri: NotRequired[pulumi.Input[_builtins.str]]
    document_type: NotRequired[pulumi.Input[_builtins.str]]
    source_documents_s3_uri: NotRequired[pulumi.Input[_builtins.str]]
    split: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DocumentClassifierInputDataConfigAugmentedManifestArgs:
    def __init__(__self__, *, attribute_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], s3_uri: pulumi.Input[_builtins.str], annotation_data_s3_uri: Optional[pulumi.Input[_builtins.str]] = ..., document_type: Optional[pulumi.Input[_builtins.str]] = ..., source_documents_s3_uri: Optional[pulumi.Input[_builtins.str]] = ..., split: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeNames")
    def attribute_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @attribute_names.setter
    def attribute_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation_data_s3_uri.setter
    def annotation_data_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_type.setter
    def document_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_documents_s3_uri.setter
    def source_documents_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def split(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @split.setter
    def split(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DocumentClassifierOutputDataConfigArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    output_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DocumentClassifierOutputDataConfigArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., output_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputS3Uri")
    def output_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_s3_uri.setter
    def output_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DocumentClassifierVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class DocumentClassifierVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigArgsDict(TypedDict):
    entity_types: pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigEntityTypeArgsDict]]]
    annotations: NotRequired[pulumi.Input[EntityRecognizerInputDataConfigAnnotationsArgsDict]]
    augmented_manifests: NotRequired[pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigAugmentedManifestArgsDict]]]]
    data_format: NotRequired[pulumi.Input[_builtins.str]]
    documents: NotRequired[pulumi.Input[EntityRecognizerInputDataConfigDocumentsArgsDict]]
    entity_list: NotRequired[pulumi.Input[EntityRecognizerInputDataConfigEntityListArgsDict]]


@pulumi.input_type
class EntityRecognizerInputDataConfigArgs:
    def __init__(__self__, *, entity_types: pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigEntityTypeArgs]]], annotations: Optional[pulumi.Input[EntityRecognizerInputDataConfigAnnotationsArgs]] = ..., augmented_manifests: Optional[pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigAugmentedManifestArgs]]]] = ..., data_format: Optional[pulumi.Input[_builtins.str]] = ..., documents: Optional[pulumi.Input[EntityRecognizerInputDataConfigDocumentsArgs]] = ..., entity_list: Optional[pulumi.Input[EntityRecognizerInputDataConfigEntityListArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityTypes")
    def entity_types(self) -> pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigEntityTypeArgs]]]:
        
        ...
    
    @entity_types.setter
    def entity_types(self, value: pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigEntityTypeArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[EntityRecognizerInputDataConfigAnnotationsArgs]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[EntityRecognizerInputDataConfigAnnotationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="augmentedManifests")
    def augmented_manifests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigAugmentedManifestArgs]]]]:
        
        ...
    
    @augmented_manifests.setter
    def augmented_manifests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EntityRecognizerInputDataConfigAugmentedManifestArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def documents(self) -> Optional[pulumi.Input[EntityRecognizerInputDataConfigDocumentsArgs]]:
        
        ...
    
    @documents.setter
    def documents(self, value: Optional[pulumi.Input[EntityRecognizerInputDataConfigDocumentsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityList")
    def entity_list(self) -> Optional[pulumi.Input[EntityRecognizerInputDataConfigEntityListArgs]]:
        
        ...
    
    @entity_list.setter
    def entity_list(self, value: Optional[pulumi.Input[EntityRecognizerInputDataConfigEntityListArgs]]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigAnnotationsArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]
    test_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EntityRecognizerInputDataConfigAnnotationsArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str], test_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @test_s3_uri.setter
    def test_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigAugmentedManifestArgsDict(TypedDict):
    attribute_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    s3_uri: pulumi.Input[_builtins.str]
    annotation_data_s3_uri: NotRequired[pulumi.Input[_builtins.str]]
    document_type: NotRequired[pulumi.Input[_builtins.str]]
    source_documents_s3_uri: NotRequired[pulumi.Input[_builtins.str]]
    split: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EntityRecognizerInputDataConfigAugmentedManifestArgs:
    def __init__(__self__, *, attribute_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], s3_uri: pulumi.Input[_builtins.str], annotation_data_s3_uri: Optional[pulumi.Input[_builtins.str]] = ..., document_type: Optional[pulumi.Input[_builtins.str]] = ..., source_documents_s3_uri: Optional[pulumi.Input[_builtins.str]] = ..., split: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeNames")
    def attribute_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @attribute_names.setter
    def attribute_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation_data_s3_uri.setter
    def annotation_data_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_type.setter
    def document_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_documents_s3_uri.setter
    def source_documents_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def split(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @split.setter
    def split(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigDocumentsArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]
    input_format: NotRequired[pulumi.Input[_builtins.str]]
    test_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EntityRecognizerInputDataConfigDocumentsArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str], input_format: Optional[pulumi.Input[_builtins.str]] = ..., test_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_format.setter
    def input_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testS3Uri")
    def test_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @test_s3_uri.setter
    def test_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigEntityListArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class EntityRecognizerInputDataConfigEntityListArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EntityRecognizerInputDataConfigEntityTypeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class EntityRecognizerInputDataConfigEntityTypeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EntityRecognizerVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class EntityRecognizerVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


