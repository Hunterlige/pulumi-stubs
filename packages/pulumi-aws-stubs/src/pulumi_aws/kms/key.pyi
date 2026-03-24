import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyArgs", "Key"]

@pulumi.input_type
class KeyArgs:
    def __init__(
        __self__,
        *,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_key_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_master_key_spec: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_key_rotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_usage: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rotation_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        xks_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="customKeyStoreId")
    def custom_key_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_key_store_id.setter
    def custom_key_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_master_key_spec.setter
    def customer_master_key_spec(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_key_rotation.setter
    def enable_key_rotation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @_builtins.property
    @pulumi.getter(name="rotationPeriodInDays")
    def rotation_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rotation_period_in_days.setter
    def rotation_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="xksKeyId")
    def xks_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @xks_key_id.setter
    def xks_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KeyState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_key_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_master_key_spec: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_key_rotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_usage: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rotation_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        xks_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="customKeyStoreId")
    def custom_key_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_key_store_id.setter
    def custom_key_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_master_key_spec.setter
    def customer_master_key_spec(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_key_rotation.setter
    def enable_key_rotation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @_builtins.property
    @pulumi.getter(name="rotationPeriodInDays")
    def rotation_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rotation_period_in_days.setter
    def rotation_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="xksKeyId")
    def xks_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @xks_key_id.setter
    def xks_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:kms/key:Key")
class Key(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_key_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_master_key_spec: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_key_rotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_usage: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rotation_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        xks_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[KeyArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bypass_policy_lockout_safety_check: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_key_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_master_key_spec: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_key_rotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_usage: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rotation_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        xks_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Key: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="customKeyStoreId")
    def custom_key_store_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rotationPeriodInDays")
    def rotation_period_in_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="xksKeyId")
    def xks_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
