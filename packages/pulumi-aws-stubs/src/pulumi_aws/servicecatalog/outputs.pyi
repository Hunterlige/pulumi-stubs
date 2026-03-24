import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProductProvisioningArtifactParameters",
    "ProvisionedProductOutput",
    "ProvisionedProductProvisioningParameter",
    "ProvisionedProductStackSetProvisioningPreferences",
    "ServiceActionDefinition",
    "GetLaunchPathsSummaryResult",
    "GetLaunchPathsSummaryConstraintSummaryResult",
    "GetPortfolioConstraintsDetailResult",
    ...,
]

@pulumi.output_type
class ProductProvisioningArtifactParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        disable_template_validation: Optional[_builtins.bool] = ...,
        name: Optional[_builtins.str] = ...,
        template_physical_id: Optional[_builtins.str] = ...,
        template_url: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableTemplateValidation")
    def disable_template_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templatePhysicalId")
    def template_physical_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedProductOutput(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedProductProvisioningParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        use_previous_value: Optional[_builtins.bool] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usePreviousValue")
    def use_previous_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedProductStackSetProvisioningPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accounts: Optional[Sequence[_builtins.str]] = ...,
        failure_tolerance_count: Optional[_builtins.int] = ...,
        failure_tolerance_percentage: Optional[_builtins.int] = ...,
        max_concurrency_count: Optional[_builtins.int] = ...,
        max_concurrency_percentage: Optional[_builtins.int] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrencyCount")
    def max_concurrency_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrencyPercentage")
    def max_concurrency_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServiceActionDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        version: _builtins.str,
        assume_role: Optional[_builtins.str] = ...,
        parameters: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetLaunchPathsSummaryResult(dict):
    def __init__(
        __self__,
        *,
        constraint_summaries: Sequence[
            outputs.GetLaunchPathsSummaryConstraintSummaryResult
        ],
        name: _builtins.str,
        path_id: _builtins.str,
        tags: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="constraintSummaries")
    def constraint_summaries(
        self,
    ) -> Sequence[outputs.GetLaunchPathsSummaryConstraintSummaryResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetLaunchPathsSummaryConstraintSummaryResult(dict):
    def __init__(
        __self__, *, description: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetPortfolioConstraintsDetailResult(dict):
    def __init__(
        __self__,
        *,
        constraint_id: _builtins.str,
        description: _builtins.str,
        owner: _builtins.str,
        portfolio_id: _builtins.str,
        product_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="constraintId")
    def constraint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetProvisioningArtifactsProvisioningArtifactDetailResult(dict):
    def __init__(
        __self__,
        *,
        active: _builtins.bool,
        created_time: _builtins.str,
        description: _builtins.str,
        guidance: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def guidance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
