import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationCustomPolicyRuleArgs", "OrganizationCustomPolicyRule"]

@pulumi.input_type
class OrganizationCustomPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        policy_runtime: pulumi.Input[_builtins.str],
        policy_text: pulumi.Input[_builtins.str],
        trigger_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        debug_log_delivery_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> pulumi.Input[_builtins.str]: ...
    @policy_runtime.setter
    def policy_runtime(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> pulumi.Input[_builtins.str]: ...
    @policy_text.setter
    def policy_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTypes")
    def trigger_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @trigger_types.setter
    def trigger_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="debugLogDeliveryAccounts")
    def debug_log_delivery_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @debug_log_delivery_accounts.setter
    def debug_log_delivery_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_accounts.setter
    def excluded_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id_scope.setter
    def resource_id_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types_scopes.setter
    def resource_types_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_key_scope.setter
    def tag_key_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_value_scope.setter
    def tag_value_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OrganizationCustomPolicyRuleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        debug_log_delivery_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_text: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="debugLogDeliveryAccounts")
    def debug_log_delivery_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @debug_log_delivery_accounts.setter
    def debug_log_delivery_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_accounts.setter
    def excluded_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_runtime.setter
    def policy_runtime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_text.setter
    def policy_text(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id_scope.setter
    def resource_id_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types_scopes.setter
    def resource_types_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_key_scope.setter
    def tag_key_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_value_scope.setter
    def tag_value_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTypes")
    def trigger_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @trigger_types.setter
    def trigger_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class OrganizationCustomPolicyRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        debug_log_delivery_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_text: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationCustomPolicyRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        debug_log_delivery_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        input_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_text: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> OrganizationCustomPolicyRule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="debugLogDeliveryAccounts")
    def debug_log_delivery_accounts(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="triggerTypes")
    def trigger_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
