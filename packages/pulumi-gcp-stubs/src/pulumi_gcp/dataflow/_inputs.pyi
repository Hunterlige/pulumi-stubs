import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipelineScheduleInfoArgs",
    "PipelineScheduleInfoArgsDict",
    "PipelineWorkloadArgs",
    "PipelineWorkloadArgsDict",
    "PipelineWorkloadDataflowFlexTemplateRequestArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "PipelineWorkloadDataflowLaunchTemplateRequestArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
]

class PipelineScheduleInfoArgsDict(TypedDict):
    next_job_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineScheduleInfoArgs:
    def __init__(
        __self__,
        *,
        next_job_time: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextJobTime")
    def next_job_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_job_time.setter
    def next_job_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineWorkloadArgsDict(TypedDict):
    dataflow_flex_template_request: NotRequired[
        pulumi.Input[PipelineWorkloadDataflowFlexTemplateRequestArgsDict]
    ]
    dataflow_launch_template_request: NotRequired[
        pulumi.Input[PipelineWorkloadDataflowLaunchTemplateRequestArgsDict]
    ]
    ...

@pulumi.input_type
class PipelineWorkloadArgs:
    def __init__(
        __self__,
        *,
        dataflow_flex_template_request: Optional[
            pulumi.Input[PipelineWorkloadDataflowFlexTemplateRequestArgs]
        ] = ...,
        dataflow_launch_template_request: Optional[
            pulumi.Input[PipelineWorkloadDataflowLaunchTemplateRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataflowFlexTemplateRequest")
    def dataflow_flex_template_request(
        self,
    ) -> Optional[pulumi.Input[PipelineWorkloadDataflowFlexTemplateRequestArgs]]: ...
    @dataflow_flex_template_request.setter
    def dataflow_flex_template_request(
        self,
        value: Optional[pulumi.Input[PipelineWorkloadDataflowFlexTemplateRequestArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataflowLaunchTemplateRequest")
    def dataflow_launch_template_request(
        self,
    ) -> Optional[pulumi.Input[PipelineWorkloadDataflowLaunchTemplateRequestArgs]]: ...
    @dataflow_launch_template_request.setter
    def dataflow_launch_template_request(
        self,
        value: Optional[
            pulumi.Input[PipelineWorkloadDataflowLaunchTemplateRequestArgs]
        ],
    ): ...

class PipelineWorkloadDataflowFlexTemplateRequestArgsDict(TypedDict):
    launch_parameter: pulumi.Input[
        PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgsDict
    ]
    location: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    validate_only: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowFlexTemplateRequestArgs:
    def __init__(
        __self__,
        *,
        launch_parameter: pulumi.Input[
            PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgs
        ],
        location: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        validate_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchParameter")
    def launch_parameter(
        self,
    ) -> pulumi.Input[
        PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgs
    ]: ...
    @launch_parameter.setter
    def launch_parameter(
        self,
        value: pulumi.Input[
            PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgsDict(TypedDict):
    job_name: pulumi.Input[_builtins.str]
    container_spec_gcs_path: NotRequired[pulumi.Input[_builtins.str]]
    environment: NotRequired[
        pulumi.Input[
            PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgsDict
        ]
    ]
    launch_options: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transform_name_mappings: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    update: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterArgs:
    def __init__(
        __self__,
        *,
        job_name: pulumi.Input[_builtins.str],
        container_spec_gcs_path: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgs
            ]
        ] = ...,
        launch_options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transform_name_mappings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerSpecGcsPath")
    def container_spec_gcs_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_spec_gcs_path.setter
    def container_spec_gcs_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environment(
        self,
    ) -> Optional[
        pulumi.Input[
            PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgs
        ]
    ]: ...
    @environment.setter
    def environment(
        self,
        value: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchOptions")
    def launch_options(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @launch_options.setter
    def launch_options(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformNameMappings")
    def transform_name_mappings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @transform_name_mappings.setter
    def transform_name_mappings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgsDict(
    TypedDict
):
    additional_experiments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    additional_user_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    enable_streaming_engine: NotRequired[pulumi.Input[_builtins.bool]]
    flexrs_goal: NotRequired[pulumi.Input[_builtins.str]]
    ip_configuration: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_workers: NotRequired[pulumi.Input[_builtins.int]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    num_workers: NotRequired[pulumi.Input[_builtins.int]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    temp_location: NotRequired[pulumi.Input[_builtins.str]]
    worker_region: NotRequired[pulumi.Input[_builtins.str]]
    worker_zone: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowFlexTemplateRequestLaunchParameterEnvironmentArgs:
    def __init__(
        __self__,
        *,
        additional_experiments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ...,
        flexrs_goal: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        num_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        temp_location: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_region: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_experiments.setter
    def additional_experiments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalUserLabels")
    def additional_user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_user_labels.setter
    def additional_user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_streaming_engine.setter
    def enable_streaming_engine(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flexrsGoal")
    def flexrs_goal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flexrs_goal.setter
    def flexrs_goal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_configuration.setter
    def ip_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_workers.setter
    def num_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @temp_location.setter
    def temp_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerRegion")
    def worker_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_region.setter
    def worker_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerZone")
    def worker_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_zone.setter
    def worker_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineWorkloadDataflowLaunchTemplateRequestArgsDict(TypedDict):
    project_id: pulumi.Input[_builtins.str]
    gcs_path: NotRequired[pulumi.Input[_builtins.str]]
    launch_parameters: NotRequired[
        pulumi.Input[
            PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgsDict
        ]
    ]
    location: NotRequired[pulumi.Input[_builtins.str]]
    validate_only: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowLaunchTemplateRequestArgs:
    def __init__(
        __self__,
        *,
        project_id: pulumi.Input[_builtins.str],
        gcs_path: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_parameters: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgs
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        validate_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcsPath")
    def gcs_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_path.setter
    def gcs_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchParameters")
    def launch_parameters(
        self,
    ) -> Optional[
        pulumi.Input[PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgs]
    ]: ...
    @launch_parameters.setter
    def launch_parameters(
        self,
        value: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgsDict(TypedDict):
    job_name: pulumi.Input[_builtins.str]
    environment: NotRequired[
        pulumi.Input[
            PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgsDict
        ]
    ]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transform_name_mapping: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    update: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersArgs:
    def __init__(
        __self__,
        *,
        job_name: pulumi.Input[_builtins.str],
        environment: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgs
            ]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transform_name_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def environment(
        self,
    ) -> Optional[
        pulumi.Input[
            PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgs
        ]
    ]: ...
    @environment.setter
    def environment(
        self,
        value: Optional[
            pulumi.Input[
                PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformNameMapping")
    def transform_name_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @transform_name_mapping.setter
    def transform_name_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgsDict(
    TypedDict
):
    additional_experiments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    additional_user_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    bypass_temp_dir_validation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_streaming_engine: NotRequired[pulumi.Input[_builtins.bool]]
    ip_configuration: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_workers: NotRequired[pulumi.Input[_builtins.int]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    num_workers: NotRequired[pulumi.Input[_builtins.int]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    temp_location: NotRequired[pulumi.Input[_builtins.str]]
    worker_region: NotRequired[pulumi.Input[_builtins.str]]
    worker_zone: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineWorkloadDataflowLaunchTemplateRequestLaunchParametersEnvironmentArgs:
    def __init__(
        __self__,
        *,
        additional_experiments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        bypass_temp_dir_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        num_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        temp_location: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_region: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_experiments.setter
    def additional_experiments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalUserLabels")
    def additional_user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_user_labels.setter
    def additional_user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bypassTempDirValidation")
    def bypass_temp_dir_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_temp_dir_validation.setter
    def bypass_temp_dir_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_streaming_engine.setter
    def enable_streaming_engine(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_configuration.setter
    def ip_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_workers.setter
    def num_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @temp_location.setter
    def temp_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerRegion")
    def worker_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_region.setter
    def worker_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerZone")
    def worker_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_zone.setter
    def worker_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
