

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobArgs', 'Job']
@pulumi.input_type
class JobArgs:
    def __init__(__self__, *, placement: pulumi.Input[JobPlacementArgs], force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., hadoop_config: Optional[pulumi.Input[JobHadoopConfigArgs]] = ..., hive_config: Optional[pulumi.Input[JobHiveConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pig_config: Optional[pulumi.Input[JobPigConfigArgs]] = ..., presto_config: Optional[pulumi.Input[JobPrestoConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pyspark_config: Optional[pulumi.Input[JobPysparkConfigArgs]] = ..., reference: Optional[pulumi.Input[JobReferenceArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[JobSchedulingArgs]] = ..., spark_config: Optional[pulumi.Input[JobSparkConfigArgs]] = ..., sparksql_config: Optional[pulumi.Input[JobSparksqlConfigArgs]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Input[JobPlacementArgs]:
        
        ...
    
    @placement.setter
    def placement(self, value: pulumi.Input[JobPlacementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hadoopConfig")
    def hadoop_config(self) -> Optional[pulumi.Input[JobHadoopConfigArgs]]:
        
        ...
    
    @hadoop_config.setter
    def hadoop_config(self, value: Optional[pulumi.Input[JobHadoopConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveConfig")
    def hive_config(self) -> Optional[pulumi.Input[JobHiveConfigArgs]]:
        
        ...
    
    @hive_config.setter
    def hive_config(self, value: Optional[pulumi.Input[JobHiveConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pigConfig")
    def pig_config(self) -> Optional[pulumi.Input[JobPigConfigArgs]]:
        
        ...
    
    @pig_config.setter
    def pig_config(self, value: Optional[pulumi.Input[JobPigConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prestoConfig")
    def presto_config(self) -> Optional[pulumi.Input[JobPrestoConfigArgs]]:
        
        ...
    
    @presto_config.setter
    def presto_config(self, value: Optional[pulumi.Input[JobPrestoConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pysparkConfig")
    def pyspark_config(self) -> Optional[pulumi.Input[JobPysparkConfigArgs]]:
        
        ...
    
    @pyspark_config.setter
    def pyspark_config(self, value: Optional[pulumi.Input[JobPysparkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input[JobReferenceArgs]]:
        
        ...
    
    @reference.setter
    def reference(self, value: Optional[pulumi.Input[JobReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[pulumi.Input[JobSchedulingArgs]]:
        
        ...
    
    @scheduling.setter
    def scheduling(self, value: Optional[pulumi.Input[JobSchedulingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkConfig")
    def spark_config(self) -> Optional[pulumi.Input[JobSparkConfigArgs]]:
        
        ...
    
    @spark_config.setter
    def spark_config(self, value: Optional[pulumi.Input[JobSparkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparksqlConfig")
    def sparksql_config(self) -> Optional[pulumi.Input[JobSparksqlConfigArgs]]:
        
        ...
    
    @sparksql_config.setter
    def sparksql_config(self, value: Optional[pulumi.Input[JobSparksqlConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_completion.setter
    def wait_for_completion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _JobState:
    def __init__(__self__, *, driver_controls_files_uri: Optional[pulumi.Input[_builtins.str]] = ..., driver_output_resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., hadoop_config: Optional[pulumi.Input[JobHadoopConfigArgs]] = ..., hive_config: Optional[pulumi.Input[JobHiveConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pig_config: Optional[pulumi.Input[JobPigConfigArgs]] = ..., placement: Optional[pulumi.Input[JobPlacementArgs]] = ..., presto_config: Optional[pulumi.Input[JobPrestoConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pyspark_config: Optional[pulumi.Input[JobPysparkConfigArgs]] = ..., reference: Optional[pulumi.Input[JobReferenceArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[JobSchedulingArgs]] = ..., spark_config: Optional[pulumi.Input[JobSparkConfigArgs]] = ..., sparksql_config: Optional[pulumi.Input[JobSparksqlConfigArgs]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverControlsFilesUri")
    def driver_controls_files_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @driver_controls_files_uri.setter
    def driver_controls_files_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverOutputResourceUri")
    def driver_output_resource_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @driver_output_resource_uri.setter
    def driver_output_resource_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hadoopConfig")
    def hadoop_config(self) -> Optional[pulumi.Input[JobHadoopConfigArgs]]:
        
        ...
    
    @hadoop_config.setter
    def hadoop_config(self, value: Optional[pulumi.Input[JobHadoopConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveConfig")
    def hive_config(self) -> Optional[pulumi.Input[JobHiveConfigArgs]]:
        
        ...
    
    @hive_config.setter
    def hive_config(self, value: Optional[pulumi.Input[JobHiveConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pigConfig")
    def pig_config(self) -> Optional[pulumi.Input[JobPigConfigArgs]]:
        
        ...
    
    @pig_config.setter
    def pig_config(self, value: Optional[pulumi.Input[JobPigConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[JobPlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[JobPlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prestoConfig")
    def presto_config(self) -> Optional[pulumi.Input[JobPrestoConfigArgs]]:
        
        ...
    
    @presto_config.setter
    def presto_config(self, value: Optional[pulumi.Input[JobPrestoConfigArgs]]): # -> None:
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
    @pulumi.getter(name="pysparkConfig")
    def pyspark_config(self) -> Optional[pulumi.Input[JobPysparkConfigArgs]]:
        
        ...
    
    @pyspark_config.setter
    def pyspark_config(self, value: Optional[pulumi.Input[JobPysparkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input[JobReferenceArgs]]:
        
        ...
    
    @reference.setter
    def reference(self, value: Optional[pulumi.Input[JobReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[pulumi.Input[JobSchedulingArgs]]:
        
        ...
    
    @scheduling.setter
    def scheduling(self, value: Optional[pulumi.Input[JobSchedulingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkConfig")
    def spark_config(self) -> Optional[pulumi.Input[JobSparkConfigArgs]]:
        
        ...
    
    @spark_config.setter
    def spark_config(self, value: Optional[pulumi.Input[JobSparkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparksqlConfig")
    def sparksql_config(self) -> Optional[pulumi.Input[JobSparksqlConfigArgs]]:
        
        ...
    
    @sparksql_config.setter
    def sparksql_config(self, value: Optional[pulumi.Input[JobSparksqlConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_completion.setter
    def wait_for_completion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataproc/job:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., hadoop_config: Optional[pulumi.Input[Union[JobHadoopConfigArgs, JobHadoopConfigArgsDict]]] = ..., hive_config: Optional[pulumi.Input[Union[JobHiveConfigArgs, JobHiveConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pig_config: Optional[pulumi.Input[Union[JobPigConfigArgs, JobPigConfigArgsDict]]] = ..., placement: Optional[pulumi.Input[Union[JobPlacementArgs, JobPlacementArgsDict]]] = ..., presto_config: Optional[pulumi.Input[Union[JobPrestoConfigArgs, JobPrestoConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pyspark_config: Optional[pulumi.Input[Union[JobPysparkConfigArgs, JobPysparkConfigArgsDict]]] = ..., reference: Optional[pulumi.Input[Union[JobReferenceArgs, JobReferenceArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[Union[JobSchedulingArgs, JobSchedulingArgsDict]]] = ..., spark_config: Optional[pulumi.Input[Union[JobSparkConfigArgs, JobSparkConfigArgsDict]]] = ..., sparksql_config: Optional[pulumi.Input[Union[JobSparksqlConfigArgs, JobSparksqlConfigArgsDict]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., driver_controls_files_uri: Optional[pulumi.Input[_builtins.str]] = ..., driver_output_resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., hadoop_config: Optional[pulumi.Input[Union[JobHadoopConfigArgs, JobHadoopConfigArgsDict]]] = ..., hive_config: Optional[pulumi.Input[Union[JobHiveConfigArgs, JobHiveConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pig_config: Optional[pulumi.Input[Union[JobPigConfigArgs, JobPigConfigArgsDict]]] = ..., placement: Optional[pulumi.Input[Union[JobPlacementArgs, JobPlacementArgsDict]]] = ..., presto_config: Optional[pulumi.Input[Union[JobPrestoConfigArgs, JobPrestoConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pyspark_config: Optional[pulumi.Input[Union[JobPysparkConfigArgs, JobPysparkConfigArgsDict]]] = ..., reference: Optional[pulumi.Input[Union[JobReferenceArgs, JobReferenceArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[Union[JobSchedulingArgs, JobSchedulingArgsDict]]] = ..., spark_config: Optional[pulumi.Input[Union[JobSparkConfigArgs, JobSparkConfigArgsDict]]] = ..., sparksql_config: Optional[pulumi.Input[Union[JobSparksqlConfigArgs, JobSparksqlConfigArgsDict]]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JobStatusArgs, JobStatusArgsDict]]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ...) -> Job:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverControlsFilesUri")
    def driver_controls_files_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverOutputResourceUri")
    def driver_output_resource_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hadoopConfig")
    def hadoop_config(self) -> pulumi.Output[Optional[outputs.JobHadoopConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveConfig")
    def hive_config(self) -> pulumi.Output[Optional[outputs.JobHiveConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pigConfig")
    def pig_config(self) -> pulumi.Output[Optional[outputs.JobPigConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Output[outputs.JobPlacement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prestoConfig")
    def presto_config(self) -> pulumi.Output[Optional[outputs.JobPrestoConfig]]:
        
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
    @pulumi.getter(name="pysparkConfig")
    def pyspark_config(self) -> pulumi.Output[Optional[outputs.JobPysparkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> pulumi.Output[outputs.JobReference]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> pulumi.Output[Optional[outputs.JobScheduling]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkConfig")
    def spark_config(self) -> pulumi.Output[Optional[outputs.JobSparkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparksqlConfig")
    def sparksql_config(self) -> pulumi.Output[Optional[outputs.JobSparksqlConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.JobStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


