import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SQuotaPreferenceQuotaConfig",
    "GetSQuotaInfoDimensionsInfoResult",
    "GetSQuotaInfoDimensionsInfoDetailResult",
    "GetSQuotaInfoQuotaIncreaseEligibilityResult",
    "GetSQuotaInfosQuotaInfoResult",
    "GetSQuotaInfosQuotaInfoDimensionsInfoResult",
    "GetSQuotaInfosQuotaInfoDimensionsInfoDetailResult",
    ...,
]

@pulumi.output_type
class SQuotaPreferenceQuotaConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preferred_value: _builtins.str,
        annotations: Optional[Mapping[str, _builtins.str]] = ...,
        granted_value: Optional[_builtins.str] = ...,
        request_origin: Optional[_builtins.str] = ...,
        state_detail: Optional[_builtins.str] = ...,
        trace_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredValue")
    def preferred_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="grantedValue")
    def granted_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestOrigin")
    def request_origin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateDetail")
    def state_detail(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="traceId")
    def trace_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetSQuotaInfoDimensionsInfoResult(dict):
    def __init__(
        __self__,
        *,
        applicable_locations: Sequence[_builtins.str],
        details: Sequence[outputs.GetSQuotaInfoDimensionsInfoDetailResult],
        dimensions: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicableLocations")
    def applicable_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.GetSQuotaInfoDimensionsInfoDetailResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetSQuotaInfoDimensionsInfoDetailResult(dict):
    def __init__(__self__, *, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetSQuotaInfoQuotaIncreaseEligibilityResult(dict):
    def __init__(
        __self__, *, ineligibility_reason: _builtins.str, is_eligible: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ineligibilityReason")
    def ineligibility_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEligible")
    def is_eligible(self) -> _builtins.bool: ...

@pulumi.output_type
class GetSQuotaInfosQuotaInfoResult(dict):
    def __init__(
        __self__,
        *,
        container_type: _builtins.str,
        dimensions: Sequence[_builtins.str],
        dimensions_infos: Sequence[outputs.GetSQuotaInfosQuotaInfoDimensionsInfoResult],
        is_concurrent: _builtins.bool,
        is_fixed: _builtins.bool,
        is_precise: _builtins.bool,
        metric: _builtins.str,
        metric_display_name: _builtins.str,
        metric_unit: _builtins.str,
        name: _builtins.str,
        quota_display_name: _builtins.str,
        quota_id: _builtins.str,
        quota_increase_eligibilities: Sequence[
            outputs.GetSQuotaInfosQuotaInfoQuotaIncreaseEligibilityResult
        ],
        refresh_interval: _builtins.str,
        service: _builtins.str,
        service_request_quota_uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dimensionsInfos")
    def dimensions_infos(
        self,
    ) -> Sequence[outputs.GetSQuotaInfosQuotaInfoDimensionsInfoResult]: ...
    @_builtins.property
    @pulumi.getter(name="isConcurrent")
    def is_concurrent(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isFixed")
    def is_fixed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isPrecise")
    def is_precise(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def metric(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricDisplayName")
    def metric_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaDisplayName")
    def quota_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaIncreaseEligibilities")
    def quota_increase_eligibilities(
        self,
    ) -> Sequence[outputs.GetSQuotaInfosQuotaInfoQuotaIncreaseEligibilityResult]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRequestQuotaUri")
    def service_request_quota_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetSQuotaInfosQuotaInfoDimensionsInfoResult(dict):
    def __init__(
        __self__,
        *,
        applicable_locations: Sequence[_builtins.str],
        details: Sequence[outputs.GetSQuotaInfosQuotaInfoDimensionsInfoDetailResult],
        dimensions: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicableLocations")
    def applicable_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Sequence[outputs.GetSQuotaInfosQuotaInfoDimensionsInfoDetailResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetSQuotaInfosQuotaInfoDimensionsInfoDetailResult(dict):
    def __init__(__self__, *, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetSQuotaInfosQuotaInfoQuotaIncreaseEligibilityResult(dict):
    def __init__(
        __self__, *, ineligibility_reason: _builtins.str, is_eligible: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ineligibilityReason")
    def ineligibility_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEligible")
    def is_eligible(self) -> _builtins.bool: ...
