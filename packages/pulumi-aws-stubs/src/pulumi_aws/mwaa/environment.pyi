import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentArgs", "Environment"]

@pulumi.input_type
class EnvironmentArgs:
    def __init__(
        __self__,
        *,
        dag_s3_path: pulumi.Input[_builtins.str],
        execution_role_arn: pulumi.Input[_builtins.str],
        network_configuration: pulumi.Input[EnvironmentNetworkConfigurationArgs],
        source_bucket_arn: pulumi.Input[_builtins.str],
        airflow_configuration_options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        airflow_version: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_management: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_class: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[EnvironmentLoggingConfigurationArgs]
        ] = ...,
        max_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        plugins_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        plugins_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        schedulers: Optional[pulumi.Input[_builtins.int]] = ...,
        startup_script_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        webserver_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dagS3Path")
    def dag_s3_path(self) -> pulumi.Input[_builtins.str]: ...
    @dag_s3_path.setter
    def dag_s3_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Input[EnvironmentNetworkConfigurationArgs]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: pulumi.Input[EnvironmentNetworkConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceBucketArn")
    def source_bucket_arn(self) -> pulumi.Input[_builtins.str]: ...
    @source_bucket_arn.setter
    def source_bucket_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="airflowConfigurationOptions")
    def airflow_configuration_options(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @airflow_configuration_options.setter
    def airflow_configuration_options(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="airflowVersion")
    def airflow_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @airflow_version.setter
    def airflow_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointManagement")
    def endpoint_management(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_management.setter
    def endpoint_management(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentClass")
    def environment_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_class.setter
    def environment_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxWebservers")
    def max_webservers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_webservers.setter
    def max_webservers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minWebservers")
    def min_webservers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_webservers.setter
    def min_webservers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minWorkers")
    def min_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_workers.setter
    def min_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugins_s3_object_version.setter
    def plugins_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3Path")
    def plugins_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugins_s3_path.setter
    def plugins_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_s3_object_version.setter
    def requirements_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3Path")
    def requirements_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_s3_path.setter
    def requirements_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedulers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schedulers.setter
    def schedulers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script_s3_object_version.setter
    def startup_script_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3Path")
    def startup_script_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script_s3_path.setter
    def startup_script_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="webserverAccessMode")
    def webserver_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webserver_access_mode.setter
    def webserver_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workerReplacementStrategy")
    def worker_replacement_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_replacement_strategy.setter
    def worker_replacement_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _EnvironmentState:
    def __init__(
        __self__,
        *,
        airflow_configuration_options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        airflow_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        dag_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        database_vpc_endpoint_service: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_management: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updateds: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedArgs]]]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[EnvironmentLoggingConfigurationArgs]
        ] = ...,
        max_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[EnvironmentNetworkConfigurationArgs]
        ] = ...,
        plugins_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        plugins_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        schedulers: Optional[pulumi.Input[_builtins.int]] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        webserver_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        webserver_url: Optional[pulumi.Input[_builtins.str]] = ...,
        webserver_vpc_endpoint_service: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="airflowConfigurationOptions")
    def airflow_configuration_options(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @airflow_configuration_options.setter
    def airflow_configuration_options(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="airflowVersion")
    def airflow_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @airflow_version.setter
    def airflow_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dagS3Path")
    def dag_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dag_s3_path.setter
    def dag_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseVpcEndpointService")
    def database_vpc_endpoint_service(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_vpc_endpoint_service.setter
    def database_vpc_endpoint_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointManagement")
    def endpoint_management(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_management.setter
    def endpoint_management(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentClass")
    def environment_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_class.setter
    def environment_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateds")
    def last_updateds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedArgs]]]]: ...
    @last_updateds.setter
    def last_updateds(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxWebservers")
    def max_webservers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_webservers.setter
    def max_webservers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minWebservers")
    def min_webservers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_webservers.setter
    def min_webservers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minWorkers")
    def min_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_workers.setter
    def min_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[EnvironmentNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[EnvironmentNetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugins_s3_object_version.setter
    def plugins_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3Path")
    def plugins_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugins_s3_path.setter
    def plugins_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_s3_object_version.setter
    def requirements_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3Path")
    def requirements_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_s3_path.setter
    def requirements_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedulers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schedulers.setter
    def schedulers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceBucketArn")
    def source_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_bucket_arn.setter
    def source_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script_s3_object_version.setter
    def startup_script_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3Path")
    def startup_script_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script_s3_path.setter
    def startup_script_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webserverAccessMode")
    def webserver_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webserver_access_mode.setter
    def webserver_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webserverUrl")
    def webserver_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webserver_url.setter
    def webserver_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webserverVpcEndpointService")
    def webserver_vpc_endpoint_service(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webserver_vpc_endpoint_service.setter
    def webserver_vpc_endpoint_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workerReplacementStrategy")
    def worker_replacement_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_replacement_strategy.setter
    def worker_replacement_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:mwaa/environment:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        airflow_configuration_options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        airflow_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dag_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_management: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    EnvironmentLoggingConfigurationArgs,
                    EnvironmentLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        max_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    EnvironmentNetworkConfigurationArgs,
                    EnvironmentNetworkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        plugins_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        plugins_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        schedulers: Optional[pulumi.Input[_builtins.int]] = ...,
        source_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        webserver_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        airflow_configuration_options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        airflow_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        dag_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        database_vpc_endpoint_service: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_management: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updateds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EnvironmentLastUpdatedArgs, EnvironmentLastUpdatedArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    EnvironmentLoggingConfigurationArgs,
                    EnvironmentLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        max_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        max_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_webservers: Optional[pulumi.Input[_builtins.int]] = ...,
        min_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    EnvironmentNetworkConfigurationArgs,
                    EnvironmentNetworkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        plugins_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        plugins_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        schedulers: Optional[pulumi.Input[_builtins.int]] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_script_s3_path: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        webserver_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        webserver_url: Optional[pulumi.Input[_builtins.str]] = ...,
        webserver_vpc_endpoint_service: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_window_start: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Environment: ...
    @_builtins.property
    @pulumi.getter(name="airflowConfigurationOptions")
    def airflow_configuration_options(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="airflowVersion")
    def airflow_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dagS3Path")
    def dag_s3_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseVpcEndpointService")
    def database_vpc_endpoint_service(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointManagement")
    def endpoint_management(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="environmentClass")
    def environment_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateds")
    def last_updateds(
        self,
    ) -> pulumi.Output[Sequence[outputs.EnvironmentLastUpdated]]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Output[outputs.EnvironmentLoggingConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="maxWebservers")
    def max_webservers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minWebservers")
    def min_webservers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minWorkers")
    def min_workers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Output[outputs.EnvironmentNetworkConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pluginsS3Path")
    def plugins_s3_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirementsS3Path")
    def requirements_s3_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def schedulers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceBucketArn")
    def source_bucket_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startupScriptS3Path")
    def startup_script_s3_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="webserverAccessMode")
    def webserver_access_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webserverUrl")
    def webserver_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webserverVpcEndpointService")
    def webserver_vpc_endpoint_service(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerReplacementStrategy")
    def worker_replacement_strategy(self) -> pulumi.Output[_builtins.str]: ...
