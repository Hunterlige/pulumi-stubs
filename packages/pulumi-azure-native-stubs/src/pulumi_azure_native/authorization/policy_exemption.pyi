import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyExemptionArgs", "PolicyExemption"]

@pulumi.input_type
class PolicyExemptionArgs:
    def __init__(
        __self__,
        *,
        exemption_category: pulumi.Input[Union[_builtins.str, ExemptionCategory]],
        policy_assignment_id: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        assignment_scope_validation: Optional[
            pulumi.Input[Union[_builtins.str, AssignmentScopeValidation]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expires_on: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[Any] = ...,
        policy_definition_reference_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        policy_exemption_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceSelectorArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ExemptionCategory]]: ...
    @exemption_category.setter
    def exemption_category(
        self, value: pulumi.Input[Union[_builtins.str, ExemptionCategory]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_assignment_id.setter
    def policy_assignment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assignmentScopeValidation")
    def assignment_scope_validation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssignmentScopeValidation]]]: ...
    @assignment_scope_validation.setter
    def assignment_scope_validation(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AssignmentScopeValidation]]],
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
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policy_definition_reference_ids.setter
    def policy_definition_reference_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyExemptionName")
    def policy_exemption_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_exemption_name.setter
    def policy_exemption_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceSelectorArgs]]]]: ...
    @resource_selectors.setter
    def resource_selectors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceSelectorArgs]]]],
    ): ...

@pulumi.type_token("azure-native:authorization:PolicyExemption")
class PolicyExemption(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assignment_scope_validation: Optional[
            pulumi.Input[Union[_builtins.str, AssignmentScopeValidation]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        exemption_category: Optional[
            pulumi.Input[Union[_builtins.str, ExemptionCategory]]
        ] = ...,
        expires_on: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[Any] = ...,
        policy_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_definition_reference_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        policy_exemption_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ResourceSelectorArgs, ResourceSelectorArgsDict]]
                ]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyExemptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PolicyExemption: ...
    @_builtins.property
    @pulumi.getter(name="assignmentScopeValidation")
    def assignment_scope_validation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ResourceSelectorResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
