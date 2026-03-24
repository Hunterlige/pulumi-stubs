

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudFormationTypeLoggingConfigArgs', 'CloudFormationTypeLoggingConfigArgsDict', 'StackInstancesDeploymentTargetsArgs', 'StackInstancesDeploymentTargetsArgsDict', 'StackInstancesOperationPreferencesArgs', 'StackInstancesOperationPreferencesArgsDict', 'StackInstancesStackInstanceSummaryArgs', 'StackInstancesStackInstanceSummaryArgsDict', 'StackSetAutoDeploymentArgs', 'StackSetAutoDeploymentArgsDict', 'StackSetInstanceDeploymentTargetsArgs', 'StackSetInstanceDeploymentTargetsArgsDict', 'StackSetInstanceOperationPreferencesArgs', 'StackSetInstanceOperationPreferencesArgsDict', 'StackSetInstanceStackInstanceSummaryArgs', 'StackSetInstanceStackInstanceSummaryArgsDict', 'StackSetManagedExecutionArgs', 'StackSetManagedExecutionArgsDict', 'StackSetOperationPreferencesArgs', 'StackSetOperationPreferencesArgsDict']
class CloudFormationTypeLoggingConfigArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]
    log_role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class CloudFormationTypeLoggingConfigArgs:
    def __init__(__self__, *, log_group_name: pulumi.Input[_builtins.str], log_role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logRoleArn")
    def log_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_role_arn.setter
    def log_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class StackInstancesDeploymentTargetsArgsDict(TypedDict):
    account_filter_type: NotRequired[pulumi.Input[_builtins.str]]
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accounts_url: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class StackInstancesDeploymentTargetsArgs:
    def __init__(__self__, *, account_filter_type: Optional[pulumi.Input[_builtins.str]] = ..., accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accounts_url: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountFilterType")
    def account_filter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_filter_type.setter
    def account_filter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsUrl")
    def accounts_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accounts_url.setter
    def accounts_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitIds")
    def organizational_unit_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @organizational_unit_ids.setter
    def organizational_unit_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class StackInstancesOperationPreferencesArgsDict(TypedDict):
    concurrency_mode: NotRequired[pulumi.Input[_builtins.str]]
    failure_tolerance_count: NotRequired[pulumi.Input[_builtins.int]]
    failure_tolerance_percentage: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_count: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_percentage: NotRequired[pulumi.Input[_builtins.int]]
    region_concurrency_type: NotRequired[pulumi.Input[_builtins.str]]
    region_orders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class StackInstancesOperationPreferencesArgs:
    def __init__(__self__, *, concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., failure_tolerance_count: Optional[pulumi.Input[_builtins.int]] = ..., failure_tolerance_percentage: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_count: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_percentage: Optional[pulumi.Input[_builtins.int]] = ..., region_concurrency_type: Optional[pulumi.Input[_builtins.str]] = ..., region_orders: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @concurrency_mode.setter
    def concurrency_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_count.setter
    def max_concurrent_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_concurrency_type.setter
    def region_concurrency_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @region_orders.setter
    def region_orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class StackInstancesStackInstanceSummaryArgsDict(TypedDict):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    detailed_status: NotRequired[pulumi.Input[_builtins.str]]
    drift_status: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_id: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    stack_id: NotRequired[pulumi.Input[_builtins.str]]
    stack_set_id: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    status_reason: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StackInstancesStackInstanceSummaryArgs:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., detailed_status: Optional[pulumi.Input[_builtins.str]] = ..., drift_status: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stack_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_id: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detailed_status.setter
    def detailed_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="driftStatus")
    def drift_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @drift_status.setter
    def drift_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit_id.setter
    def organizational_unit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_id.setter
    def stack_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_id.setter
    def stack_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StackSetAutoDeploymentArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    retain_stacks_on_account_removal: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class StackSetAutoDeploymentArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., retain_stacks_on_account_removal: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStacksOnAccountRemoval")
    def retain_stacks_on_account_removal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_stacks_on_account_removal.setter
    def retain_stacks_on_account_removal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class StackSetInstanceDeploymentTargetsArgsDict(TypedDict):
    account_filter_type: NotRequired[pulumi.Input[_builtins.str]]
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accounts_url: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class StackSetInstanceDeploymentTargetsArgs:
    def __init__(__self__, *, account_filter_type: Optional[pulumi.Input[_builtins.str]] = ..., accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accounts_url: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountFilterType")
    def account_filter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_filter_type.setter
    def account_filter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsUrl")
    def accounts_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accounts_url.setter
    def accounts_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitIds")
    def organizational_unit_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @organizational_unit_ids.setter
    def organizational_unit_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class StackSetInstanceOperationPreferencesArgsDict(TypedDict):
    concurrency_mode: NotRequired[pulumi.Input[_builtins.str]]
    failure_tolerance_count: NotRequired[pulumi.Input[_builtins.int]]
    failure_tolerance_percentage: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_count: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_percentage: NotRequired[pulumi.Input[_builtins.int]]
    region_concurrency_type: NotRequired[pulumi.Input[_builtins.str]]
    region_orders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class StackSetInstanceOperationPreferencesArgs:
    def __init__(__self__, *, concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., failure_tolerance_count: Optional[pulumi.Input[_builtins.int]] = ..., failure_tolerance_percentage: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_count: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_percentage: Optional[pulumi.Input[_builtins.int]] = ..., region_concurrency_type: Optional[pulumi.Input[_builtins.str]] = ..., region_orders: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @concurrency_mode.setter
    def concurrency_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_count.setter
    def max_concurrent_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_concurrency_type.setter
    def region_concurrency_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @region_orders.setter
    def region_orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class StackSetInstanceStackInstanceSummaryArgsDict(TypedDict):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_id: NotRequired[pulumi.Input[_builtins.str]]
    stack_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StackSetInstanceStackInstanceSummaryArgs:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit_id.setter
    def organizational_unit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_id.setter
    def stack_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StackSetManagedExecutionArgsDict(TypedDict):
    active: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class StackSetManagedExecutionArgs:
    def __init__(__self__, *, active: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @active.setter
    def active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class StackSetOperationPreferencesArgsDict(TypedDict):
    failure_tolerance_count: NotRequired[pulumi.Input[_builtins.int]]
    failure_tolerance_percentage: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_count: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_percentage: NotRequired[pulumi.Input[_builtins.int]]
    region_concurrency_type: NotRequired[pulumi.Input[_builtins.str]]
    region_orders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class StackSetOperationPreferencesArgs:
    def __init__(__self__, *, failure_tolerance_count: Optional[pulumi.Input[_builtins.int]] = ..., failure_tolerance_percentage: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_count: Optional[pulumi.Input[_builtins.int]] = ..., max_concurrent_percentage: Optional[pulumi.Input[_builtins.int]] = ..., region_concurrency_type: Optional[pulumi.Input[_builtins.str]] = ..., region_orders: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_count.setter
    def max_concurrent_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_concurrency_type.setter
    def region_concurrency_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionOrders")
    def region_orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @region_orders.setter
    def region_orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


