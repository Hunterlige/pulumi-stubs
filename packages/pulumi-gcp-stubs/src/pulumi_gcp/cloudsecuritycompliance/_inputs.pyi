import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CloudControlParameterSpecArgs",
    "CloudControlParameterSpecArgsDict",
    "CloudControlParameterSpecDefaultValueArgs",
    "CloudControlParameterSpecDefaultValueArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CloudControlParameterSpecSubParameterArgs",
    "CloudControlParameterSpecSubParameterArgsDict",
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
    "CloudControlParameterSpecSubstitutionRuleArgs",
    "CloudControlParameterSpecSubstitutionRuleArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CloudControlParameterSpecValidationArgs",
    "CloudControlParameterSpecValidationArgsDict",
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
    "CloudControlParameterSpecValidationIntRangeArgs",
    ...,
    ...,
    ...,
    "CloudControlRuleArgs",
    "CloudControlRuleArgsDict",
    "CloudControlRuleCelExpressionArgs",
    "CloudControlRuleCelExpressionArgsDict",
    ...,
    ...,
    "FrameworkCloudControlDetailArgs",
    "FrameworkCloudControlDetailArgsDict",
    "FrameworkCloudControlDetailParameterArgs",
    "FrameworkCloudControlDetailParameterArgsDict",
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
    "FrameworkDeploymentCloudControlMetadataArgs",
    "FrameworkDeploymentCloudControlMetadataArgsDict",
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
    "FrameworkDeploymentFrameworkArgs",
    "FrameworkDeploymentFrameworkArgsDict",
    "FrameworkDeploymentTargetResourceConfigArgs",
    "FrameworkDeploymentTargetResourceConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class CloudControlParameterSpecArgsDict(TypedDict):
    is_required: pulumi.Input[_builtins.bool]
    name: pulumi.Input[_builtins.str]
    value_type: pulumi.Input[_builtins.str]
    default_value: NotRequired[
        pulumi.Input[CloudControlParameterSpecDefaultValueArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    sub_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CloudControlParameterSpecSubParameterArgsDict]]
        ]
    ]
    substitution_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CloudControlParameterSpecSubstitutionRuleArgsDict]]
        ]
    ]
    validation: NotRequired[pulumi.Input[CloudControlParameterSpecValidationArgsDict]]

@pulumi.input_type
class CloudControlParameterSpecArgs:
    def __init__(
        __self__,
        *,
        is_required: pulumi.Input[_builtins.bool],
        name: pulumi.Input[_builtins.str],
        value_type: pulumi.Input[_builtins.str],
        default_value: Optional[
            pulumi.Input[CloudControlParameterSpecDefaultValueArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CloudControlParameterSpecSubParameterArgs]]
            ]
        ] = ...,
        substitution_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CloudControlParameterSpecSubstitutionRuleArgs]]
            ]
        ] = ...,
        validation: Optional[
            pulumi.Input[CloudControlParameterSpecValidationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> pulumi.Input[_builtins.bool]: ...
    @is_required.setter
    def is_required(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]: ...
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(
        self,
    ) -> Optional[pulumi.Input[CloudControlParameterSpecDefaultValueArgs]]: ...
    @default_value.setter
    def default_value(
        self, value: Optional[pulumi.Input[CloudControlParameterSpecDefaultValueArgs]]
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
    @_builtins.property
    @pulumi.getter(name="subParameters")
    def sub_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecSubParameterArgs]]]
    ]: ...
    @sub_parameters.setter
    def sub_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CloudControlParameterSpecSubParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="substitutionRules")
    def substitution_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CloudControlParameterSpecSubstitutionRuleArgs]]
        ]
    ]: ...
    @substitution_rules.setter
    def substitution_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CloudControlParameterSpecSubstitutionRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[pulumi.Input[CloudControlParameterSpecValidationArgs]]: ...
    @validation.setter
    def validation(
        self, value: Optional[pulumi.Input[CloudControlParameterSpecValidationArgs]]
    ): ...

class CloudControlParameterSpecDefaultValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[CloudControlParameterSpecDefaultValueOneofValueArgsDict]
    ]
    string_list_value: NotRequired[
        pulumi.Input[CloudControlParameterSpecDefaultValueStringListValueArgsDict]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecDefaultValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[CloudControlParameterSpecDefaultValueOneofValueArgs]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[CloudControlParameterSpecDefaultValueStringListValueArgs]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecDefaultValueOneofValueArgs]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecDefaultValueOneofValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecDefaultValueStringListValueArgs]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecDefaultValueStringListValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecDefaultValueOneofValueArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecDefaultValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecDefaultValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecDefaultValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecDefaultValueOneofValueParameterValueArgs]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecDefaultValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecDefaultValueOneofValueParameterValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecDefaultValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecDefaultValueStringListValueArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecDefaultValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecSubParameterArgsDict(TypedDict):
    is_required: pulumi.Input[_builtins.bool]
    name: pulumi.Input[_builtins.str]
    value_type: pulumi.Input[_builtins.str]
    default_value: NotRequired[
        pulumi.Input[CloudControlParameterSpecSubParameterDefaultValueArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    substitution_rules: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudControlParameterSpecSubParameterSubstitutionRuleArgsDict
                ]
            ]
        ]
    ]
    validation: NotRequired[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationArgsDict]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterArgs:
    def __init__(
        __self__,
        *,
        is_required: pulumi.Input[_builtins.bool],
        name: pulumi.Input[_builtins.str],
        value_type: pulumi.Input[_builtins.str],
        default_value: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterDefaultValueArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        substitution_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudControlParameterSpecSubParameterSubstitutionRuleArgs
                    ]
                ]
            ]
        ] = ...,
        validation: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterValidationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> pulumi.Input[_builtins.bool]: ...
    @is_required.setter
    def is_required(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]: ...
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterDefaultValueArgs]
    ]: ...
    @default_value.setter
    def default_value(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterDefaultValueArgs]
        ],
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
    @_builtins.property
    @pulumi.getter(name="substitutionRules")
    def substitution_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudControlParameterSpecSubParameterSubstitutionRuleArgs]
            ]
        ]
    ]: ...
    @substitution_rules.setter
    def substitution_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudControlParameterSpecSubParameterSubstitutionRuleArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationArgs]
    ]: ...
    @validation.setter
    def validation(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterValidationArgs]
        ],
    ): ...

