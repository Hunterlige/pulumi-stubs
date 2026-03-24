import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        release_label: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_start_configuration: Optional[
            pulumi.Input[ApplicationAutoStartConfigurationArgs]
        ] = ...,
        auto_stop_configuration: Optional[
            pulumi.Input[ApplicationAutoStopConfigurationArgs]
        ] = ...,
        image_configuration: Optional[
            pulumi.Input[ApplicationImageConfigurationArgs]
        ] = ...,
        initial_capacities: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
        ] = ...,
        interactive_configuration: Optional[
            pulumi.Input[ApplicationInteractiveConfigurationArgs]
        ] = ...,
        job_level_cost_allocation_configuration: Optional[
            pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]
        ] = ...,
        maximum_capacity: Optional[pulumi.Input[ApplicationMaximumCapacityArgs]] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[ApplicationMonitoringConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[ApplicationNetworkConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
        ] = ...,
        scheduler_configuration: Optional[
            pulumi.Input[ApplicationSchedulerConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
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
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationAutoStartConfigurationArgs]]: ...
    @auto_start_configuration.setter
    def auto_start_configuration(
        self, value: Optional[pulumi.Input[ApplicationAutoStartConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationAutoStopConfigurationArgs]]: ...
    @auto_stop_configuration.setter
    def auto_stop_configuration(
        self, value: Optional[pulumi.Input[ApplicationAutoStopConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationImageConfigurationArgs]]: ...
    @image_configuration.setter
    def image_configuration(
        self, value: Optional[pulumi.Input[ApplicationImageConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialCapacities")
    def initial_capacities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
    ]: ...
    @initial_capacities.setter
    def initial_capacities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="interactiveConfiguration")
    def interactive_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationInteractiveConfigurationArgs]]: ...
    @interactive_configuration.setter
    def interactive_configuration(
        self, value: Optional[pulumi.Input[ApplicationInteractiveConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobLevelCostAllocationConfiguration")
    def job_level_cost_allocation_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]]: ...
    @job_level_cost_allocation_configuration.setter
    def job_level_cost_allocation_configuration(
        self,
        value: Optional[
            pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(
        self,
    ) -> Optional[pulumi.Input[ApplicationMaximumCapacityArgs]]: ...
    @maximum_capacity.setter
    def maximum_capacity(
        self, value: Optional[pulumi.Input[ApplicationMaximumCapacityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationMonitoringConfigurationArgs]]: ...
    @monitoring_configuration.setter
    def monitoring_configuration(
        self, value: Optional[pulumi.Input[ApplicationMonitoringConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[ApplicationNetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfigurations")
    def runtime_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
    ]: ...
    @runtime_configurations.setter
    def runtime_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulerConfiguration")
    def scheduler_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationSchedulerConfigurationArgs]]: ...
    @scheduler_configuration.setter
    def scheduler_configuration(
        self, value: Optional[pulumi.Input[ApplicationSchedulerConfigurationArgs]]
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

@pulumi.input_type
class _ApplicationState:
    def __init__(
        __self__,
        *,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_start_configuration: Optional[
            pulumi.Input[ApplicationAutoStartConfigurationArgs]
        ] = ...,
        auto_stop_configuration: Optional[
            pulumi.Input[ApplicationAutoStopConfigurationArgs]
        ] = ...,
        image_configuration: Optional[
            pulumi.Input[ApplicationImageConfigurationArgs]
        ] = ...,
        initial_capacities: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
        ] = ...,
        interactive_configuration: Optional[
            pulumi.Input[ApplicationInteractiveConfigurationArgs]
        ] = ...,
        job_level_cost_allocation_configuration: Optional[
            pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]
        ] = ...,
        maximum_capacity: Optional[pulumi.Input[ApplicationMaximumCapacityArgs]] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[ApplicationMonitoringConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[ApplicationNetworkConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
        ] = ...,
        scheduler_configuration: Optional[
            pulumi.Input[ApplicationSchedulerConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationAutoStartConfigurationArgs]]: ...
    @auto_start_configuration.setter
    def auto_start_configuration(
        self, value: Optional[pulumi.Input[ApplicationAutoStartConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationAutoStopConfigurationArgs]]: ...
    @auto_stop_configuration.setter
    def auto_stop_configuration(
        self, value: Optional[pulumi.Input[ApplicationAutoStopConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationImageConfigurationArgs]]: ...
    @image_configuration.setter
    def image_configuration(
        self, value: Optional[pulumi.Input[ApplicationImageConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialCapacities")
    def initial_capacities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
    ]: ...
    @initial_capacities.setter
    def initial_capacities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationInitialCapacityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="interactiveConfiguration")
    def interactive_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationInteractiveConfigurationArgs]]: ...
    @interactive_configuration.setter
    def interactive_configuration(
        self, value: Optional[pulumi.Input[ApplicationInteractiveConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobLevelCostAllocationConfiguration")
    def job_level_cost_allocation_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]]: ...
    @job_level_cost_allocation_configuration.setter
    def job_level_cost_allocation_configuration(
        self,
        value: Optional[
            pulumi.Input[ApplicationJobLevelCostAllocationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(
        self,
    ) -> Optional[pulumi.Input[ApplicationMaximumCapacityArgs]]: ...
    @maximum_capacity.setter
    def maximum_capacity(
        self, value: Optional[pulumi.Input[ApplicationMaximumCapacityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationMonitoringConfigurationArgs]]: ...
    @monitoring_configuration.setter
    def monitoring_configuration(
        self, value: Optional[pulumi.Input[ApplicationMonitoringConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[ApplicationNetworkConfigurationArgs]]
    ): ...
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
    @pulumi.getter(name="runtimeConfigurations")
    def runtime_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
    ]: ...
    @runtime_configurations.setter
    def runtime_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationRuntimeConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulerConfiguration")
    def scheduler_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationSchedulerConfigurationArgs]]: ...
    @scheduler_configuration.setter
    def scheduler_configuration(
        self, value: Optional[pulumi.Input[ApplicationSchedulerConfigurationArgs]]
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:emrserverless/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_start_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAutoStartConfigurationArgs,
                    ApplicationAutoStartConfigurationArgsDict,
                ]
            ]
        ] = ...,
        auto_stop_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAutoStopConfigurationArgs,
                    ApplicationAutoStopConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationImageConfigurationArgs,
                    ApplicationImageConfigurationArgsDict,
                ]
            ]
        ] = ...,
        initial_capacities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationInitialCapacityArgs,
                            ApplicationInitialCapacityArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        interactive_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationInteractiveConfigurationArgs,
                    ApplicationInteractiveConfigurationArgsDict,
                ]
            ]
        ] = ...,
        job_level_cost_allocation_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationJobLevelCostAllocationConfigurationArgs,
                    ApplicationJobLevelCostAllocationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        maximum_capacity: Optional[
            pulumi.Input[
                Union[
                    ApplicationMaximumCapacityArgs, ApplicationMaximumCapacityArgsDict
                ]
            ]
        ] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationMonitoringConfigurationArgs,
                    ApplicationMonitoringConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationNetworkConfigurationArgs,
                    ApplicationNetworkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationRuntimeConfigurationArgs,
                            ApplicationRuntimeConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        scheduler_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationSchedulerConfigurationArgs,
                    ApplicationSchedulerConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_start_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAutoStartConfigurationArgs,
                    ApplicationAutoStartConfigurationArgsDict,
                ]
            ]
        ] = ...,
        auto_stop_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAutoStopConfigurationArgs,
                    ApplicationAutoStopConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationImageConfigurationArgs,
                    ApplicationImageConfigurationArgsDict,
                ]
            ]
        ] = ...,
        initial_capacities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationInitialCapacityArgs,
                            ApplicationInitialCapacityArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        interactive_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationInteractiveConfigurationArgs,
                    ApplicationInteractiveConfigurationArgsDict,
                ]
            ]
        ] = ...,
        job_level_cost_allocation_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationJobLevelCostAllocationConfigurationArgs,
                    ApplicationJobLevelCostAllocationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        maximum_capacity: Optional[
            pulumi.Input[
                Union[
                    ApplicationMaximumCapacityArgs, ApplicationMaximumCapacityArgsDict
                ]
            ]
        ] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationMonitoringConfigurationArgs,
                    ApplicationMonitoringConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationNetworkConfigurationArgs,
                    ApplicationNetworkConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationRuntimeConfigurationArgs,
                            ApplicationRuntimeConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        scheduler_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationSchedulerConfigurationArgs,
                    ApplicationSchedulerConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationAutoStartConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationAutoStopConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationImageConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="initialCapacities")
    def initial_capacities(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationInitialCapacity]]]: ...
    @_builtins.property
    @pulumi.getter(name="interactiveConfiguration")
    def interactive_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationInteractiveConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="jobLevelCostAllocationConfiguration")
    def job_level_cost_allocation_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationJobLevelCostAllocationConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(self) -> pulumi.Output[outputs.ApplicationMaximumCapacity]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationMonitoringConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationNetworkConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfigurations")
    def runtime_configurations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationRuntimeConfiguration]]]: ...
    @_builtins.property
    @pulumi.getter(name="schedulerConfiguration")
    def scheduler_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationSchedulerConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
