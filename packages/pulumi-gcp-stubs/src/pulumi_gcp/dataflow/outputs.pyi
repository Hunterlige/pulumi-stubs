import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipelineScheduleInfo",
    "PipelineWorkload",
    "PipelineWorkloadDataflowFlexTemplateRequest",
    ...,
    ...,
    "PipelineWorkloadDataflowLaunchTemplateRequest",
    ...,
    ...,
]

@pulumi.output_type
class PipelineScheduleInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        next_job_time: Optional[_builtins.str] = ...,
        schedule: Optional[_builtins.str] = ...,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextJobTime")
    def next_job_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineWorkload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataflow_flex_template_request: Optional[
            outputs.PipelineWorkloadDataflowFlexTemplateRequest
        ] = ...,
        dataflow_launch_template_request: Optional[
            outputs.PipelineWorkloadDataflowLaunchTemplateRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataflowFlexTemplateRequest")
    def dataflow_flex_template_request(
        self,
    ) -> Optional[outputs.PipelineWorkloadDataflowFlexTemplateRequest]: ...
    @_builtins.property
    @pulumi.getter(name="dataflowLaunchTemplateRequest")
    def dataflow_launch_template_request(
        self,
    ) -> Optional[outputs.PipelineWorkloadDataflowLaunchTemplateRequest]: ...

@pulumi.output_type
class PipelineWorkloadDataflowFlexTemplateRequest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        launch_parameter: outputs.PipelineWorkloadDataflowFlexTemplateRequestLaunchParameter,
        location: _builtins.str,
        project_id: _builtins.str,
        validate_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchParameter")
    def launch_parameter(
        self,
    ) -> outputs.PipelineWorkloadDataflowFlexTemplateRequestLaunchParameter: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_name: _builtins.str,
        container_spec_gcs_path: Optional[_builtins.str] = ...,
        environment: Optional[
            outputs.PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironment
        ] = ...,
        launch_options: Optional[Mapping[str, _builtins.str]] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        transform_name_mappings: Optional[Mapping[str, _builtins.str]] = ...,
        update: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerSpecGcsPath")
    def container_spec_gcs_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(
        self,
    ) -> Optional[
        outputs.PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="launchOptions")
    def launch_options(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transformNameMappings")
    def transform_name_mappings(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_experiments: Optional[Sequence[_builtins.str]] = ...,
        additional_user_labels: Optional[Mapping[str, _builtins.str]] = ...,
        enable_streaming_engine: Optional[_builtins.bool] = ...,
        flexrs_goal: Optional[_builtins.str] = ...,
        ip_configuration: Optional[_builtins.str] = ...,
        kms_key_name: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        max_workers: Optional[_builtins.int] = ...,
        network: Optional[_builtins.str] = ...,
        num_workers: Optional[_builtins.int] = ...,
        service_account_email: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
        temp_location: Optional[_builtins.str] = ...,
        worker_region: Optional[_builtins.str] = ...,
        worker_zone: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalUserLabels")
    def additional_user_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="flexrsGoal")
    def flexrs_goal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerRegion")
    def worker_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerZone")
    def worker_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineWorkloadDataflowLaunchTemplateRequest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        project_id: _builtins.str,
        gcs_path: Optional[_builtins.str] = ...,
        launch_parameters: Optional[
            outputs.PipelineWorkloadDataflowLaunchTemplateRequestLaunchParameters
        ] = ...,
        location: Optional[_builtins.str] = ...,
        validate_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcsPath")
    def gcs_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchParameters")
    def launch_parameters(
        self,
    ) -> Optional[
        outputs.PipelineWorkloadDataflowLaunchTemplateRequestLaunchParameters
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_name: _builtins.str,
        environment: Optional[
            outputs.PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironment
        ] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        transform_name_mapping: Optional[Mapping[str, _builtins.str]] = ...,
        update: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def environment(
        self,
    ) -> Optional[
        outputs.PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironment
    ]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transformNameMapping")
    def transform_name_mapping(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_experiments: Optional[Sequence[_builtins.str]] = ...,
        additional_user_labels: Optional[Mapping[str, _builtins.str]] = ...,
        bypass_temp_dir_validation: Optional[_builtins.bool] = ...,
        enable_streaming_engine: Optional[_builtins.bool] = ...,
        ip_configuration: Optional[_builtins.str] = ...,
        kms_key_name: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        max_workers: Optional[_builtins.int] = ...,
        network: Optional[_builtins.str] = ...,
        num_workers: Optional[_builtins.int] = ...,
        service_account_email: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
        temp_location: Optional[_builtins.str] = ...,
        worker_region: Optional[_builtins.str] = ...,
        worker_zone: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalUserLabels")
    def additional_user_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bypassTempDirValidation")
    def bypass_temp_dir_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerRegion")
    def worker_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerZone")
    def worker_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...
