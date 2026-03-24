import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KxClusterArgs", "KxCluster"]

@pulumi.input_type
class KxClusterArgs:
    def __init__(
        __self__,
        *,
        az_mode: pulumi.Input[_builtins.str],
        environment_id: pulumi.Input[_builtins.str],
        release_label: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        vpc_configuration: pulumi.Input[KxClusterVpcConfigurationArgs],
        auto_scaling_configuration: Optional[
            pulumi.Input[KxClusterAutoScalingConfigurationArgs]
        ] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_storage_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
        ] = ...,
        capacity_configuration: Optional[
            pulumi.Input[KxClusterCapacityConfigurationArgs]
        ] = ...,
        code: Optional[pulumi.Input[KxClusterCodeArgs]] = ...,
        command_line_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        databases: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        initialization_script: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        savedown_storage_configuration: Optional[
            pulumi.Input[KxClusterSavedownStorageConfigurationArgs]
        ] = ...,
        scaling_group_configuration: Optional[
            pulumi.Input[KxClusterScalingGroupConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tickerplant_log_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> pulumi.Input[_builtins.str]: ...
    @az_mode.setter
    def az_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[_builtins.str]: ...
    @environment_id.setter
    def environment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Input[_builtins.str]: ...
    @release_label.setter
    def release_label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Input[KxClusterVpcConfigurationArgs]: ...
    @vpc_configuration.setter
    def vpc_configuration(self, value: pulumi.Input[KxClusterVpcConfigurationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfiguration")
    def auto_scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterAutoScalingConfigurationArgs]]: ...
    @auto_scaling_configuration.setter
    def auto_scaling_configuration(
        self, value: Optional[pulumi.Input[KxClusterAutoScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheStorageConfigurations")
    def cache_storage_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
    ]: ...
    @cache_storage_configurations.setter
    def cache_storage_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityConfiguration")
    def capacity_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterCapacityConfigurationArgs]]: ...
    @capacity_configuration.setter
    def capacity_configuration(
        self, value: Optional[pulumi.Input[KxClusterCapacityConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[KxClusterCodeArgs]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[KxClusterCodeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @command_line_arguments.setter
    def command_line_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]]: ...
    @databases.setter
    def databases(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initializationScript")
    def initialization_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initialization_script.setter
    def initialization_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="savedownStorageConfiguration")
    def savedown_storage_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterSavedownStorageConfigurationArgs]]: ...
    @savedown_storage_configuration.setter
    def savedown_storage_configuration(
        self, value: Optional[pulumi.Input[KxClusterSavedownStorageConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingGroupConfiguration")
    def scaling_group_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterScalingGroupConfigurationArgs]]: ...
    @scaling_group_configuration.setter
    def scaling_group_configuration(
        self, value: Optional[pulumi.Input[KxClusterScalingGroupConfigurationArgs]]
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
    @_builtins.property
    @pulumi.getter(name="tickerplantLogConfigurations")
    def tickerplant_log_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]]
    ]: ...
    @tickerplant_log_configurations.setter
    def tickerplant_log_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]
            ]
        ],
    ): ...

