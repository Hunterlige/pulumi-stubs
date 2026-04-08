import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrefixListGlobalRulestackArgs", "PrefixListGlobalRulestack"]

@pulumi.input_type
class PrefixListGlobalRulestackArgs:
    def __init__(
        __self__,
        *,
        global_rulestack_name: pulumi.Input[_builtins.str],
        prefix_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        audit_comment: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalRulestackName")
    def global_rulestack_name(self) -> pulumi.Input[_builtins.str]: ...
    @global_rulestack_name.setter
    def global_rulestack_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @prefix_list.setter
    def prefix_list(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cloudngfw:PrefixListGlobalRulestack")
class PrefixListGlobalRulestack(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_comment: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrefixListGlobalRulestackArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PrefixListGlobalRulestack: ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
