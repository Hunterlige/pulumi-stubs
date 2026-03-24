import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotebookExecutionArgs", "NotebookExecution"]

@pulumi.input_type
class NotebookExecutionArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        gcs_output_uri: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        custom_environment_spec: Optional[
            pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]
        ] = ...,
        dataform_repository_source: Optional[
            pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]
        ] = ...,
        direct_notebook_source: Optional[
            pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]
        ] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_user: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_notebook_source: Optional[
            pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]
        ] = ...,
        notebook_execution_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_runtime_template_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcsOutputUri")
    def gcs_output_uri(self) -> pulumi.Input[_builtins.str]: ...
    @gcs_output_uri.setter
    def gcs_output_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customEnvironmentSpec")
    def custom_environment_spec(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]]: ...
    @custom_environment_spec.setter
    def custom_environment_spec(
        self, value: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataformRepositorySource")
    def dataform_repository_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]]: ...
    @dataform_repository_source.setter
    def dataform_repository_source(
        self,
        value: Optional[pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="directNotebookSource")
    def direct_notebook_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]]: ...
    @direct_notebook_source.setter
    def direct_notebook_source(
        self, value: Optional[pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionUser")
    def execution_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_user.setter
    def execution_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsNotebookSource")
    def gcs_notebook_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]]: ...
    @gcs_notebook_source.setter
    def gcs_notebook_source(
        self, value: Optional[pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notebookExecutionJobId")
    def notebook_execution_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notebook_execution_job_id.setter
    def notebook_execution_job_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplateResourceName")
    def notebook_runtime_template_resource_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notebook_runtime_template_resource_name.setter
    def notebook_runtime_template_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NotebookExecutionState:
    def __init__(
        __self__,
        *,
        custom_environment_spec: Optional[
            pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]
        ] = ...,
        dataform_repository_source: Optional[
            pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]
        ] = ...,
        direct_notebook_source: Optional[
            pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_user: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_notebook_source: Optional[
            pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]
        ] = ...,
        gcs_output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_execution_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_runtime_template_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customEnvironmentSpec")
    def custom_environment_spec(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]]: ...
    @custom_environment_spec.setter
    def custom_environment_spec(
        self, value: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataformRepositorySource")
    def dataform_repository_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]]: ...
    @dataform_repository_source.setter
    def dataform_repository_source(
        self,
        value: Optional[pulumi.Input[NotebookExecutionDataformRepositorySourceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="directNotebookSource")
    def direct_notebook_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]]: ...
    @direct_notebook_source.setter
    def direct_notebook_source(
        self, value: Optional[pulumi.Input[NotebookExecutionDirectNotebookSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionUser")
    def execution_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_user.setter
    def execution_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsNotebookSource")
    def gcs_notebook_source(
        self,
    ) -> Optional[pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]]: ...
    @gcs_notebook_source.setter
    def gcs_notebook_source(
        self, value: Optional[pulumi.Input[NotebookExecutionGcsNotebookSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsOutputUri")
    def gcs_output_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_output_uri.setter
    def gcs_output_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notebookExecutionJobId")
    def notebook_execution_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notebook_execution_job_id.setter
    def notebook_execution_job_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplateResourceName")
    def notebook_runtime_template_resource_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notebook_runtime_template_resource_name.setter
    def notebook_runtime_template_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:colab/notebookExecution:NotebookExecution")
class NotebookExecution(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_environment_spec: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionCustomEnvironmentSpecArgs,
                    NotebookExecutionCustomEnvironmentSpecArgsDict,
                ]
            ]
        ] = ...,
        dataform_repository_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionDataformRepositorySourceArgs,
                    NotebookExecutionDataformRepositorySourceArgsDict,
                ]
            ]
        ] = ...,
        direct_notebook_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionDirectNotebookSourceArgs,
                    NotebookExecutionDirectNotebookSourceArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_user: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_notebook_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionGcsNotebookSourceArgs,
                    NotebookExecutionGcsNotebookSourceArgsDict,
                ]
            ]
        ] = ...,
        gcs_output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_execution_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_runtime_template_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotebookExecutionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_environment_spec: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionCustomEnvironmentSpecArgs,
                    NotebookExecutionCustomEnvironmentSpecArgsDict,
                ]
            ]
        ] = ...,
        dataform_repository_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionDataformRepositorySourceArgs,
                    NotebookExecutionDataformRepositorySourceArgsDict,
                ]
            ]
        ] = ...,
        direct_notebook_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionDirectNotebookSourceArgs,
                    NotebookExecutionDirectNotebookSourceArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_user: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_notebook_source: Optional[
            pulumi.Input[
                Union[
                    NotebookExecutionGcsNotebookSourceArgs,
                    NotebookExecutionGcsNotebookSourceArgsDict,
                ]
            ]
        ] = ...,
        gcs_output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_execution_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        notebook_runtime_template_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NotebookExecution: ...
    @_builtins.property
    @pulumi.getter(name="customEnvironmentSpec")
    def custom_environment_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.NotebookExecutionCustomEnvironmentSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="dataformRepositorySource")
    def dataform_repository_source(
        self,
    ) -> pulumi.Output[Optional[outputs.NotebookExecutionDataformRepositorySource]]: ...
    @_builtins.property
    @pulumi.getter(name="directNotebookSource")
    def direct_notebook_source(
        self,
    ) -> pulumi.Output[Optional[outputs.NotebookExecutionDirectNotebookSource]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionUser")
    def execution_user(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsNotebookSource")
    def gcs_notebook_source(
        self,
    ) -> pulumi.Output[Optional[outputs.NotebookExecutionGcsNotebookSource]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsOutputUri")
    def gcs_output_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notebookExecutionJobId")
    def notebook_execution_job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplateResourceName")
    def notebook_runtime_template_resource_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
