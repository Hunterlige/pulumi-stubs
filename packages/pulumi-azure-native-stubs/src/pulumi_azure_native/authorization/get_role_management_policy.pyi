import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoleManagementPolicyResult",
    "AwaitableGetRoleManagementPolicyResult",
    "get_role_management_policy",
    "get_role_management_policy_output",
]

@pulumi.output_type
class GetRoleManagementPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        display_name=...,
        effective_rules=...,
        id=...,
        is_organization_default=...,
        last_modified_by=...,
        last_modified_date_time=...,
        name=...,
        policy_properties=...,
        rules=...,
        scope=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveRules")
    def effective_rules(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isOrganizationDefault")
    def is_organization_default(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> outputs.PrincipalResponse: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDateTime")
    def last_modified_date_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyProperties")
    def policy_properties(self) -> outputs.PolicyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRoleManagementPolicyResult(GetRoleManagementPolicyResult):
    def __await__(self): ...

def get_role_management_policy(
    role_management_policy_name: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleManagementPolicyResult: ...
def get_role_management_policy_output(
    role_management_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleManagementPolicyResult]: ...
