

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FlexTemplateJobArgs', 'FlexTemplateJob']
@pulumi.input_type
class FlexTemplateJobArgs:
    def __init__(__self__, *, container_spec_gcs_path: pulumi.Input[_builtins.str], additional_experiments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., additional_pipeline_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autoscaling_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ..., ip_configuration: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launcher_machine_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_workers: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., num_workers: Optional[pulumi.Input[_builtins.int]] = ..., on_delete: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sdk_container_image: Optional[pulumi.Input[_builtins.str]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., skip_wait_on_job_termination: Optional[pulumi.Input[_builtins.bool]] = ..., staging_location: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., temp_location: Optional[pulumi.Input[_builtins.str]] = ..., transform_name_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerSpecGcsPath")
    def container_spec_gcs_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_spec_gcs_path.setter
    def container_spec_gcs_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_experiments.setter
    def additional_experiments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalPipelineOptions")
    def additional_pipeline_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_pipeline_options.setter
    def additional_pipeline_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingAlgorithm")
    def autoscaling_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_algorithm.setter
    def autoscaling_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_streaming_engine.setter
    def enable_streaming_engine(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_configuration.setter
    def ip_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launcherMachineType")
    def launcher_machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launcher_machine_type.setter
    def launcher_machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_workers.setter
    def num_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDelete")
    def on_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_delete.setter
    def on_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdkContainerImage")
    def sdk_container_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sdk_container_image.setter
    def sdk_container_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipWaitOnJobTermination")
    def skip_wait_on_job_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_wait_on_job_termination.setter
    def skip_wait_on_job_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingLocation")
    def staging_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @staging_location.setter
    def staging_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temp_location.setter
    def temp_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformNameMapping")
    def transform_name_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @transform_name_mapping.setter
    def transform_name_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _FlexTemplateJobState:
    def __init__(__self__, *, additional_experiments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., additional_pipeline_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autoscaling_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., container_spec_gcs_path: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ..., ip_configuration: Optional[pulumi.Input[_builtins.str]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launcher_machine_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_workers: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., num_workers: Optional[pulumi.Input[_builtins.int]] = ..., on_delete: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sdk_container_image: Optional[pulumi.Input[_builtins.str]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., skip_wait_on_job_termination: Optional[pulumi.Input[_builtins.bool]] = ..., staging_location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., temp_location: Optional[pulumi.Input[_builtins.str]] = ..., transform_name_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_experiments.setter
    def additional_experiments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalPipelineOptions")
    def additional_pipeline_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_pipeline_options.setter
    def additional_pipeline_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingAlgorithm")
    def autoscaling_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_algorithm.setter
    def autoscaling_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerSpecGcsPath")
    def container_spec_gcs_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_spec_gcs_path.setter
    def container_spec_gcs_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_streaming_engine.setter
    def enable_streaming_engine(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_configuration.setter
    def ip_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launcherMachineType")
    def launcher_machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launcher_machine_type.setter
    def launcher_machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_workers.setter
    def num_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDelete")
    def on_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_delete.setter
    def on_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdkContainerImage")
    def sdk_container_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sdk_container_image.setter
    def sdk_container_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipWaitOnJobTermination")
    def skip_wait_on_job_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_wait_on_job_termination.setter
    def skip_wait_on_job_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingLocation")
    def staging_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @staging_location.setter
    def staging_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temp_location.setter
    def temp_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformNameMapping")
    def transform_name_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @transform_name_mapping.setter
    def transform_name_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataflow/flexTemplateJob:FlexTemplateJob")
class FlexTemplateJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_experiments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., additional_pipeline_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autoscaling_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., container_spec_gcs_path: Optional[pulumi.Input[_builtins.str]] = ..., enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ..., ip_configuration: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launcher_machine_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_workers: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., num_workers: Optional[pulumi.Input[_builtins.int]] = ..., on_delete: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sdk_container_image: Optional[pulumi.Input[_builtins.str]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., skip_wait_on_job_termination: Optional[pulumi.Input[_builtins.bool]] = ..., staging_location: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., temp_location: Optional[pulumi.Input[_builtins.str]] = ..., transform_name_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FlexTemplateJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., additional_experiments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., additional_pipeline_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., autoscaling_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., container_spec_gcs_path: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_streaming_engine: Optional[pulumi.Input[_builtins.bool]] = ..., ip_configuration: Optional[pulumi.Input[_builtins.str]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launcher_machine_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_workers: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., num_workers: Optional[pulumi.Input[_builtins.int]] = ..., on_delete: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sdk_container_image: Optional[pulumi.Input[_builtins.str]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., skip_wait_on_job_termination: Optional[pulumi.Input[_builtins.bool]] = ..., staging_location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., temp_location: Optional[pulumi.Input[_builtins.str]] = ..., transform_name_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> FlexTemplateJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalExperiments")
    def additional_experiments(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalPipelineOptions")
    def additional_pipeline_options(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingAlgorithm")
    def autoscaling_algorithm(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerSpecGcsPath")
    def container_spec_gcs_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStreamingEngine")
    def enable_streaming_engine(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launcherMachineType")
    def launcher_machine_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numWorkers")
    def num_workers(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDelete")
    def on_delete(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdkContainerImage")
    def sdk_container_image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipWaitOnJobTermination")
    def skip_wait_on_job_termination(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingLocation")
    def staging_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tempLocation")
    def temp_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformNameMapping")
    def transform_name_mapping(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


