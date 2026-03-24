import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RecommendationPreferencesArgs", "RecommendationPreferences"]

@pulumi.input_type
class RecommendationPreferencesArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        scope: pulumi.Input[RecommendationPreferencesScopeArgs],
        enhanced_infrastructure_metrics: Optional[pulumi.Input[_builtins.str]] = ...,
        external_metrics_preference: Optional[
            pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
        ] = ...,
        inferred_workload_types: Optional[pulumi.Input[_builtins.str]] = ...,
        look_back_period: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        utilization_preferences: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[RecommendationPreferencesScopeArgs]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[RecommendationPreferencesScopeArgs]): ...
    @_builtins.property
    @pulumi.getter(name="enhancedInfrastructureMetrics")
    def enhanced_infrastructure_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enhanced_infrastructure_metrics.setter
    def enhanced_infrastructure_metrics(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalMetricsPreference")
    def external_metrics_preference(
        self,
    ) -> Optional[
        pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
    ]: ...
    @external_metrics_preference.setter
    def external_metrics_preference(
        self,
        value: Optional[
            pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferredWorkloadTypes")
    def inferred_workload_types(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inferred_workload_types.setter
    def inferred_workload_types(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookBackPeriod")
    def look_back_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @look_back_period.setter
    def look_back_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredResources")
    def preferred_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
        ]
    ]: ...
    @preferred_resources.setter
    def preferred_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @savings_estimation_mode.setter
    def savings_estimation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="utilizationPreferences")
    def utilization_preferences(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]]
        ]
    ]: ...
    @utilization_preferences.setter
    def utilization_preferences(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]
                ]
            ]
        ],
    ): ...

@pulumi.input_type
class _RecommendationPreferencesState:
    def __init__(
        __self__,
        *,
        enhanced_infrastructure_metrics: Optional[pulumi.Input[_builtins.str]] = ...,
        external_metrics_preference: Optional[
            pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
        ] = ...,
        inferred_workload_types: Optional[pulumi.Input[_builtins.str]] = ...,
        look_back_period: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[RecommendationPreferencesScopeArgs]] = ...,
        utilization_preferences: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enhancedInfrastructureMetrics")
    def enhanced_infrastructure_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enhanced_infrastructure_metrics.setter
    def enhanced_infrastructure_metrics(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalMetricsPreference")
    def external_metrics_preference(
        self,
    ) -> Optional[
        pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
    ]: ...
    @external_metrics_preference.setter
    def external_metrics_preference(
        self,
        value: Optional[
            pulumi.Input[RecommendationPreferencesExternalMetricsPreferenceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferredWorkloadTypes")
    def inferred_workload_types(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inferred_workload_types.setter
    def inferred_workload_types(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookBackPeriod")
    def look_back_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @look_back_period.setter
    def look_back_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredResources")
    def preferred_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
        ]
    ]: ...
    @preferred_resources.setter
    def preferred_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecommendationPreferencesPreferredResourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @savings_estimation_mode.setter
    def savings_estimation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[RecommendationPreferencesScopeArgs]]: ...
    @scope.setter
    def scope(
        self, value: Optional[pulumi.Input[RecommendationPreferencesScopeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="utilizationPreferences")
    def utilization_preferences(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]]
        ]
    ]: ...
    @utilization_preferences.setter
    def utilization_preferences(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecommendationPreferencesUtilizationPreferenceArgs]
                ]
            ]
        ],
    ): ...

@pulumi.type_token(...)
class RecommendationPreferences(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enhanced_infrastructure_metrics: Optional[pulumi.Input[_builtins.str]] = ...,
        external_metrics_preference: Optional[
            pulumi.Input[
                Union[
                    RecommendationPreferencesExternalMetricsPreferenceArgs,
                    RecommendationPreferencesExternalMetricsPreferenceArgsDict,
                ]
            ]
        ] = ...,
        inferred_workload_types: Optional[pulumi.Input[_builtins.str]] = ...,
        look_back_period: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecommendationPreferencesPreferredResourceArgs,
                            RecommendationPreferencesPreferredResourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[
            pulumi.Input[
                Union[
                    RecommendationPreferencesScopeArgs,
                    RecommendationPreferencesScopeArgsDict,
                ]
            ]
        ] = ...,
        utilization_preferences: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecommendationPreferencesUtilizationPreferenceArgs,
                            RecommendationPreferencesUtilizationPreferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RecommendationPreferencesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        enhanced_infrastructure_metrics: Optional[pulumi.Input[_builtins.str]] = ...,
        external_metrics_preference: Optional[
            pulumi.Input[
                Union[
                    RecommendationPreferencesExternalMetricsPreferenceArgs,
                    RecommendationPreferencesExternalMetricsPreferenceArgsDict,
                ]
            ]
        ] = ...,
        inferred_workload_types: Optional[pulumi.Input[_builtins.str]] = ...,
        look_back_period: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecommendationPreferencesPreferredResourceArgs,
                            RecommendationPreferencesPreferredResourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        savings_estimation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[
            pulumi.Input[
                Union[
                    RecommendationPreferencesScopeArgs,
                    RecommendationPreferencesScopeArgsDict,
                ]
            ]
        ] = ...,
        utilization_preferences: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecommendationPreferencesUtilizationPreferenceArgs,
                            RecommendationPreferencesUtilizationPreferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> RecommendationPreferences: ...
    @_builtins.property
    @pulumi.getter(name="enhancedInfrastructureMetrics")
    def enhanced_infrastructure_metrics(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="externalMetricsPreference")
    def external_metrics_preference(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RecommendationPreferencesExternalMetricsPreference]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inferredWorkloadTypes")
    def inferred_workload_types(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lookBackPeriod")
    def look_back_period(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredResources")
    def preferred_resources(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RecommendationPreferencesPreferredResource]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="savingsEstimationMode")
    def savings_estimation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[outputs.RecommendationPreferencesScope]: ...
    @_builtins.property
    @pulumi.getter(name="utilizationPreferences")
    def utilization_preferences(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RecommendationPreferencesUtilizationPreference]]
    ]: ...
