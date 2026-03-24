import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyPolicyArgs", "KeyPolicy"]

@pulumi.input_type
class KeyPolicyArgs:
    def __init__(
        __self__,
        *,
        key_id: pulumi.Input[_builtins.str],
        policy: pulumi.Input[_builtins.str],
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KeyPolicyState:
    def __init__(
        __self__,
        *,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:kms/keyPolicy:KeyPolicy")
class KeyPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeyPolicy: ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
