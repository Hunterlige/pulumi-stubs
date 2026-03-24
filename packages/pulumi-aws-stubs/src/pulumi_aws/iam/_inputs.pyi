import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AWSPrincipalArgs",
    "AWSPrincipalArgsDict",
    "FederatedPrincipalArgs",
    "FederatedPrincipalArgsDict",
    "PolicyDocumentArgs",
    "PolicyDocumentArgsDict",
    "PolicyStatementArgs",
    "PolicyStatementArgsDict",
    "RoleInlinePolicyArgs",
    "RoleInlinePolicyArgsDict",
    "ServicePrincipalArgs",
    "ServicePrincipalArgsDict",
    "GetPolicyDocumentStatementArgs",
    "GetPolicyDocumentStatementArgsDict",
    "GetPolicyDocumentStatementConditionArgs",
    "GetPolicyDocumentStatementConditionArgsDict",
    "GetPolicyDocumentStatementNotPrincipalArgs",
    "GetPolicyDocumentStatementNotPrincipalArgsDict",
    "GetPolicyDocumentStatementPrincipalArgs",
    "GetPolicyDocumentStatementPrincipalArgsDict",
    "GetPrincipalPolicySimulationContextArgs",
    "GetPrincipalPolicySimulationContextArgsDict",
]

class AWSPrincipalArgsDict(TypedDict):
    aws: pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AWSPrincipalArgs:
    def __init__(
        __self__,
        *,
        aws: pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="AWS")
    def aws(
        self,
    ) -> pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aws.setter
    def aws(
        self,
        value: pulumi.Input[
            Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]
        ],
    ): ...

class FederatedPrincipalArgsDict(TypedDict):
    federated: pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class FederatedPrincipalArgs:
    def __init__(
        __self__,
        *,
        federated: pulumi.Input[
            Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Federated")
    def federated(
        self,
    ) -> pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]: ...
    @federated.setter
    def federated(
        self,
        value: pulumi.Input[
            Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]
        ],
    ): ...

