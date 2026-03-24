import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TemplateArgs", "Template"]

@pulumi.input_type
class TemplateArgs:
    def __init__(
        __self__,
        *,
        template_id: pulumi.Input[_builtins.str],
        version_description: pulumi.Input[_builtins.str],
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_entity: Optional[pulumi.Input[TemplateSourceEntityArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Input[_builtins.str]: ...
    @template_id.setter
    def template_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Input[_builtins.str]: ...
    @version_description.setter
    def version_description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]]: ...
    @permissions.setter
    def permissions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> Optional[pulumi.Input[TemplateSourceEntityArgs]]: ...
    @source_entity.setter
    def source_entity(
        self, value: Optional[pulumi.Input[TemplateSourceEntityArgs]]
    ): ...
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
class _TemplateState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_entity: Optional[pulumi.Input[TemplateSourceEntityArgs]] = ...,
        source_entity_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_description: Optional[pulumi.Input[_builtins.str]] = ...,
        version_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]]: ...
    @permissions.setter
    def permissions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TemplatePermissionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> Optional[pulumi.Input[TemplateSourceEntityArgs]]: ...
    @source_entity.setter
    def source_entity(
        self, value: Optional[pulumi.Input[TemplateSourceEntityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityArn")
    def source_entity_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_entity_arn.setter
    def source_entity_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @version_number.setter
    def version_number(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:quicksight/template:Template")
class Template(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TemplatePermissionArgs, TemplatePermissionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_entity: Optional[
            pulumi.Input[Union[TemplateSourceEntityArgs, TemplateSourceEntityArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_description: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TemplatePermissionArgs, TemplatePermissionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_entity: Optional[
            pulumi.Input[Union[TemplateSourceEntityArgs, TemplateSourceEntityArgsDict]]
        ] = ...,
        source_entity_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_description: Optional[pulumi.Input[_builtins.str]] = ...,
        version_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> Template: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TemplatePermission]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(
        self,
    ) -> pulumi.Output[Optional[outputs.TemplateSourceEntity]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityArn")
    def source_entity_arn(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> pulumi.Output[_builtins.int]: ...
