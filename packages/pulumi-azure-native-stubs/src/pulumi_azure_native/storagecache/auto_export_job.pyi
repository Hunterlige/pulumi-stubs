import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AutoExportJobArgs", "AutoExportJob"]

@pulumi.input_type
class AutoExportJobArgs:
    def __init__(
        __self__,
        *,
        aml_filesystem_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        admin_status: Optional[
            pulumi.Input[Union[_builtins.str, AutoExportJobAdminStatus]]
        ] = ...,
        auto_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_export_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, AutoExportStatusType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amlFilesystemName")
    def aml_filesystem_name(self) -> pulumi.Input[_builtins.str]: ...
    @aml_filesystem_name.setter
    def aml_filesystem_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adminStatus")
    def admin_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoExportJobAdminStatus]]]: ...
    @admin_status.setter
    def admin_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AutoExportJobAdminStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoExportJobName")
    def auto_export_job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_export_job_name.setter
    def auto_export_job_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoExportPrefixes")
    def auto_export_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @auto_export_prefixes.setter
    def auto_export_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoExportStatusType]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AutoExportStatusType]]]
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

@pulumi.type_token("azure-native:storagecache:AutoExportJob")
class AutoExportJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_status: Optional[
            pulumi.Input[Union[_builtins.str, AutoExportJobAdminStatus]]
        ] = ...,
        aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_export_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, AutoExportStatusType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AutoExportJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AutoExportJob: ...
    @_builtins.property
    @pulumi.getter(name="adminStatus")
    def admin_status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoExportPrefixes")
    def auto_export_prefixes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesDiscovered")
    def current_iteration_files_discovered(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesExported")
    def current_iteration_files_exported(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesFailed")
    def current_iteration_files_failed(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationMiBDiscovered")
    def current_iteration_mi_b_discovered(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationMiBExported")
    def current_iteration_mi_b_exported(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="exportIterationCount")
    def export_iteration_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lastCompletionTimeUTC")
    def last_completion_time_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastStartedTimeUTC")
    def last_started_time_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulIterationCompletionTimeUTC")
    def last_successful_iteration_completion_time_utc(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesExported")
    def total_files_exported(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesFailed")
    def total_files_failed(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="totalMiBExported")
    def total_mi_b_exported(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
