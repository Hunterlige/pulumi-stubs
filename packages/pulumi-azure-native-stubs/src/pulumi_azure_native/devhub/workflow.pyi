import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkflowArgs", "Workflow"]

@pulumi.input_type
class WorkflowArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        builder_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dockerfile_generation_mode: Optional[
            pulumi.Input[Union[_builtins.str, DockerfileGenerationMode]]
        ] = ...,
        dockerfile_output_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_language: Optional[
            pulumi.Input[Union[_builtins.str, GenerationLanguage]]
        ] = ...,
        github_workflow_profile: Optional[
            pulumi.Input[GitHubWorkflowProfileArgs]
        ] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        language_version: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_generation_mode: Optional[
            pulumi.Input[Union[_builtins.str, ManifestGenerationMode]]
        ] = ...,
        manifest_output_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_type: Optional[
            pulumi.Input[Union[_builtins.str, GenerationManifestType]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_name.setter
    def app_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="builderVersion")
    def builder_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @builder_version.setter
    def builder_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerfileGenerationMode")
    def dockerfile_generation_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DockerfileGenerationMode]]]: ...
    @dockerfile_generation_mode.setter
    def dockerfile_generation_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DockerfileGenerationMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dockerfileOutputDirectory")
    def dockerfile_output_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dockerfile_output_directory.setter
    def dockerfile_output_directory(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="generationLanguage")
    def generation_language(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, GenerationLanguage]]]: ...
    @generation_language.setter
    def generation_language(
        self, value: Optional[pulumi.Input[Union[_builtins.str, GenerationLanguage]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="githubWorkflowProfile")
    def github_workflow_profile(
        self,
    ) -> Optional[pulumi.Input[GitHubWorkflowProfileArgs]]: ...
    @github_workflow_profile.setter
    def github_workflow_profile(
        self, value: Optional[pulumi.Input[GitHubWorkflowProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_tag.setter
    def image_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_version.setter
    def language_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manifestGenerationMode")
    def manifest_generation_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManifestGenerationMode]]]: ...
    @manifest_generation_mode.setter
    def manifest_generation_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ManifestGenerationMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestOutputDirectory")
    def manifest_output_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manifest_output_directory.setter
    def manifest_output_directory(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestType")
    def manifest_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, GenerationManifestType]]]: ...
    @manifest_type.setter
    def manifest_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, GenerationManifestType]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:devhub:Workflow")
class Workflow(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        builder_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dockerfile_generation_mode: Optional[
            pulumi.Input[Union[_builtins.str, DockerfileGenerationMode]]
        ] = ...,
        dockerfile_output_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_language: Optional[
            pulumi.Input[Union[_builtins.str, GenerationLanguage]]
        ] = ...,
        github_workflow_profile: Optional[
            pulumi.Input[
                Union[GitHubWorkflowProfileArgs, GitHubWorkflowProfileArgsDict]
            ]
        ] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        language_version: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_generation_mode: Optional[
            pulumi.Input[Union[_builtins.str, ManifestGenerationMode]]
        ] = ...,
        manifest_output_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_type: Optional[
            pulumi.Input[Union[_builtins.str, GenerationManifestType]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkflowArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Workflow: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="builderVersion")
    def builder_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dockerfileGenerationMode")
    def dockerfile_generation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dockerfileOutputDirectory")
    def dockerfile_output_directory(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="generationLanguage")
    def generation_language(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="githubWorkflowProfile")
    def github_workflow_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.GitHubWorkflowProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manifestGenerationMode")
    def manifest_generation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="manifestOutputDirectory")
    def manifest_output_directory(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="manifestType")
    def manifest_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
