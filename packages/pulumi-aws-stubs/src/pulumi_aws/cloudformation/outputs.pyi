import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CloudFormationTypeLoggingConfig",
    "StackInstancesDeploymentTargets",
    "StackInstancesOperationPreferences",
    "StackInstancesStackInstanceSummary",
    "StackSetAutoDeployment",
    "StackSetInstanceDeploymentTargets",
    "StackSetInstanceOperationPreferences",
    "StackSetInstanceStackInstanceSummary",
    "StackSetManagedExecution",
    "StackSetOperationPreferences",
    "GetCloudFormationTypeLoggingConfigResult",
]

@pulumi.output_type
class CloudFormationTypeLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, log_group_name: _builtins.str, log_role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logRoleArn")
    def log_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class StackInstancesDeploymentTargets(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_filter_type: Optional[_builtins.str] = ...,
        accounts: Optional[Sequence[_builtins.str]] = ...,
        accounts_url: Optional[_builtins.str] = ...,
        organizational_unit_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountFilterType")
    def account_filter_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="accountsUrl")
    def accounts_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitIds")
    def organizational_unit_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackInstancesOperationPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        concurrency_mode: Optional[_builtins.str] = ...,
        failure_tolerance_count: Optional[_builtins.int] = ...,
        failure_tolerance_percentage: Optional[_builtins.int] = ...,
        max_concurrent_count: Optional[_builtins.int] = ...,
        max_concurrent_percentage: Optional[_builtins.int] = ...,
        region_concurrency_type: Optional[_builtins.str] = ...,
        region_orders: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackInstancesStackInstanceSummary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: Optional[_builtins.str] = ...,
        detailed_status: Optional[_builtins.str] = ...,
        drift_status: Optional[_builtins.str] = ...,
        organizational_unit_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        stack_id: Optional[_builtins.str] = ...,
        stack_set_id: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        status_reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="driftStatus")
    def drift_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackSetAutoDeployment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        retain_stacks_on_account_removal: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="retainStacksOnAccountRemoval")
    def retain_stacks_on_account_removal(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StackSetInstanceDeploymentTargets(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_filter_type: Optional[_builtins.str] = ...,
        accounts: Optional[Sequence[_builtins.str]] = ...,
        accounts_url: Optional[_builtins.str] = ...,
        organizational_unit_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountFilterType")
    def account_filter_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="accountsUrl")
    def accounts_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitIds")
    def organizational_unit_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackSetInstanceOperationPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        concurrency_mode: Optional[_builtins.str] = ...,
        failure_tolerance_count: Optional[_builtins.int] = ...,
        failure_tolerance_percentage: Optional[_builtins.int] = ...,
        max_concurrent_count: Optional[_builtins.int] = ...,
        max_concurrent_percentage: Optional[_builtins.int] = ...,
        region_concurrency_type: Optional[_builtins.str] = ...,
        region_orders: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackSetInstanceStackInstanceSummary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: Optional[_builtins.str] = ...,
        organizational_unit_id: Optional[_builtins.str] = ...,
        stack_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackSetManagedExecution(dict):
    def __init__(__self__, *, active: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StackSetOperationPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_tolerance_count: Optional[_builtins.int] = ...,
        failure_tolerance_percentage: Optional[_builtins.int] = ...,
        max_concurrent_count: Optional[_builtins.int] = ...,
        max_concurrent_percentage: Optional[_builtins.int] = ...,
        region_concurrency_type: Optional[_builtins.str] = ...,
        region_orders: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetCloudFormationTypeLoggingConfigResult(dict):
    def __init__(
        __self__, *, log_group_name: _builtins.str, log_role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logRoleArn")
    def log_role_arn(self) -> _builtins.str: ...