class CloudControlParameterSpecSubParameterDefaultValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueOneofValueArgsDict
        ]
    ]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterDefaultValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueArgs
            ]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterDefaultValueOneofValueArgs]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterDefaultValueOneofValueArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgs
        ]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecSubParameterDefaultValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterDefaultValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecSubParameterSubstitutionRuleArgsDict(TypedDict):
    attribute_substitution_rule: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgsDict
        ]
    ]
    placeholder_substitution_rule: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterSubstitutionRuleArgs:
    def __init__(
        __self__,
        *,
        attribute_substitution_rule: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgs
            ]
        ] = ...,
        placeholder_substitution_rule: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeSubstitutionRule")
    def attribute_substitution_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgs
        ]
    ]: ...
    @attribute_substitution_rule.setter
    def attribute_substitution_rule(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="placeholderSubstitutionRule")
    def placeholder_substitution_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgs
        ]
    ]: ...
    @placeholder_substitution_rule.setter
    def placeholder_substitution_rule(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRuleArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRuleArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterValidationArgsDict(TypedDict):
    allowed_values: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesArgsDict
        ]
    ]
    int_range: NotRequired[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationIntRangeArgsDict]
    ]
    regexp_pattern: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationRegexpPatternArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationArgs:
    def __init__(
        __self__,
        *,
        allowed_values: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesArgs
            ]
        ] = ...,
        int_range: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterValidationIntRangeArgs]
        ] = ...,
        regexp_pattern: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationRegexpPatternArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationAllowedValuesArgs]
    ]: ...
    @allowed_values.setter
    def allowed_values(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intRange")
    def int_range(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationIntRangeArgs]
    ]: ...
    @int_range.setter
    def int_range(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecSubParameterValidationIntRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexpPattern")
    def regexp_pattern(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecSubParameterValidationRegexpPatternArgs]
    ]: ...
    @regexp_pattern.setter
    def regexp_pattern(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationRegexpPatternArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesArgsDict(TypedDict):
    values: pulumi.Input[
        Sequence[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgsDict
            ]
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesArgs:
    def __init__(
        __self__,
        *,
        values: pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgs
            ]
        ]
    ]: ...
    @values.setter
    def values(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgs
                ]
            ]
        ],
    ): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgsDict
        ]
    ]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgs
            ]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgs
        ]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgs
        ]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecSubParameterValidationIntRangeArgsDict(TypedDict):
    max: pulumi.Input[_builtins.str]
    min: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationIntRangeArgs:
    def __init__(
        __self__, *, max: pulumi.Input[_builtins.str], min: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> pulumi.Input[_builtins.str]: ...
    @max.setter
    def max(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.str]: ...
    @min.setter
    def min(self, value: pulumi.Input[_builtins.str]): ...

class CloudControlParameterSpecSubParameterValidationRegexpPatternArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudControlParameterSpecSubParameterValidationRegexpPatternArgs:
    def __init__(__self__, *, pattern: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...

class CloudControlParameterSpecSubstitutionRuleArgsDict(TypedDict):
    attribute_substitution_rule: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgsDict
        ]
    ]
    placeholder_substitution_rule: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecSubstitutionRuleArgs:
    def __init__(
        __self__,
        *,
        attribute_substitution_rule: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgs
            ]
        ] = ...,
        placeholder_substitution_rule: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeSubstitutionRule")
    def attribute_substitution_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgs
        ]
    ]: ...
    @attribute_substitution_rule.setter
    def attribute_substitution_rule(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="placeholderSubstitutionRule")
    def placeholder_substitution_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgs
        ]
    ]: ...
    @placeholder_substitution_rule.setter
    def placeholder_substitution_rule(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRuleArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRuleArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecValidationArgsDict(TypedDict):
    allowed_values: NotRequired[
        pulumi.Input[CloudControlParameterSpecValidationAllowedValuesArgsDict]
    ]
    int_range: NotRequired[
        pulumi.Input[CloudControlParameterSpecValidationIntRangeArgsDict]
    ]
    regexp_pattern: NotRequired[
        pulumi.Input[CloudControlParameterSpecValidationRegexpPatternArgsDict]
    ]

@pulumi.input_type
class CloudControlParameterSpecValidationArgs:
    def __init__(
        __self__,
        *,
        allowed_values: Optional[
            pulumi.Input[CloudControlParameterSpecValidationAllowedValuesArgs]
        ] = ...,
        int_range: Optional[
            pulumi.Input[CloudControlParameterSpecValidationIntRangeArgs]
        ] = ...,
        regexp_pattern: Optional[
            pulumi.Input[CloudControlParameterSpecValidationRegexpPatternArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecValidationAllowedValuesArgs]
    ]: ...
    @allowed_values.setter
    def allowed_values(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecValidationAllowedValuesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intRange")
    def int_range(
        self,
    ) -> Optional[pulumi.Input[CloudControlParameterSpecValidationIntRangeArgs]]: ...
    @int_range.setter
    def int_range(
        self,
        value: Optional[pulumi.Input[CloudControlParameterSpecValidationIntRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexpPattern")
    def regexp_pattern(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlParameterSpecValidationRegexpPatternArgs]
    ]: ...
    @regexp_pattern.setter
    def regexp_pattern(
        self,
        value: Optional[
            pulumi.Input[CloudControlParameterSpecValidationRegexpPatternArgs]
        ],
    ): ...

class CloudControlParameterSpecValidationAllowedValuesArgsDict(TypedDict):
    values: pulumi.Input[
        Sequence[
            pulumi.Input[CloudControlParameterSpecValidationAllowedValuesValueArgsDict]
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesArgs:
    def __init__(
        __self__,
        *,
        values: pulumi.Input[
            Sequence[
                pulumi.Input[CloudControlParameterSpecValidationAllowedValuesValueArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[CloudControlParameterSpecValidationAllowedValuesValueArgs]
        ]
    ]: ...
    @values.setter
    def values(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[CloudControlParameterSpecValidationAllowedValuesValueArgs]
            ]
        ],
    ): ...

class CloudControlParameterSpecValidationAllowedValuesValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgsDict
        ]
    ]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgs
            ]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgs
        ]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgs
        ]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlParameterSpecValidationAllowedValuesValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class CloudControlParameterSpecValidationIntRangeArgsDict(TypedDict):
    max: pulumi.Input[_builtins.str]
    min: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudControlParameterSpecValidationIntRangeArgs:
    def __init__(
        __self__, *, max: pulumi.Input[_builtins.str], min: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> pulumi.Input[_builtins.str]: ...
    @max.setter
    def max(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.str]: ...
    @min.setter
    def min(self, value: pulumi.Input[_builtins.str]): ...

class CloudControlParameterSpecValidationRegexpPatternArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudControlParameterSpecValidationRegexpPatternArgs:
    def __init__(__self__, *, pattern: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...

class CloudControlRuleArgsDict(TypedDict):
    rule_action_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cel_expression: NotRequired[pulumi.Input[CloudControlRuleCelExpressionArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudControlRuleArgs:
    def __init__(
        __self__,
        *,
        rule_action_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        cel_expression: Optional[pulumi.Input[CloudControlRuleCelExpressionArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleActionTypes")
    def rule_action_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @rule_action_types.setter
    def rule_action_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(
        self,
    ) -> Optional[pulumi.Input[CloudControlRuleCelExpressionArgs]]: ...
    @cel_expression.setter
    def cel_expression(
        self, value: Optional[pulumi.Input[CloudControlRuleCelExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudControlRuleCelExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    resource_types_values: NotRequired[
        pulumi.Input[CloudControlRuleCelExpressionResourceTypesValuesArgsDict]
    ]

@pulumi.input_type
class CloudControlRuleCelExpressionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        resource_types_values: Optional[
            pulumi.Input[CloudControlRuleCelExpressionResourceTypesValuesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesValues")
    def resource_types_values(
        self,
    ) -> Optional[
        pulumi.Input[CloudControlRuleCelExpressionResourceTypesValuesArgs]
    ]: ...
    @resource_types_values.setter
    def resource_types_values(
        self,
        value: Optional[
            pulumi.Input[CloudControlRuleCelExpressionResourceTypesValuesArgs]
        ],
    ): ...

class CloudControlRuleCelExpressionResourceTypesValuesArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CloudControlRuleCelExpressionResourceTypesValuesArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class FrameworkCloudControlDetailArgsDict(TypedDict):
    major_revision_id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FrameworkCloudControlDetailParameterArgsDict]]
        ]
    ]

@pulumi.input_type
class FrameworkCloudControlDetailArgs:
    def __init__(
        __self__,
        *,
        major_revision_id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FrameworkCloudControlDetailParameterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> pulumi.Input[_builtins.str]: ...
    @major_revision_id.setter
    def major_revision_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FrameworkCloudControlDetailParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FrameworkCloudControlDetailParameterArgs]]
            ]
        ],
    ): ...

class FrameworkCloudControlDetailParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[
        FrameworkCloudControlDetailParameterParameterValueArgsDict
    ]

@pulumi.input_type
class FrameworkCloudControlDetailParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        parameter_value: pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> pulumi.Input[FrameworkCloudControlDetailParameterParameterValueArgs]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: pulumi.Input[FrameworkCloudControlDetailParameterParameterValueArgs],
    ): ...

class FrameworkCloudControlDetailParameterParameterValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueOneofValueArgsDict
        ]
    ]
    string_list_value: NotRequired[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrameworkCloudControlDetailParameterParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueArgs
            ]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[FrameworkCloudControlDetailParameterParameterValueOneofValueArgs]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkCloudControlDetailParameterParameterValueOneofValueArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class FrameworkCloudControlDetailParameterParameterValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgs
        ]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class FrameworkCloudControlDetailParameterParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class FrameworkCloudControlDetailParameterParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class FrameworkDeploymentCloudControlDeploymentReferenceArgsDict(TypedDict):
    cloud_control_deployment: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrameworkDeploymentCloudControlDeploymentReferenceArgs:
    def __init__(
        __self__,
        *,
        cloud_control_deployment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudControlDeployment")
    def cloud_control_deployment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_control_deployment.setter
    def cloud_control_deployment(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FrameworkDeploymentCloudControlMetadataArgsDict(TypedDict):
    cloud_control_details: pulumi.Input[
        FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgsDict
    ]
    enforcement_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataArgs:
    def __init__(
        __self__,
        *,
        cloud_control_details: pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgs
        ],
        enforcement_mode: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudControlDetails")
    def cloud_control_details(
        self,
    ) -> pulumi.Input[
        FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgs
    ]: ...
    @cloud_control_details.setter
    def cloud_control_details(
        self,
        value: pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> pulumi.Input[_builtins.str]: ...
    @enforcement_mode.setter
    def enforcement_mode(self, value: pulumi.Input[_builtins.str]): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgsDict(TypedDict):
    major_revision_id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsArgs:
    def __init__(
        __self__,
        *,
        major_revision_id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> pulumi.Input[_builtins.str]: ...
    @major_revision_id.setter
    def major_revision_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgs
                ]
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgs
                    ]
                ]
            ]
        ],
    ): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[
        FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgsDict
    ]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        parameter_value: pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> pulumi.Input[
        FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgs
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgs
        ],
    ): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    oneof_value: NotRequired[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgsDict
        ]
    ]
    string_list_value: NotRequired[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        oneof_value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgs
            ]
        ] = ...,
        string_list_value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgs
        ]
    ]: ...
    @oneof_value.setter
    def oneof_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameter_value: NotRequired[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgsDict
        ]
    ]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgs
        ]
    ]: ...
    @parameter_value.setter
    def parameter_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgs
            ]
        ],
    ): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgsDict(
    TypedDict
):
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    number_value: NotRequired[pulumi.Input[_builtins.float]]
    string_list_value: NotRequired[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_value: Optional[pulumi.Input[_builtins.float]] = ...,
        string_list_value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_value.setter
    def number_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgs
        ]
    ]: ...
    @string_list_value.setter
    def string_list_value(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValueArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class FrameworkDeploymentFrameworkArgsDict(TypedDict):
    framework: pulumi.Input[_builtins.str]
    major_revision_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class FrameworkDeploymentFrameworkArgs:
    def __init__(
        __self__,
        *,
        framework: pulumi.Input[_builtins.str],
        major_revision_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def framework(self) -> pulumi.Input[_builtins.str]: ...
    @framework.setter
    def framework(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> pulumi.Input[_builtins.str]: ...
    @major_revision_id.setter
    def major_revision_id(self, value: pulumi.Input[_builtins.str]): ...

class FrameworkDeploymentTargetResourceConfigArgsDict(TypedDict):
    existing_target_resource: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_creation_config: NotRequired[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgsDict
        ]
    ]

@pulumi.input_type
class FrameworkDeploymentTargetResourceConfigArgs:
    def __init__(
        __self__,
        *,
        existing_target_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_creation_config: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="existingTargetResource")
    def existing_target_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @existing_target_resource.setter
    def existing_target_resource(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceCreationConfig")
    def target_resource_creation_config(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgs
        ]
    ]: ...
    @target_resource_creation_config.setter
    def target_resource_creation_config(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgs
            ]
        ],
    ): ...

