import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PosturePolicySetArgs",
    "PosturePolicySetArgsDict",
    "PosturePolicySetPolicyArgs",
    "PosturePolicySetPolicyArgsDict",
    "PosturePolicySetPolicyComplianceStandardArgs",
    "PosturePolicySetPolicyComplianceStandardArgsDict",
    "PosturePolicySetPolicyConstraintArgs",
    "PosturePolicySetPolicyConstraintArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class PosturePolicySetArgsDict(TypedDict):
    policies: pulumi.Input[Sequence[pulumi.Input[PosturePolicySetPolicyArgsDict]]]
    policy_set_id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetArgs:
    def __init__(
        __self__,
        *,
        policies: pulumi.Input[Sequence[pulumi.Input[PosturePolicySetPolicyArgs]]],
        policy_set_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PosturePolicySetPolicyArgs]]]: ...
    @policies.setter
    def policies(
        self, value: pulumi.Input[Sequence[pulumi.Input[PosturePolicySetPolicyArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policySetId")
    def policy_set_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_set_id.setter
    def policy_set_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyArgsDict(TypedDict):
    constraint: pulumi.Input[PosturePolicySetPolicyConstraintArgsDict]
    policy_id: pulumi.Input[_builtins.str]
    compliance_standards: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PosturePolicySetPolicyComplianceStandardArgsDict]]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyArgs:
    def __init__(
        __self__,
        *,
        constraint: pulumi.Input[PosturePolicySetPolicyConstraintArgs],
        policy_id: pulumi.Input[_builtins.str],
        compliance_standards: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PosturePolicySetPolicyComplianceStandardArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> pulumi.Input[PosturePolicySetPolicyConstraintArgs]: ...
    @constraint.setter
    def constraint(self, value: pulumi.Input[PosturePolicySetPolicyConstraintArgs]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="complianceStandards")
    def compliance_standards(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PosturePolicySetPolicyComplianceStandardArgs]]
        ]
    ]: ...
    @compliance_standards.setter
    def compliance_standards(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PosturePolicySetPolicyComplianceStandardArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyComplianceStandardArgsDict(TypedDict):
    control: NotRequired[pulumi.Input[_builtins.str]]
    standard: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyComplianceStandardArgs:
    def __init__(
        __self__,
        *,
        control: Optional[pulumi.Input[_builtins.str]] = ...,
        standard: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control.setter
    def control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def standard(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @standard.setter
    def standard(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyConstraintArgsDict(TypedDict):
    org_policy_constraint: NotRequired[
        pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintArgsDict]
    ]
    org_policy_constraint_custom: NotRequired[
        pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgsDict]
    ]
    security_health_analytics_custom_module: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgsDict
        ]
    ]
    security_health_analytics_module: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgsDict
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintArgs:
    def __init__(
        __self__,
        *,
        org_policy_constraint: Optional[
            pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintArgs]
        ] = ...,
        org_policy_constraint_custom: Optional[
            pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgs]
        ] = ...,
        security_health_analytics_custom_module: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgs
            ]
        ] = ...,
        security_health_analytics_module: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="orgPolicyConstraint")
    def org_policy_constraint(
        self,
    ) -> Optional[
        pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintArgs]
    ]: ...
    @org_policy_constraint.setter
    def org_policy_constraint(
        self,
        value: Optional[
            pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="orgPolicyConstraintCustom")
    def org_policy_constraint_custom(
        self,
    ) -> Optional[
        pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgs]
    ]: ...
    @org_policy_constraint_custom.setter
    def org_policy_constraint_custom(
        self,
        value: Optional[
            pulumi.Input[PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityHealthAnalyticsCustomModule")
    def security_health_analytics_custom_module(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgs
        ]
    ]: ...
    @security_health_analytics_custom_module.setter
    def security_health_analytics_custom_module(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityHealthAnalyticsModule")
    def security_health_analytics_module(
        self,
    ) -> Optional[
        pulumi.Input[PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgs]
    ]: ...
    @security_health_analytics_module.setter
    def security_health_analytics_module(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgs
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintArgsDict(TypedDict):
    canned_constraint_id: pulumi.Input[_builtins.str]
    policy_rules: pulumi.Input[
        Sequence[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgsDict
            ]
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintArgs:
    def __init__(
        __self__,
        *,
        canned_constraint_id: pulumi.Input[_builtins.str],
        policy_rules: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedConstraintId")
    def canned_constraint_id(self) -> pulumi.Input[_builtins.str]: ...
    @canned_constraint_id.setter
    def canned_constraint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyRules")
    def policy_rules(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgs
            ]
        ]
    ]: ...
    @policy_rules.setter
    def policy_rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgs
                ]
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgsDict(TypedDict):
    policy_rules: pulumi.Input[
        Sequence[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgsDict
            ]
        ]
    ]
    custom_constraint: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgsDict
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomArgs:
    def __init__(
        __self__,
        *,
        policy_rules: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgs
                ]
            ]
        ],
        custom_constraint: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyRules")
    def policy_rules(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgs
            ]
        ]
    ]: ...
    @policy_rules.setter
    def policy_rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customConstraint")
    def custom_constraint(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgs
        ]
    ]: ...
    @custom_constraint.setter
    def custom_constraint(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgs
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgsDict(
    TypedDict
):
    action_type: pulumi.Input[_builtins.str]
    condition: pulumi.Input[_builtins.str]
    method_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraintArgs:
    def __init__(
        __self__,
        *,
        action_type: pulumi.Input[_builtins.str],
        condition: pulumi.Input[_builtins.str],
        method_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
        resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[_builtins.str]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="methodTypes")
    def method_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @method_types.setter
    def method_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgsDict(
    TypedDict
):
    allow_all: NotRequired[pulumi.Input[_builtins.bool]]
    condition: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgsDict
        ]
    ]
    deny_all: NotRequired[pulumi.Input[_builtins.bool]]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgsDict
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        allow_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        condition: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgs
            ]
        ] = ...,
        deny_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce: Optional[pulumi.Input[_builtins.bool]] = ...,
        values: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgs
        ]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deny_all.setter
    def deny_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgs
        ]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgs
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgsDict(
    TypedDict
):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgsDict(
    TypedDict
):
    allowed_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    denied_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValuesArgs:
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

