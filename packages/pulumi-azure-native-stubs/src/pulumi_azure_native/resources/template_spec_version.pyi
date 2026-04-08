import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TemplateSpecVersionArgs", "TemplateSpecVersion"]

@pulumi.input_type
class TemplateSpecVersionArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        template_spec_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_templates: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedTemplateArtifactArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        main_template: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_spec_version: Optional[pulumi.Input[_builtins.str]] = ...,
        ui_form_definition: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="templateSpecName")
    def template_spec_name(self) -> pulumi.Input[_builtins.str]: ...
    @template_spec_name.setter
    def template_spec_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedTemplates")
    def linked_templates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedTemplateArtifactArgs]]]]: ...
    @linked_templates.setter
    def linked_templates(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedTemplateArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]: ...
    @main_template.setter
    def main_template(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...
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
    @pulumi.getter(name="templateSpecVersion")
    def template_spec_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_spec_version.setter
    def template_spec_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uiFormDefinition")
    def ui_form_definition(self) -> Optional[Any]: ...
    @ui_form_definition.setter
    def ui_form_definition(self, value: Optional[Any]): ...

@pulumi.type_token("azure-native:resources:TemplateSpecVersion")
class TemplateSpecVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_templates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LinkedTemplateArtifactArgs, LinkedTemplateArtifactArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        main_template: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_spec_name: Optional[pulumi.Input[_builtins.str]] = ...,
        template_spec_version: Optional[pulumi.Input[_builtins.str]] = ...,
        ui_form_definition: Optional[Any] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TemplateSpecVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> TemplateSpecVersion: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedTemplates")
    def linked_templates(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.LinkedTemplateArtifactResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uiFormDefinition")
    def ui_form_definition(self) -> pulumi.Output[Optional[Any]]: ...
