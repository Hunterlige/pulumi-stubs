import builtins as _builtins
import sys
import pulumi
from typing import Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLicenseGrantsFilterResult",
    "GetReceivedLicenseConsumptionConfigurationResult",
    ...,
    ...,
    "GetReceivedLicenseEntitlementResult",
    "GetReceivedLicenseIssuerResult",
    "GetReceivedLicenseLicenseMetadataResult",
    "GetReceivedLicenseReceivedMetadataResult",
    "GetReceivedLicenseValidityResult",
    "GetReceivedLicensesFilterResult",
]

@pulumi.output_type
class GetLicenseGrantsFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetReceivedLicenseConsumptionConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        borrow_configurations: Sequence[
            outputs.GetReceivedLicenseConsumptionConfigurationBorrowConfigurationResult
        ],
        provisional_configurations: Sequence[
            outputs.GetReceivedLicenseConsumptionConfigurationProvisionalConfigurationResult
        ],
        renew_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="borrowConfigurations")
    def borrow_configurations(
        self,
    ) -> Sequence[
        outputs.GetReceivedLicenseConsumptionConfigurationBorrowConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisionalConfigurations")
    def provisional_configurations(
        self,
    ) -> Sequence[
        outputs.GetReceivedLicenseConsumptionConfigurationProvisionalConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="renewType")
    def renew_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicenseConsumptionConfigurationBorrowConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        allow_early_check_in: _builtins.bool,
        max_time_to_live_in_minutes: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowEarlyCheckIn")
    def allow_early_check_in(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxTimeToLiveInMinutes")
    def max_time_to_live_in_minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetReceivedLicenseConsumptionConfigurationProvisionalConfigurationResult(dict):
    def __init__(__self__, *, max_time_to_live_in_minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTimeToLiveInMinutes")
    def max_time_to_live_in_minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetReceivedLicenseEntitlementResult(dict):
    def __init__(
        __self__,
        *,
        allow_check_in: _builtins.bool,
        max_count: _builtins.int,
        name: _builtins.str,
        overage: _builtins.bool,
        unit: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCheckIn")
    def allow_check_in(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def overage(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicenseIssuerResult(dict):
    def __init__(
        __self__,
        *,
        key_fingerprint: _builtins.str,
        name: _builtins.str,
        sign_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signKey")
    def sign_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicenseLicenseMetadataResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicenseReceivedMetadataResult(dict):
    def __init__(
        __self__,
        *,
        allowed_operations: Sequence[_builtins.str],
        received_status: _builtins.str,
        received_status_reason: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="receivedStatus")
    def received_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="receivedStatusReason")
    def received_status_reason(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicenseValidityResult(dict):
    def __init__(__self__, *, begin: _builtins.str, end: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def begin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.str: ...

@pulumi.output_type
class GetReceivedLicensesFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
