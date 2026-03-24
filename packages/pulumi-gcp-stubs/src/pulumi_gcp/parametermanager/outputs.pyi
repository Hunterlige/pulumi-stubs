import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ParameterPolicyMember",
    "RegionalParameterPolicyMember",
    "GetParameterPolicyMemberResult",
    "GetParametersParameterResult",
    "GetParametersParameterPolicyMemberResult",
    "GetRegionalParameterPolicyMemberResult",
    "GetRegionalParametersParameterResult",
    "GetRegionalParametersParameterPolicyMemberResult",
]

@pulumi.output_type
class ParameterPolicyMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: Optional[_builtins.str] = ...,
        iam_policy_uid_principal: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegionalParameterPolicyMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: Optional[_builtins.str] = ...,
        iam_policy_uid_principal: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetParameterPolicyMemberResult(dict):
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: _builtins.str,
        iam_policy_uid_principal: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetParametersParameterResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        format: _builtins.str,
        kms_key: _builtins.str,
        labels: Mapping[str, _builtins.str],
        name: _builtins.str,
        parameter_id: _builtins.str,
        policy_members: Sequence[outputs.GetParametersParameterPolicyMemberResult],
        project: _builtins.str,
        pulumi_labels: Mapping[str, _builtins.str],
        update_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyMembers")
    def policy_members(
        self,
    ) -> Sequence[outputs.GetParametersParameterPolicyMemberResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetParametersParameterPolicyMemberResult(dict):
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: _builtins.str,
        iam_policy_uid_principal: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetRegionalParameterPolicyMemberResult(dict):
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: _builtins.str,
        iam_policy_uid_principal: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetRegionalParametersParameterResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        format: _builtins.str,
        kms_key: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
        name: _builtins.str,
        parameter_id: _builtins.str,
        policy_members: Sequence[
            outputs.GetRegionalParametersParameterPolicyMemberResult
        ],
        project: _builtins.str,
        pulumi_labels: Mapping[str, _builtins.str],
        update_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyMembers")
    def policy_members(
        self,
    ) -> Sequence[outputs.GetRegionalParametersParameterPolicyMemberResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetRegionalParametersParameterPolicyMemberResult(dict):
    def __init__(
        __self__,
        *,
        iam_policy_name_principal: _builtins.str,
        iam_policy_uid_principal: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> _builtins.str: ...