@pulumi.input_type
class _KxClusterState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_configuration: Optional[
            pulumi.Input[KxClusterAutoScalingConfigurationArgs]
        ] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_storage_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
        ] = ...,
        capacity_configuration: Optional[
            pulumi.Input[KxClusterCapacityConfigurationArgs]
        ] = ...,
        code: Optional[pulumi.Input[KxClusterCodeArgs]] = ...,
        command_line_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        created_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        databases: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        initialization_script: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        savedown_storage_configuration: Optional[
            pulumi.Input[KxClusterSavedownStorageConfigurationArgs]
        ] = ...,
        scaling_group_configuration: Optional[
            pulumi.Input[KxClusterScalingGroupConfigurationArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tickerplant_log_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_configuration: Optional[pulumi.Input[KxClusterVpcConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfiguration")
    def auto_scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterAutoScalingConfigurationArgs]]: ...
    @auto_scaling_configuration.setter
    def auto_scaling_configuration(
        self, value: Optional[pulumi.Input[KxClusterAutoScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @az_mode.setter
    def az_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheStorageConfigurations")
    def cache_storage_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
    ]: ...
    @cache_storage_configurations.setter
    def cache_storage_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KxClusterCacheStorageConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityConfiguration")
    def capacity_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterCapacityConfigurationArgs]]: ...
    @capacity_configuration.setter
    def capacity_configuration(
        self, value: Optional[pulumi.Input[KxClusterCapacityConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[KxClusterCodeArgs]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[KxClusterCodeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @command_line_arguments.setter
    def command_line_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_timestamp.setter
    def created_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]]: ...
    @databases.setter
    def databases(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[KxClusterDatabaseArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initializationScript")
    def initialization_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initialization_script.setter
    def initialization_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimestamp")
    def last_modified_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_timestamp.setter
    def last_modified_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_label.setter
    def release_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="savedownStorageConfiguration")
    def savedown_storage_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterSavedownStorageConfigurationArgs]]: ...
    @savedown_storage_configuration.setter
    def savedown_storage_configuration(
        self, value: Optional[pulumi.Input[KxClusterSavedownStorageConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingGroupConfiguration")
    def scaling_group_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterScalingGroupConfigurationArgs]]: ...
    @scaling_group_configuration.setter
    def scaling_group_configuration(
        self, value: Optional[pulumi.Input[KxClusterScalingGroupConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tickerplantLogConfigurations")
    def tickerplant_log_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]]
    ]: ...
    @tickerplant_log_configurations.setter
    def tickerplant_log_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxClusterTickerplantLogConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[pulumi.Input[KxClusterVpcConfigurationArgs]]: ...
    @vpc_configuration.setter
    def vpc_configuration(
        self, value: Optional[pulumi.Input[KxClusterVpcConfigurationArgs]]
    ): ...

@pulumi.type_token("aws:finspace/kxCluster:KxCluster")
class KxCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterAutoScalingConfigurationArgs,
                    KxClusterAutoScalingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_storage_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxClusterCacheStorageConfigurationArgs,
                            KxClusterCacheStorageConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        capacity_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterCapacityConfigurationArgs,
                    KxClusterCapacityConfigurationArgsDict,
                ]
            ]
        ] = ...,
        code: Optional[
            pulumi.Input[Union[KxClusterCodeArgs, KxClusterCodeArgsDict]]
        ] = ...,
        command_line_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        databases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[KxClusterDatabaseArgs, KxClusterDatabaseArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        initialization_script: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        savedown_storage_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterSavedownStorageConfigurationArgs,
                    KxClusterSavedownStorageConfigurationArgsDict,
                ]
            ]
        ] = ...,
        scaling_group_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterScalingGroupConfigurationArgs,
                    KxClusterScalingGroupConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tickerplant_log_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxClusterTickerplantLogConfigurationArgs,
                            KxClusterTickerplantLogConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[KxClusterVpcConfigurationArgs, KxClusterVpcConfigurationArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KxClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterAutoScalingConfigurationArgs,
                    KxClusterAutoScalingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_storage_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxClusterCacheStorageConfigurationArgs,
                            KxClusterCacheStorageConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        capacity_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterCapacityConfigurationArgs,
                    KxClusterCapacityConfigurationArgsDict,
                ]
            ]
        ] = ...,
        code: Optional[
            pulumi.Input[Union[KxClusterCodeArgs, KxClusterCodeArgsDict]]
        ] = ...,
        command_line_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        created_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        databases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[KxClusterDatabaseArgs, KxClusterDatabaseArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        initialization_script: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        savedown_storage_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterSavedownStorageConfigurationArgs,
                    KxClusterSavedownStorageConfigurationArgsDict,
                ]
            ]
        ] = ...,
        scaling_group_configuration: Optional[
            pulumi.Input[
                Union[
                    KxClusterScalingGroupConfigurationArgs,
                    KxClusterScalingGroupConfigurationArgsDict,
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tickerplant_log_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxClusterTickerplantLogConfigurationArgs,
                            KxClusterTickerplantLogConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[KxClusterVpcConfigurationArgs, KxClusterVpcConfigurationArgsDict]
            ]
        ] = ...,
    ) -> KxCluster: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfiguration")
    def auto_scaling_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KxClusterAutoScalingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheStorageConfigurations")
    def cache_storage_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.KxClusterCacheStorageConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="capacityConfiguration")
    def capacity_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KxClusterCapacityConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[outputs.KxClusterCode]]: ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.KxClusterDatabase]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="initializationScript")
    def initialization_script(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimestamp")
    def last_modified_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="savedownStorageConfiguration")
    def savedown_storage_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KxClusterSavedownStorageConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="scalingGroupConfiguration")
    def scaling_group_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KxClusterScalingGroupConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tickerplantLogConfigurations")
    def tickerplant_log_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.KxClusterTickerplantLogConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[outputs.KxClusterVpcConfiguration]: ...
