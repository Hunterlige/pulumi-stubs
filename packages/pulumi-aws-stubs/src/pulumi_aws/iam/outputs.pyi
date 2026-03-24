import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RoleInlinePolicy",
    "GetAccessKeysAccessKeyResult",
    "GetGroupUserResult",
    "GetPolicyDocumentStatementResult",
    "GetPolicyDocumentStatementConditionResult",
    "GetPolicyDocumentStatementNotPrincipalResult",
    "GetPolicyDocumentStatementPrincipalResult",
    "GetPrincipalPolicySimulationContextResult",
    "GetPrincipalPolicySimulationResultResult",
    ...,
    "GetRoleRoleLastUsedResult",
]

@pulumi.output_type
class RoleInlinePolicy(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetAccessKeysAccessKeyResult(dict):
    def __init__(
        __self__,
        *,
        access_key_id: _builtins.str,
        create_date: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetGroupUserResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        path: _builtins.str,
        user_id: _builtins.str,
        user_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetPolicyDocumentStatementResult(dict):
    def __init__(
        __self__,
        *,
        actions: Optional[Sequence[_builtins.str]] = ...,
        conditions: Optional[
            Sequence[outputs.GetPolicyDocumentStatementConditionResult]
        ] = ...,
        effect: Optional[_builtins.str] = ...,
        not_actions: Optional[Sequence[_builtins.str]] = ...,
        not_principals: Optional[
            Sequence[outputs.GetPolicyDocumentStatementNotPrincipalResult]
        ] = ...,
        not_resources: Optional[Sequence[_builtins.str]] = ...,
        principals: Optional[
            Sequence[outputs.GetPolicyDocumentStatementPrincipalResult]
        ] = ...,
        resources: Optional[Sequence[_builtins.str]] = ...,
        sid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[Sequence[outputs.GetPolicyDocumentStatementConditionResult]]: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notPrincipals")
    def not_principals(
        self,
    ) -> Optional[Sequence[outputs.GetPolicyDocumentStatementNotPrincipalResult]]: ...
    @_builtins.property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def principals(
        self,
    ) -> Optional[Sequence[outputs.GetPolicyDocumentStatementPrincipalResult]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetPolicyDocumentStatementConditionResult(dict):
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
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str: ...

@pulumi.output_type
class GetPolicyDocumentStatementNotPrincipalResult(dict):
    def __init__(
        __self__, *, identifiers: Sequence[_builtins.str], type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetPolicyDocumentStatementPrincipalResult(dict):
    def __init__(
        __self__, *, identifiers: Sequence[_builtins.str], type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetPrincipalPolicySimulationContextResult(dict):
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
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetPrincipalPolicySimulationResultResult(dict):
    def __init__(
        __self__,
        *,
        action_name: _builtins.str,
        allowed: _builtins.bool,
        decision: _builtins.str,
        decision_details: Mapping[str, _builtins.str],
        matched_statements: Sequence[
            outputs.GetPrincipalPolicySimulationResultMatchedStatementResult
        ],
        missing_context_keys: Sequence[_builtins.str],
        resource_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def allowed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def decision(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="decisionDetails")
    def decision_details(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchedStatements")
    def matched_statements(
        self,
    ) -> Sequence[outputs.GetPrincipalPolicySimulationResultMatchedStatementResult]: ...
    @_builtins.property
    @pulumi.getter(name="missingContextKeys")
    def missing_context_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetPrincipalPolicySimulationResultMatchedStatementResult(dict):
    def __init__(
        __self__, *, source_policy_id: _builtins.str, source_policy_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourcePolicyId")
    def source_policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourcePolicyType")
    def source_policy_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetRoleRoleLastUsedResult(dict):
    def __init__(
        __self__, *, last_used_date: _builtins.str, region: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastUsedDate")
    def last_used_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
