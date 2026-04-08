import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProductProvisioningArtifactParametersArgs",
    "ProductProvisioningArtifactParametersArgsDict",
    "ProvisionedProductOutputArgs",
    "ProvisionedProductOutputArgsDict",
    "ProvisionedProductProvisioningParameterArgs",
    "ProvisionedProductProvisioningParameterArgsDict",
    ...,
    ...,
    "ServiceActionDefinitionArgs",
    "ServiceActionDefinitionArgsDict",
]

class ProductProvisioningArtifactParametersArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_template_validation: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    template_physical_id: NotRequired[pulumi.Input[_builtins.str]]
    template_url: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProductProvisioningArtifactParametersArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_template_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        template_physical_id: Optional[pulumi.Input[_builtins.str]] = ...,
        template_url: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableTemplateValidation")
    def disable_template_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_template_validation.setter
    def disable_template_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templatePhysicalId")
    def template_physical_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_physical_id.setter
    def template_physical_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_url.setter
    def template_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProvisionedProductOutputArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProvisionedProductOutputArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProvisionedProductProvisioningParameterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    use_previous_value: NotRequired[pulumi.Input[_builtins.bool]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProvisionedProductProvisioningParameterArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        use_previous_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usePreviousValue")
    def use_previous_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_previous_value.setter
    def use_previous_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProvisionedProductStackSetProvisioningPreferencesArgsDict(TypedDict):
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    failure_tolerance_count: NotRequired[pulumi.Input[_builtins.int]]
    failure_tolerance_percentage: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrency_count: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrency_percentage: NotRequired[pulumi.Input[_builtins.int]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ProvisionedProductStackSetProvisioningPreferencesArgs:
    def __init__(
        __self__,
        *,
        accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        failure_tolerance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        failure_tolerance_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrency_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrency_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accounts.setter
    def accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrencyCount")
    def max_concurrency_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrency_count.setter
    def max_concurrency_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrencyPercentage")
    def max_concurrency_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrency_percentage.setter
    def max_concurrency_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceActionDefinitionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    assume_role: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        assume_role: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assume_role.setter
    def assume_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
