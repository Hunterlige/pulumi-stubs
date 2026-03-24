import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResourcePolicyArgs", "ResourcePolicy"]

@pulumi.input_type
class ResourcePolicyArgs:
    def __init__(
        __self__,
        *,
        policy_document: pulumi.Input[_builtins.str],
        policy_name: pulumi.Input[_builtins.str],
        bypass_policy_lockout_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[_builtins.str]: ...
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @policy_name.setter
    def policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutCheck")
    def bypass_policy_lockout_check(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_policy_lockout_check.setter
    def bypass_policy_lockout_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyRevisionId")
    def policy_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_revision_id.setter
    def policy_revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ResourcePolicyState:
    def __init__(
        __self__,
        *,
        bypass_policy_lockout_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutCheck")
    def bypass_policy_lockout_check(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_policy_lockout_check.setter
    def bypass_policy_lockout_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyRevisionId")
    def policy_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_revision_id.setter
    def policy_revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:xray/resourcePolicy:ResourcePolicy")
class ResourcePolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bypass_policy_lockout_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResourcePolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bypass_policy_lockout_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ResourcePolicy: ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutCheck")
    def bypass_policy_lockout_check(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyRevisionId")
    def policy_revision_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
