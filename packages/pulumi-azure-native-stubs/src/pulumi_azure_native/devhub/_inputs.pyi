import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ACRArgs",
    "ACRArgsDict",
    "DeploymentPropertiesArgs",
    "DeploymentPropertiesArgsDict",
    "GitHubWorkflowProfileOidcCredentialsArgs",
    "GitHubWorkflowProfileOidcCredentialsArgsDict",
    "GitHubWorkflowProfileArgs",
    "GitHubWorkflowProfileArgsDict",
    "IacTemplateDetailsArgs",
    "IacTemplateDetailsArgsDict",
    "IacTemplatePropertiesArgs",
    "IacTemplatePropertiesArgsDict",
    "StagePropertiesArgs",
    "StagePropertiesArgsDict",
    "WorkflowRunArgs",
    "WorkflowRunArgsDict",
]

class ACRArgsDict(TypedDict):
    acr_registry_name: NotRequired[pulumi.Input[_builtins.str]]
    acr_repository_name: NotRequired[pulumi.Input[_builtins.str]]
    acr_resource_group: NotRequired[pulumi.Input[_builtins.str]]
    acr_subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ACRArgs:
    def __init__(
        __self__,
        *,
        acr_registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        acr_repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
        acr_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        acr_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acrRegistryName")
    def acr_registry_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_registry_name.setter
    def acr_registry_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acrRepositoryName")
    def acr_repository_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_repository_name.setter
    def acr_repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acrResourceGroup")
    def acr_resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_resource_group.setter
    def acr_resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acrSubscriptionId")
    def acr_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_subscription_id.setter
    def acr_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentPropertiesArgsDict(TypedDict):
    helm_chart_path: NotRequired[pulumi.Input[_builtins.str]]
    helm_values: NotRequired[pulumi.Input[_builtins.str]]
    kube_manifest_locations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    manifest_type: NotRequired[pulumi.Input[Union[_builtins.str, ManifestType]]]
    overrides: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeploymentPropertiesArgs:
    def __init__(
        __self__,
        *,
        helm_chart_path: Optional[pulumi.Input[_builtins.str]] = ...,
        helm_values: Optional[pulumi.Input[_builtins.str]] = ...,
        kube_manifest_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        manifest_type: Optional[pulumi.Input[Union[_builtins.str, ManifestType]]] = ...,
        overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="helmChartPath")
    def helm_chart_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @helm_chart_path.setter
    def helm_chart_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="helmValues")
    def helm_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @helm_values.setter
    def helm_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubeManifestLocations")
    def kube_manifest_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kube_manifest_locations.setter
    def kube_manifest_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestType")
    def manifest_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManifestType]]]: ...
    @manifest_type.setter
    def manifest_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManifestType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @overrides.setter
    def overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class GitHubWorkflowProfileOidcCredentialsArgsDict(TypedDict):
    azure_client_id: NotRequired[pulumi.Input[_builtins.str]]
    azure_tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GitHubWorkflowProfileOidcCredentialsArgs:
    def __init__(
        __self__,
        *,
        azure_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureClientId")
    def azure_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_client_id.setter
    def azure_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azureTenantId")
    def azure_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_tenant_id.setter
    def azure_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GitHubWorkflowProfileArgsDict(TypedDict):
    acr: NotRequired[pulumi.Input[ACRArgsDict]]
    aks_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    branch_name: NotRequired[pulumi.Input[_builtins.str]]
    deployment_properties: NotRequired[pulumi.Input[DeploymentPropertiesArgsDict]]
    docker_build_context: NotRequired[pulumi.Input[_builtins.str]]
    dockerfile: NotRequired[pulumi.Input[_builtins.str]]
    last_workflow_run: NotRequired[pulumi.Input[WorkflowRunArgsDict]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    oidc_credentials: NotRequired[
        pulumi.Input[GitHubWorkflowProfileOidcCredentialsArgsDict]
    ]
    repository_name: NotRequired[pulumi.Input[_builtins.str]]
    repository_owner: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GitHubWorkflowProfileArgs:
    def __init__(
        __self__,
        *,
        acr: Optional[pulumi.Input[ACRArgs]] = ...,
        aks_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        branch_name: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_properties: Optional[pulumi.Input[DeploymentPropertiesArgs]] = ...,
        docker_build_context: Optional[pulumi.Input[_builtins.str]] = ...,
        dockerfile: Optional[pulumi.Input[_builtins.str]] = ...,
        last_workflow_run: Optional[pulumi.Input[WorkflowRunArgs]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        oidc_credentials: Optional[
            pulumi.Input[GitHubWorkflowProfileOidcCredentialsArgs]
        ] = ...,
        repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_owner: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acr(self) -> Optional[pulumi.Input[ACRArgs]]: ...
    @acr.setter
    def acr(self, value: Optional[pulumi.Input[ACRArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="aksResourceId")
    def aks_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aks_resource_id.setter
    def aks_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentProperties")
    def deployment_properties(
        self,
    ) -> Optional[pulumi.Input[DeploymentPropertiesArgs]]: ...
    @deployment_properties.setter
    def deployment_properties(
        self, value: Optional[pulumi.Input[DeploymentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dockerBuildContext")
    def docker_build_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docker_build_context.setter
    def docker_build_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dockerfile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dockerfile.setter
    def dockerfile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastWorkflowRun")
    def last_workflow_run(self) -> Optional[pulumi.Input[WorkflowRunArgs]]: ...
    @last_workflow_run.setter
    def last_workflow_run(self, value: Optional[pulumi.Input[WorkflowRunArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oidcCredentials")
    def oidc_credentials(
        self,
    ) -> Optional[pulumi.Input[GitHubWorkflowProfileOidcCredentialsArgs]]: ...
    @oidc_credentials.setter
    def oidc_credentials(
        self, value: Optional[pulumi.Input[GitHubWorkflowProfileOidcCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryOwner")
    def repository_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_owner.setter
    def repository_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IacTemplateDetailsArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    naming_convention: NotRequired[pulumi.Input[_builtins.str]]
    product_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IacTemplateDetailsArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        naming_convention: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="namingConvention")
    def naming_convention(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @naming_convention.setter
    def naming_convention(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IacTemplatePropertiesArgsDict(TypedDict):
    instance_name: NotRequired[pulumi.Input[_builtins.str]]
    instance_stage: NotRequired[pulumi.Input[_builtins.str]]
    quick_start_template_type: NotRequired[
        pulumi.Input[Union[_builtins.str, QuickStartTemplateType]]
    ]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    template_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IacTemplateDetailsArgsDict]]]
    ]
    template_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IacTemplatePropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        quick_start_template_type: Optional[
            pulumi.Input[Union[_builtins.str, QuickStartTemplateType]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        template_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[IacTemplateDetailsArgs]]]
        ] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceStage")
    def instance_stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_stage.setter
    def instance_stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quickStartTemplateType")
    def quick_start_template_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, QuickStartTemplateType]]]: ...
    @quick_start_template_type.setter
    def quick_start_template_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, QuickStartTemplateType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateDetails")
    def template_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IacTemplateDetailsArgs]]]]: ...
    @template_details.setter
    def template_details(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[IacTemplateDetailsArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StagePropertiesArgsDict(TypedDict):
    dependencies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    git_environment: NotRequired[pulumi.Input[_builtins.str]]
    stage_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StagePropertiesArgs:
    def __init__(
        __self__,
        *,
        dependencies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        git_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        stage_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dependencies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dependencies.setter
    def dependencies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitEnvironment")
    def git_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_environment.setter
    def git_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowRunArgsDict(TypedDict):
    workflow_run_status: NotRequired[
        pulumi.Input[Union[_builtins.str, WorkflowRunStatus]]
    ]

@pulumi.input_type
class WorkflowRunArgs:
    def __init__(
        __self__,
        *,
        workflow_run_status: Optional[
            pulumi.Input[Union[_builtins.str, WorkflowRunStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowRunStatus")
    def workflow_run_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkflowRunStatus]]]: ...
    @workflow_run_status.setter
    def workflow_run_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkflowRunStatus]]]
    ): ...
