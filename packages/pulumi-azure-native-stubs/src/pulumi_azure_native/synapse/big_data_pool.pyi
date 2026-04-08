import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BigDataPoolArgs", "BigDataPool"]

@pulumi.input_type
class BigDataPoolArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        auto_pause: Optional[pulumi.Input[AutoPausePropertiesArgs]] = ...,
        auto_scale: Optional[pulumi.Input[AutoScalePropertiesArgs]] = ...,
        big_data_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_size: Optional[pulumi.Input[_builtins.int]] = ...,
        custom_libraries: Optional[
            pulumi.Input[Sequence[pulumi.Input[LibraryInfoArgs]]]
        ] = ...,
        default_spark_log_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_executor_allocation: Optional[
            pulumi.Input[DynamicExecutorAllocationArgs]
        ] = ...,
        force: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_autotune_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_compute_isolation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        library_requirements: Optional[pulumi.Input[LibraryRequirementsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_size: Optional[pulumi.Input[Union[_builtins.str, NodeSize]]] = ...,
        node_size_family: Optional[
            pulumi.Input[Union[_builtins.str, NodeSizeFamily]]
        ] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        session_level_packages_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        spark_config_properties: Optional[
            pulumi.Input[SparkConfigPropertiesArgs]
        ] = ...,
        spark_events_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[pulumi.Input[AutoPausePropertiesArgs]]: ...
    @auto_pause.setter
    def auto_pause(self, value: Optional[pulumi.Input[AutoPausePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[pulumi.Input[AutoScalePropertiesArgs]]: ...
    @auto_scale.setter
    def auto_scale(self, value: Optional[pulumi.Input[AutoScalePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="bigDataPoolName")
    def big_data_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @big_data_pool_name.setter
    def big_data_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_size.setter
    def cache_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LibraryInfoArgs]]]]: ...
    @custom_libraries.setter
    def custom_libraries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LibraryInfoArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_spark_log_folder.setter
    def default_spark_log_folder(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(
        self,
    ) -> Optional[pulumi.Input[DynamicExecutorAllocationArgs]]: ...
    @dynamic_executor_allocation.setter
    def dynamic_executor_allocation(
        self, value: Optional[pulumi.Input[DynamicExecutorAllocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force.setter
    def force(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isAutotuneEnabled")
    def is_autotune_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_autotune_enabled.setter
    def is_autotune_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_compute_isolation_enabled.setter
    def is_compute_isolation_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(
        self,
    ) -> Optional[pulumi.Input[LibraryRequirementsArgs]]: ...
    @library_requirements.setter
    def library_requirements(
        self, value: Optional[pulumi.Input[LibraryRequirementsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[pulumi.Input[Union[_builtins.str, NodeSize]]]: ...
    @node_size.setter
    def node_size(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NodeSize]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NodeSizeFamily]]]: ...
    @node_size_family.setter
    def node_size_family(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NodeSizeFamily]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @session_level_packages_enabled.setter
    def session_level_packages_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(
        self,
    ) -> Optional[pulumi.Input[SparkConfigPropertiesArgs]]: ...
    @spark_config_properties.setter
    def spark_config_properties(
        self, value: Optional[pulumi.Input[SparkConfigPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_events_folder.setter
    def spark_events_folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_version.setter
    def spark_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:synapse:BigDataPool")
class BigDataPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_pause: Optional[
            pulumi.Input[Union[AutoPausePropertiesArgs, AutoPausePropertiesArgsDict]]
        ] = ...,
        auto_scale: Optional[
            pulumi.Input[Union[AutoScalePropertiesArgs, AutoScalePropertiesArgsDict]]
        ] = ...,
        big_data_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_size: Optional[pulumi.Input[_builtins.int]] = ...,
        custom_libraries: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[LibraryInfoArgs, LibraryInfoArgsDict]]]
            ]
        ] = ...,
        default_spark_log_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_executor_allocation: Optional[
            pulumi.Input[
                Union[DynamicExecutorAllocationArgs, DynamicExecutorAllocationArgsDict]
            ]
        ] = ...,
        force: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_autotune_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_compute_isolation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        library_requirements: Optional[
            pulumi.Input[Union[LibraryRequirementsArgs, LibraryRequirementsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_size: Optional[pulumi.Input[Union[_builtins.str, NodeSize]]] = ...,
        node_size_family: Optional[
            pulumi.Input[Union[_builtins.str, NodeSizeFamily]]
        ] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_level_packages_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        spark_config_properties: Optional[
            pulumi.Input[
                Union[SparkConfigPropertiesArgs, SparkConfigPropertiesArgsDict]
            ]
        ] = ...,
        spark_events_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BigDataPoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BigDataPool: ...
    @_builtins.property
    @pulumi.getter(name="autoPause")
    def auto_pause(
        self,
    ) -> pulumi.Output[Optional[outputs.AutoPausePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="autoScale")
    def auto_scale(
        self,
    ) -> pulumi.Output[Optional[outputs.AutoScalePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.LibraryInfoResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(
        self,
    ) -> pulumi.Output[Optional[outputs.DynamicExecutorAllocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="isAutotuneEnabled")
    def is_autotune_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastSucceededTimestamp")
    def last_succeeded_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(
        self,
    ) -> pulumi.Output[Optional[outputs.LibraryRequirementsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.SparkConfigPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
