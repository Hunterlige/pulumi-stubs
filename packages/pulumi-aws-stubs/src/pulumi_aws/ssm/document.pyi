import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DocumentArgs", "Document"]

@pulumi.input_type
class DocumentArgs:
    def __init__(
        __self__,
        *,
        content: pulumi.Input[_builtins.str],
        document_type: pulumi.Input[_builtins.str],
        attachments_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
        ] = ...,
        document_format: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]: ...
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> pulumi.Input[_builtins.str]: ...
    @document_type.setter
    def document_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentsSources")
    def attachments_sources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
    ]: ...
    @attachments_sources.setter
    def attachments_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="documentFormat")
    def document_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_format.setter
    def document_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DocumentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        attachments_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
        ] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        default_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        document_format: Optional[pulumi.Input[_builtins.str]] = ...,
        document_type: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hash: Optional[pulumi.Input[_builtins.str]] = ...,
        hash_type: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_version: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DocumentParameterArgs]]]
        ] = ...,
        permissions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        platform_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentsSources")
    def attachments_sources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
    ]: ...
    @attachments_sources.setter
    def attachments_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DocumentAttachmentsSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentFormat")
    def document_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_format.setter
    def document_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_type.setter
    def document_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hash.setter
    def hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hashType")
    def hash_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hash_type.setter
    def hash_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_version.setter
    def latest_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DocumentParameterArgs]]]]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DocumentParameterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformTypes")
    def platform_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @platform_types.setter
    def platform_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ssm/document:Document")
class Document(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachments_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DocumentAttachmentsSourceArgs,
                            DocumentAttachmentsSourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        document_format: Optional[pulumi.Input[_builtins.str]] = ...,
        document_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DocumentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        attachments_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DocumentAttachmentsSourceArgs,
                            DocumentAttachmentsSourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        default_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        document_format: Optional[pulumi.Input[_builtins.str]] = ...,
        document_type: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hash: Optional[pulumi.Input[_builtins.str]] = ...,
        hash_type: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_version: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DocumentParameterArgs, DocumentParameterArgsDict]
                    ]
                ]
            ]
        ] = ...,
        permissions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        platform_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_type: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Document: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="attachmentsSources")
    def attachments_sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DocumentAttachmentsSource]]]: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentFormat")
    def document_format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hashType")
    def hash_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence[outputs.DocumentParameter]]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="platformTypes")
    def platform_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