class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgsDict(
    TypedDict
):
    folder_creation_config: NotRequired[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgsDict
        ]
    ]
    project_creation_config: NotRequired[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgsDict
        ]
    ]

@pulumi.input_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigArgs:
    def __init__(
        __self__,
        *,
        folder_creation_config: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgs
            ]
        ] = ...,
        project_creation_config: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="folderCreationConfig")
    def folder_creation_config(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgs
        ]
    ]: ...
    @folder_creation_config.setter
    def folder_creation_config(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectCreationConfig")
    def project_creation_config(
        self,
    ) -> Optional[
        pulumi.Input[
            FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgs
        ]
    ]: ...
    @project_creation_config.setter
    def project_creation_config(
        self,
        value: Optional[
            pulumi.Input[
                FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgs
            ]
        ],
    ): ...

class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgsDict(
    TypedDict
):
    folder_display_name: pulumi.Input[_builtins.str]
    parent: pulumi.Input[_builtins.str]

@pulumi.input_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfigArgs:
    def __init__(
        __self__,
        *,
        folder_display_name: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="folderDisplayName")
    def folder_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @folder_display_name.setter
    def folder_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...

class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgsDict(
    TypedDict
):
    billing_account_id: pulumi.Input[_builtins.str]
    parent: pulumi.Input[_builtins.str]
    project_display_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfigArgs:
    def __init__(
        __self__,
        *,
        billing_account_id: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        project_display_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectDisplayName")
    def project_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_display_name.setter
    def project_display_name(self, value: pulumi.Input[_builtins.str]): ...