class PolicyDocumentArgsDict(TypedDict):
    statement: pulumi.Input[Sequence[pulumi.Input[PolicyStatementArgsDict]]]
    version: pulumi.Input[PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(
        __self__,
        *,
        statement: pulumi.Input[Sequence[pulumi.Input[PolicyStatementArgs]]],
        version: pulumi.Input[PolicyDocumentVersion],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PolicyStatementArgs]]]: ...
    @statement.setter
    def statement(
        self, value: pulumi.Input[Sequence[pulumi.Input[PolicyStatementArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[PolicyDocumentVersion]: ...
    @version.setter
    def version(self, value: pulumi.Input[PolicyDocumentVersion]): ...
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyStatementArgsDict(TypedDict):
    effect: pulumi.Input[PolicyStatementEffect]
    action: NotRequired[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]
    condition: NotRequired[pulumi.Input[Mapping[str, Any]]]
    not_action: NotRequired[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]
    not_principal: NotRequired[
        pulumi.Input[
            Union[
                _builtins.str,
                AWSPrincipalArgsDict,
                ServicePrincipalArgsDict,
                FederatedPrincipalArgsDict,
            ]
        ]
    ]
    not_resource: NotRequired[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]
    principal: NotRequired[
        pulumi.Input[
            Union[
                _builtins.str,
                AWSPrincipalArgsDict,
                ServicePrincipalArgsDict,
                FederatedPrincipalArgsDict,
            ]
        ]
    ]
    resource: NotRequired[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]
    sid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyStatementArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[PolicyStatementEffect],
        action: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ] = ...,
        condition: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        not_action: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ] = ...,
        not_principal: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    AWSPrincipalArgs,
                    ServicePrincipalArgs,
                    FederatedPrincipalArgs,
                ]
            ]
        ] = ...,
        not_resource: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ] = ...,
        principal: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    AWSPrincipalArgs,
                    ServicePrincipalArgs,
                    FederatedPrincipalArgs,
                ]
            ]
        ] = ...,
        resource: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ] = ...,
        sid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Effect")
    def effect(self) -> pulumi.Input[PolicyStatementEffect]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[PolicyStatementEffect]): ...
    @_builtins.property
    @pulumi.getter(name="Action")
    def action(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]: ...
    @action.setter
    def action(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="Condition")
    def condition(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...
    @_builtins.property
    @pulumi.getter(name="NotAction")
    def not_action(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]: ...
    @not_action.setter
    def not_action(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="NotPrincipal")
    def not_principal(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                _builtins.str,
                AWSPrincipalArgs,
                ServicePrincipalArgs,
                FederatedPrincipalArgs,
            ]
        ]
    ]: ...
    @not_principal.setter
    def not_principal(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    AWSPrincipalArgs,
                    ServicePrincipalArgs,
                    FederatedPrincipalArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="NotResource")
    def not_resource(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]: ...
    @not_resource.setter
    def not_resource(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="Principal")
    def principal(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                _builtins.str,
                AWSPrincipalArgs,
                ServicePrincipalArgs,
                FederatedPrincipalArgs,
            ]
        ]
    ]: ...
    @principal.setter
    def principal(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    AWSPrincipalArgs,
                    ServicePrincipalArgs,
                    FederatedPrincipalArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="Resource")
    def resource(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ]: ...
    @resource.setter
    def resource(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="Sid")
    def sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sid.setter
    def sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoleInlinePolicyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RoleInlinePolicyArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePrincipalArgsDict(TypedDict):
    service: pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ServicePrincipalArgs:
    def __init__(
        __self__,
        *,
        service: pulumi.Input[
            Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Service")
    def service(
        self,
    ) -> pulumi.Input[Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service.setter
    def service(
        self,
        value: pulumi.Input[
            Union[_builtins.str, Sequence[pulumi.Input[_builtins.str]]]
        ],
    ): ...

class GetPolicyDocumentStatementArgsDict(TypedDict):
    actions: NotRequired[Sequence[_builtins.str]]
    conditions: NotRequired[Sequence[GetPolicyDocumentStatementConditionArgsDict]]
    effect: NotRequired[_builtins.str]
    not_actions: NotRequired[Sequence[_builtins.str]]
    not_principals: NotRequired[
        Sequence[GetPolicyDocumentStatementNotPrincipalArgsDict]
    ]
    not_resources: NotRequired[Sequence[_builtins.str]]
    principals: NotRequired[Sequence[GetPolicyDocumentStatementPrincipalArgsDict]]
    resources: NotRequired[Sequence[_builtins.str]]
    sid: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetPolicyDocumentStatementArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[Sequence[_builtins.str]] = ...,
        conditions: Optional[Sequence[GetPolicyDocumentStatementConditionArgs]] = ...,
        effect: Optional[_builtins.str] = ...,
        not_actions: Optional[Sequence[_builtins.str]] = ...,
        not_principals: Optional[
            Sequence[GetPolicyDocumentStatementNotPrincipalArgs]
        ] = ...,
        not_resources: Optional[Sequence[_builtins.str]] = ...,
        principals: Optional[Sequence[GetPolicyDocumentStatementPrincipalArgs]] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        sid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @actions.setter
    def actions(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[Sequence[GetPolicyDocumentStatementConditionArgs]]: ...
    @conditions.setter
    def conditions(
        self, value: Optional[Sequence[GetPolicyDocumentStatementConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @effect.setter
    def effect(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @not_actions.setter
    def not_actions(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notPrincipals")
    def not_principals(
        self,
    ) -> Optional[Sequence[GetPolicyDocumentStatementNotPrincipalArgs]]: ...
    @not_principals.setter
    def not_principals(
        self, value: Optional[Sequence[GetPolicyDocumentStatementNotPrincipalArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @not_resources.setter
    def not_resources(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def principals(
        self,
    ) -> Optional[Sequence[GetPolicyDocumentStatementPrincipalArgs]]: ...
    @principals.setter
    def principals(
        self, value: Optional[Sequence[GetPolicyDocumentStatementPrincipalArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @resources.setter
    def resources(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]: ...
    @sid.setter
    def sid(self, value: Optional[_builtins.str]): ...

class GetPolicyDocumentStatementConditionArgsDict(TypedDict):
    test: _builtins.str
    values: Sequence[_builtins.str]
    variable: _builtins.str
    ...

@pulumi.input_type
class GetPolicyDocumentStatementConditionArgs:
    def __init__(
        __self__,
        *,
        test: _builtins.str,
        values: Sequence[_builtins.str],
        variable: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def test(self) -> _builtins.str: ...
    @test.setter
    def test(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str: ...
    @variable.setter
    def variable(self, value: _builtins.str): ...

class GetPolicyDocumentStatementNotPrincipalArgsDict(TypedDict):
    identifiers: Sequence[_builtins.str]
    type: _builtins.str
    ...

@pulumi.input_type
class GetPolicyDocumentStatementNotPrincipalArgs:
    def __init__(
        __self__, *, identifiers: Sequence[_builtins.str], type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]: ...
    @identifiers.setter
    def identifiers(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...

class GetPolicyDocumentStatementPrincipalArgsDict(TypedDict):
    identifiers: Sequence[_builtins.str]
    type: _builtins.str
    ...

@pulumi.input_type
class GetPolicyDocumentStatementPrincipalArgs:
    def __init__(
        __self__, *, identifiers: Sequence[_builtins.str], type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]: ...
    @identifiers.setter
    def identifiers(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...

class GetPrincipalPolicySimulationContextArgsDict(TypedDict):
    key: _builtins.str
    type: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetPrincipalPolicySimulationContextArgs:
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        type: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @key.setter
    def key(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
