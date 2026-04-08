import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RunbookArgs", "Runbook"]

@pulumi.input_type
class RunbookArgs:
    def __init__(
        __self__,
        *,
        automation_account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        runbook_type: pulumi.Input[Union[_builtins.str, RunbookTypeEnum]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        draft: Optional[pulumi.Input[RunbookDraftArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_activity_trace: Optional[pulumi.Input[_builtins.int]] = ...,
        log_progress: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_verbose: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        publish_content_link: Optional[pulumi.Input[ContentLinkArgs]] = ...,
        runbook_name: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="runbookType")
    def runbook_type(self) -> pulumi.Input[Union[_builtins.str, RunbookTypeEnum]]: ...
    @runbook_type.setter
    def runbook_type(
        self, value: pulumi.Input[Union[_builtins.str, RunbookTypeEnum]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def draft(self) -> Optional[pulumi.Input[RunbookDraftArgs]]: ...
    @draft.setter
    def draft(self, value: Optional[pulumi.Input[RunbookDraftArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logActivityTrace")
    def log_activity_trace(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @log_activity_trace.setter
    def log_activity_trace(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="logProgress")
    def log_progress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_progress.setter
    def log_progress(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_verbose.setter
    def log_verbose(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publishContentLink")
    def publish_content_link(self) -> Optional[pulumi.Input[ContentLinkArgs]]: ...
    @publish_content_link.setter
    def publish_content_link(self, value: Optional[pulumi.Input[ContentLinkArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runbookName")
    def runbook_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runbook_name.setter
    def runbook_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_environment.setter
    def runtime_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:automation:Runbook")
class Runbook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        draft: Optional[
            pulumi.Input[Union[RunbookDraftArgs, RunbookDraftArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_activity_trace: Optional[pulumi.Input[_builtins.int]] = ...,
        log_progress: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_verbose: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        publish_content_link: Optional[
            pulumi.Input[Union[ContentLinkArgs, ContentLinkArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        runbook_name: Optional[pulumi.Input[_builtins.str]] = ...,
        runbook_type: Optional[
            pulumi.Input[Union[_builtins.str, RunbookTypeEnum]]
        ] = ...,
        runtime_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RunbookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Runbook: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def draft(self) -> pulumi.Output[Optional[outputs.RunbookDraftResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logActivityTrace")
    def log_activity_trace(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="logProgress")
    def log_progress(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputTypes")
    def output_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, outputs.RunbookParameterResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publishContentLink")
    def publish_content_link(
        self,
    ) -> pulumi.Output[Optional[outputs.ContentLinkResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="runbookType")
    def runbook_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
