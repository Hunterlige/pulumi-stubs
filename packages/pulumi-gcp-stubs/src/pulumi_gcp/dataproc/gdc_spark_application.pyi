import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GdcSparkApplicationArgs", "GdcSparkApplication"]

@pulumi.input_type
class GdcSparkApplicationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        serviceinstance: pulumi.Input[_builtins.str],
        spark_application_id: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        application_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        dependency_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_application_config: Optional[
            pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]
        ] = ...,
        spark_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]
        ] = ...,
        spark_r_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]
        ] = ...,
        spark_sql_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def serviceinstance(self) -> pulumi.Input[_builtins.str]: ...
    @serviceinstance.setter
    def serviceinstance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationId")
    def spark_application_id(self) -> pulumi.Input[_builtins.str]: ...
    @spark_application_id.setter
    def spark_application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationEnvironment")
    def application_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_environment.setter
    def application_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dependencyImages")
    def dependency_images(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dependency_images.setter
    def dependency_images(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pysparkApplicationConfig")
    def pyspark_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]]: ...
    @pyspark_application_config.setter
    def pyspark_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationConfig")
    def spark_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]]: ...
    @spark_application_config.setter
    def spark_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkRApplicationConfig")
    def spark_r_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]]: ...
    @spark_r_application_config.setter
    def spark_r_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlApplicationConfig")
    def spark_sql_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]]: ...
    @spark_sql_application_config.setter
    def spark_sql_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GdcSparkApplicationState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        application_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dependency_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_application_config: Optional[
            pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        serviceinstance: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]
        ] = ...,
        spark_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_r_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]
        ] = ...,
        spark_sql_application_config: Optional[
            pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_message: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationEnvironment")
    def application_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_environment.setter
    def application_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dependencyImages")
    def dependency_images(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dependency_images.setter
    def dependency_images(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringEndpoint")
    def monitoring_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_endpoint.setter
    def monitoring_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_uri.setter
    def output_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pysparkApplicationConfig")
    def pyspark_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]]: ...
    @pyspark_application_config.setter
    def pyspark_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationPysparkApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def serviceinstance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serviceinstance.setter
    def serviceinstance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationConfig")
    def spark_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]]: ...
    @spark_application_config.setter
    def spark_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationId")
    def spark_application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_application_id.setter
    def spark_application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkRApplicationConfig")
    def spark_r_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]]: ...
    @spark_r_application_config.setter
    def spark_r_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkRApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlApplicationConfig")
    def spark_sql_application_config(
        self,
    ) -> Optional[pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]]: ...
    @spark_sql_application_config.setter
    def spark_sql_application_config(
        self,
        value: Optional[pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class GdcSparkApplication(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        application_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        dependency_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationPysparkApplicationConfigArgs,
                    GdcSparkApplicationPysparkApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        serviceinstance: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkApplicationConfigArgs,
                    GdcSparkApplicationSparkApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_r_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkRApplicationConfigArgs,
                    GdcSparkApplicationSparkRApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_sql_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkSqlApplicationConfigArgs,
                    GdcSparkApplicationSparkSqlApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GdcSparkApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        application_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dependency_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationPysparkApplicationConfigArgs,
                    GdcSparkApplicationPysparkApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        serviceinstance: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkApplicationConfigArgs,
                    GdcSparkApplicationSparkApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_r_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkRApplicationConfigArgs,
                    GdcSparkApplicationSparkRApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_sql_application_config: Optional[
            pulumi.Input[
                Union[
                    GdcSparkApplicationSparkSqlApplicationConfigArgs,
                    GdcSparkApplicationSparkSqlApplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_message: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GdcSparkApplication: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnvironment")
    def application_environment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dependencyImages")
    def dependency_images(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringEndpoint")
    def monitoring_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pysparkApplicationConfig")
    def pyspark_application_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.GdcSparkApplicationPysparkApplicationConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def serviceinstance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationConfig")
    def spark_application_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GdcSparkApplicationSparkApplicationConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkApplicationId")
    def spark_application_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sparkRApplicationConfig")
    def spark_r_application_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.GdcSparkApplicationSparkRApplicationConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlApplicationConfig")
    def spark_sql_application_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.GdcSparkApplicationSparkSqlApplicationConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
