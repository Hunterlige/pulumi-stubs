import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PolicyDryRunSpecArgs",
    "PolicyDryRunSpecArgsDict",
    "PolicyDryRunSpecRuleArgs",
    "PolicyDryRunSpecRuleArgsDict",
    "PolicyDryRunSpecRuleConditionArgs",
    "PolicyDryRunSpecRuleConditionArgsDict",
    "PolicyDryRunSpecRuleValuesArgs",
    "PolicyDryRunSpecRuleValuesArgsDict",
    "PolicySpecArgs",
    "PolicySpecArgsDict",
    "PolicySpecRuleArgs",
    "PolicySpecRuleArgsDict",
    "PolicySpecRuleConditionArgs",
    "PolicySpecRuleConditionArgsDict",
    "PolicySpecRuleValuesArgs",
    "PolicySpecRuleValuesArgsDict",
]

class PolicyDryRunSpecArgsDict(TypedDict):
    etag: NotRequired[pulumi.Input[_builtins.str]]
    inherit_from_parent: NotRequired[pulumi.Input[_builtins.bool]]
    reset: NotRequired[pulumi.Input[_builtins.bool]]
    rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PolicyDryRunSpecRuleArgsDict]]]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyDryRunSpecArgs:
    def __init__(
        __self__,
        *,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        inherit_from_parent: Optional[pulumi.Input[_builtins.bool]] = ...,
        reset: Optional[pulumi.Input[_builtins.bool]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[PolicyDryRunSpecRuleArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @inherit_from_parent.setter
    def inherit_from_parent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def reset(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reset.setter
    def reset(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyDryRunSpecRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyDryRunSpecRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyDryRunSpecRuleArgsDict(TypedDict):
    allow_all: NotRequired[pulumi.Input[_builtins.str]]
    condition: NotRequired[pulumi.Input[PolicyDryRunSpecRuleConditionArgsDict]]
    deny_all: NotRequired[pulumi.Input[_builtins.str]]
    enforce: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[PolicyDryRunSpecRuleValuesArgsDict]]
    ...

@pulumi.input_type
class PolicyDryRunSpecRuleArgs:
    def __init__(
        __self__,
        *,
        allow_all: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[pulumi.Input[PolicyDryRunSpecRuleConditionArgs]] = ...,
        deny_all: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[PolicyDryRunSpecRuleValuesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[PolicyDryRunSpecRuleConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[PolicyDryRunSpecRuleConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deny_all.setter
    def deny_all(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[PolicyDryRunSpecRuleValuesArgs]]: ...
    @values.setter
    def values(self, value: Optional[pulumi.Input[PolicyDryRunSpecRuleValuesArgs]]): ...

class PolicyDryRunSpecRuleConditionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyDryRunSpecRuleConditionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyDryRunSpecRuleValuesArgsDict(TypedDict):
    allowed_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    denied_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PolicyDryRunSpecRuleValuesArgs:
    def __init__(
        __self__,
        *,
        allowed_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        denied_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_values.setter
    def allowed_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @denied_values.setter
    def denied_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PolicySpecArgsDict(TypedDict):
    etag: NotRequired[pulumi.Input[_builtins.str]]
    inherit_from_parent: NotRequired[pulumi.Input[_builtins.bool]]
    reset: NotRequired[pulumi.Input[_builtins.bool]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySpecRuleArgsDict]]]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicySpecArgs:
    def __init__(
        __self__,
        *,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        inherit_from_parent: Optional[pulumi.Input[_builtins.bool]] = ...,
        reset: Optional[pulumi.Input[_builtins.bool]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySpecRuleArgs]]]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @inherit_from_parent.setter
    def inherit_from_parent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def reset(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reset.setter
    def reset(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySpecRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySpecRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicySpecRuleArgsDict(TypedDict):
    allow_all: NotRequired[pulumi.Input[_builtins.str]]
    condition: NotRequired[pulumi.Input[PolicySpecRuleConditionArgsDict]]
    deny_all: NotRequired[pulumi.Input[_builtins.str]]
    enforce: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[PolicySpecRuleValuesArgsDict]]
    ...

@pulumi.input_type
class PolicySpecRuleArgs:
    def __init__(
        __self__,
        *,
        allow_all: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[pulumi.Input[PolicySpecRuleConditionArgs]] = ...,
        deny_all: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[PolicySpecRuleValuesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[PolicySpecRuleConditionArgs]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[PolicySpecRuleConditionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deny_all.setter
    def deny_all(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[PolicySpecRuleValuesArgs]]: ...
    @values.setter
    def values(self, value: Optional[pulumi.Input[PolicySpecRuleValuesArgs]]): ...

class PolicySpecRuleConditionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicySpecRuleConditionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicySpecRuleValuesArgsDict(TypedDict):
    allowed_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    denied_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PolicySpecRuleValuesArgs:
    def __init__(
        __self__,
        *,
        allowed_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        denied_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_values.setter
    def allowed_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @denied_values.setter
    def denied_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