class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgsDict(TypedDict):
    allow_all: NotRequired[pulumi.Input[_builtins.bool]]
    condition: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgsDict
        ]
    ]
    deny_all: NotRequired[pulumi.Input[_builtins.bool]]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgsDict
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        allow_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        condition: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgs
            ]
        ] = ...,
        deny_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        enforce: Optional[pulumi.Input[_builtins.bool]] = ...,
        values: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgs
        ]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deny_all.setter
    def deny_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgs
        ]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgs
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgsDict(
    TypedDict
):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgsDict(
    TypedDict
):
    allowed_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    denied_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValuesArgs:
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

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgsDict(
    TypedDict
):
    config: pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgsDict
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    module_enablement_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgs
        ],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        module_enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgs
    ]: ...
    @config.setter
    def config(
        self,
        value: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="moduleEnablementState")
    def module_enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @module_enablement_state.setter
    def module_enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgsDict(
    TypedDict
):
    predicate: pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgsDict
    ]
    resource_selector: pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgsDict
    ]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgsDict
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    recommendation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigArgs:
    def __init__(
        __self__,
        *,
        predicate: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgs
        ],
        resource_selector: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgs
        ],
        severity: pulumi.Input[_builtins.str],
        custom_output: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgs
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        recommendation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(
        self,
    ) -> pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgs
    ]: ...
    @predicate.setter
    def predicate(
        self,
        value: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> pulumi.Input[
        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgs
    ]: ...
    @resource_selector.setter
    def resource_selector(
        self,
        value: pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgs
        ]
    ]: ...
    @custom_output.setter
    def custom_output(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recommendation.setter
    def recommendation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgsDict(
    TypedDict
):
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputArgs:
    def __init__(
        __self__,
        *,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value_expression: NotRequired[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgsDict
        ]
    ]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value_expression: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        pulumi.Input[
            PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgs
        ]
    ]: ...
    @value_expression.setter
    def value_expression(
        self,
        value: Optional[
            pulumi.Input[
                PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgs
            ]
        ],
    ): ...

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgsDict(
    TypedDict
):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgsDict(
    TypedDict
):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicateArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgsDict(
    TypedDict
):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelectorArgs:
    def __init__(
        __self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgsDict(TypedDict):
    module_name: pulumi.Input[_builtins.str]
    module_enablement_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModuleArgs:
    def __init__(
        __self__,
        *,
        module_name: pulumi.Input[_builtins.str],
        module_enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> pulumi.Input[_builtins.str]: ...
    @module_name.setter
    def module_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="moduleEnablementState")
    def module_enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @module_enablement_state.setter
    def module_enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
