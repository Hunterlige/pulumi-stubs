import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrincipalPolicySimulationResult",
    "AwaitableGetPrincipalPolicySimulationResult",
    "get_principal_policy_simulation",
    "get_principal_policy_simulation_output",
]

@pulumi.output_type
class GetPrincipalPolicySimulationResult:
    def __init__(
        __self__,
        action_names=...,
        additional_policies_jsons=...,
        all_allowed=...,
        caller_arn=...,
        contexts=...,
        id=...,
        permissions_boundary_policies_jsons=...,
        policy_source_arn=...,
        resource_arns=...,
        resource_handling_option=...,
        resource_owner_account_id=...,
        resource_policy_json=...,
        results=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionNames")
    def action_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPoliciesJsons")
    def additional_policies_jsons(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allAllowed")
    def all_allowed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="callerArn")
    def caller_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def contexts(
        self,
    ) -> Optional[Sequence[outputs.GetPrincipalPolicySimulationContextResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundaryPoliciesJsons")
    def permissions_boundary_policies_jsons(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="policySourceArn")
    def policy_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceHandlingOption")
    def resource_handling_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwnerAccountId")
    def resource_owner_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicyJson")
    def resource_policy_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def results(self) -> Sequence[outputs.GetPrincipalPolicySimulationResultResult]: ...

class AwaitableGetPrincipalPolicySimulationResult(GetPrincipalPolicySimulationResult):
    def __await__(self): ...

def get_principal_policy_simulation(
    action_names: Optional[Sequence[_builtins.str]] = ...,
    additional_policies_jsons: Optional[Sequence[_builtins.str]] = ...,
    caller_arn: Optional[_builtins.str] = ...,
    contexts: Optional[
        Sequence[
            Union[
                GetPrincipalPolicySimulationContextArgs,
                GetPrincipalPolicySimulationContextArgsDict,
            ]
        ]
    ] = ...,
    permissions_boundary_policies_jsons: Optional[Sequence[_builtins.str]] = ...,
    policy_source_arn: Optional[_builtins.str] = ...,
    resource_arns: Optional[Sequence[_builtins.str]] = ...,
    resource_handling_option: Optional[_builtins.str] = ...,
    resource_owner_account_id: Optional[_builtins.str] = ...,
    resource_policy_json: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrincipalPolicySimulationResult: ...
def get_principal_policy_simulation_output(
    action_names: Optional[pulumi.Input[Sequence[_builtins.str]]] = ...,
    additional_policies_jsons: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    caller_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    contexts: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetPrincipalPolicySimulationContextArgs,
                        GetPrincipalPolicySimulationContextArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    permissions_boundary_policies_jsons: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    policy_source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_arns: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    resource_handling_option: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_owner_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_policy_json: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrincipalPolicySimulationResult]: ...
