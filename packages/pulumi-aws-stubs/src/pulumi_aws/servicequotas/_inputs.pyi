import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ServiceQuotaUsageMetricArgs",
    "ServiceQuotaUsageMetricArgsDict",
    "ServiceQuotaUsageMetricMetricDimensionArgs",
    "ServiceQuotaUsageMetricMetricDimensionArgsDict",
]

class ServiceQuotaUsageMetricArgsDict(TypedDict):
    metric_dimensions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceQuotaUsageMetricMetricDimensionArgsDict]]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    metric_namespace: NotRequired[pulumi.Input[_builtins.str]]
    metric_statistic_recommendation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceQuotaUsageMetricArgs:
    def __init__(
        __self__,
        *,
        metric_dimensions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceQuotaUsageMetricMetricDimensionArgs]]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_statistic_recommendation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDimensions")
    def metric_dimensions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceQuotaUsageMetricMetricDimensionArgs]]]
    ]: ...
    @metric_dimensions.setter
    def metric_dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceQuotaUsageMetricMetricDimensionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricStatisticRecommendation")
    def metric_statistic_recommendation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_statistic_recommendation.setter
    def metric_statistic_recommendation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServiceQuotaUsageMetricMetricDimensionArgsDict(TypedDict):
    class_: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceQuotaUsageMetricMetricDimensionArgs:
    def __init__(
        __self__,
        *,
        class_: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="class")
    def class_(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @class_.setter
    def class_(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
