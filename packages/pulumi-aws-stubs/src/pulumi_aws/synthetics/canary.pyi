

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
__all__ = ['CanaryArgs', 'Canary']
@pulumi.input_type
class CanaryArgs:
    def __init__(__self__, *, artifact_s3_location: pulumi.Input[_builtins.str], execution_role_arn: pulumi.Input[_builtins.str], handler: pulumi.Input[_builtins.str], runtime_version: pulumi.Input[_builtins.str], schedule: pulumi.Input[CanaryScheduleArgs], artifact_config: Optional[pulumi.Input[CanaryArtifactConfigArgs]] = ..., delete_lambda: Optional[pulumi.Input[_builtins.bool]] = ..., failure_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., run_config: Optional[pulumi.Input[CanaryRunConfigArgs]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_version: Optional[pulumi.Input[_builtins.str]] = ..., start_canary: Optional[pulumi.Input[_builtins.bool]] = ..., success_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[CanaryVpcConfigArgs]] = ..., zip_file: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactS3Location")
    def artifact_s3_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @artifact_s3_location.setter
    def artifact_s3_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @handler.setter
    def handler(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[CanaryScheduleArgs]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: pulumi.Input[CanaryScheduleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactConfig")
    def artifact_config(self) -> Optional[pulumi.Input[CanaryArtifactConfigArgs]]:
        
        ...
    
    @artifact_config.setter
    def artifact_config(self, value: Optional[pulumi.Input[CanaryArtifactConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteLambda")
    def delete_lambda(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_lambda.setter
    def delete_lambda(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureRetentionPeriod")
    def failure_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_retention_period.setter
    def failure_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runConfig")
    def run_config(self) -> Optional[pulumi.Input[CanaryRunConfigArgs]]:
        
        ...
    
    @run_config.setter
    def run_config(self, value: Optional[pulumi.Input[CanaryRunConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key.setter
    def s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Version")
    def s3_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_version.setter
    def s3_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCanary")
    def start_canary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_canary.setter
    def start_canary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successRetentionPeriod")
    def success_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @success_retention_period.setter
    def success_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[CanaryVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[CanaryVpcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CanaryState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_config: Optional[pulumi.Input[CanaryArtifactConfigArgs]] = ..., artifact_s3_location: Optional[pulumi.Input[_builtins.str]] = ..., delete_lambda: Optional[pulumi.Input[_builtins.bool]] = ..., engine_arn: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., failure_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., run_config: Optional[pulumi.Input[CanaryRunConfigArgs]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_version: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[CanaryScheduleArgs]] = ..., source_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., start_canary: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., success_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timelines: Optional[pulumi.Input[Sequence[pulumi.Input[CanaryTimelineArgs]]]] = ..., vpc_config: Optional[pulumi.Input[CanaryVpcConfigArgs]] = ..., zip_file: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactConfig")
    def artifact_config(self) -> Optional[pulumi.Input[CanaryArtifactConfigArgs]]:
        
        ...
    
    @artifact_config.setter
    def artifact_config(self, value: Optional[pulumi.Input[CanaryArtifactConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactS3Location")
    def artifact_s3_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @artifact_s3_location.setter
    def artifact_s3_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteLambda")
    def delete_lambda(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_lambda.setter
    def delete_lambda(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineArn")
    def engine_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_arn.setter
    def engine_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureRetentionPeriod")
    def failure_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_retention_period.setter
    def failure_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @handler.setter
    def handler(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runConfig")
    def run_config(self) -> Optional[pulumi.Input[CanaryRunConfigArgs]]:
        
        ...
    
    @run_config.setter
    def run_config(self, value: Optional[pulumi.Input[CanaryRunConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key.setter
    def s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Version")
    def s3_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_version.setter
    def s3_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[CanaryScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[CanaryScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_location_arn.setter
    def source_location_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCanary")
    def start_canary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_canary.setter
    def start_canary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successRetentionPeriod")
    def success_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @success_retention_period.setter
    def success_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timelines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CanaryTimelineArgs]]]]:
        
        ...
    
    @timelines.setter
    def timelines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CanaryTimelineArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[CanaryVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[CanaryVpcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:synthetics/canary:Canary")
class Canary(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., artifact_config: Optional[pulumi.Input[Union[CanaryArtifactConfigArgs, CanaryArtifactConfigArgsDict]]] = ..., artifact_s3_location: Optional[pulumi.Input[_builtins.str]] = ..., delete_lambda: Optional[pulumi.Input[_builtins.bool]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., failure_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., run_config: Optional[pulumi.Input[Union[CanaryRunConfigArgs, CanaryRunConfigArgsDict]]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_version: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[CanaryScheduleArgs, CanaryScheduleArgsDict]]] = ..., start_canary: Optional[pulumi.Input[_builtins.bool]] = ..., success_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[CanaryVpcConfigArgs, CanaryVpcConfigArgsDict]]] = ..., zip_file: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CanaryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_config: Optional[pulumi.Input[Union[CanaryArtifactConfigArgs, CanaryArtifactConfigArgsDict]]] = ..., artifact_s3_location: Optional[pulumi.Input[_builtins.str]] = ..., delete_lambda: Optional[pulumi.Input[_builtins.bool]] = ..., engine_arn: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., failure_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., run_config: Optional[pulumi.Input[Union[CanaryRunConfigArgs, CanaryRunConfigArgsDict]]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_version: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[CanaryScheduleArgs, CanaryScheduleArgsDict]]] = ..., source_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., start_canary: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., success_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timelines: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CanaryTimelineArgs, CanaryTimelineArgsDict]]]]] = ..., vpc_config: Optional[pulumi.Input[Union[CanaryVpcConfigArgs, CanaryVpcConfigArgsDict]]] = ..., zip_file: Optional[pulumi.Input[_builtins.str]] = ...) -> Canary:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactConfig")
    def artifact_config(self) -> pulumi.Output[Optional[outputs.CanaryArtifactConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactS3Location")
    def artifact_s3_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteLambda")
    def delete_lambda(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineArn")
    def engine_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureRetentionPeriod")
    def failure_retention_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runConfig")
    def run_config(self) -> pulumi.Output[outputs.CanaryRunConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Version")
    def s3_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[outputs.CanarySchedule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCanary")
    def start_canary(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successRetentionPeriod")
    def success_retention_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timelines(self) -> pulumi.Output[Sequence[outputs.CanaryTimeline]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.CanaryVpcConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


