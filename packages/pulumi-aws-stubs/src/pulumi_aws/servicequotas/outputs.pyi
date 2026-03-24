import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ServiceQuotaUsageMetric",
    "ServiceQuotaUsageMetricMetricDimension",
    "GetServiceQuotaUsageMetricResult",
    "GetServiceQuotaUsageMetricMetricDimensionResult",
    "GetTemplatesTemplateResult",
]

@pulumi.output_type
class ServiceQuotaUsageMetric(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_dimensions: Optional[
            Sequence[outputs.ServiceQuotaUsageMetricMetricDimension]
        ] = ...,
        metric_name: Optional[_builtins.str] = ...,
        metric_namespace: Optional[_builtins.str] = ...,
        metric_statistic_recommendation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDimensions")
    def metric_dimensions(
        self,
    ) -> Optional[Sequence[outputs.ServiceQuotaUsageMetricMetricDimension]]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricStatisticRecommendation")
    def metric_statistic_recommendation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceQuotaUsageMetricMetricDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        class_: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
        service: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="class")
    def class_(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetServiceQuotaUsageMetricResult(dict):
    def __init__(
        __self__,
        *,
        metric_dimensions: Sequence[
            outputs.GetServiceQuotaUsageMetricMetricDimensionResult
        ],
        metric_name: _builtins.str,
        metric_namespace: _builtins.str,
        metric_statistic_recommendation: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDimensions")
    def metric_dimensions(
        self,
    ) -> Sequence[outputs.GetServiceQuotaUsageMetricMetricDimensionResult]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricStatisticRecommendation")
    def metric_statistic_recommendation(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceQuotaUsageMetricMetricDimensionResult(dict):
    def __init__(
        __self__,
        *,
        class_: _builtins.str,
        resource: _builtins.str,
        service: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="class")
    def class_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTemplatesTemplateResult(dict):
    def __init__(
        __self__,
        *,
        global_quota: _builtins.bool,
        quota_code: _builtins.str,
        quota_name: _builtins.str,
        region: _builtins.str,
        service_code: _builtins.str,
        service_name: _builtins.str,
        unit: _builtins.str,
        value: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalQuota")
    def global_quota(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float: ...
