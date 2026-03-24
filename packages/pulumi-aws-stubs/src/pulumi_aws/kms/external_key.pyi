

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExternalKeyArgs', 'ExternalKey']
@pulumi.input_type
class ExternalKeyArgs:
    def __init__(__self__, *, bypass_policy_lockout_safety_check: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_material_base64: Optional[pulumi.Input[_builtins.str]] = ..., key_spec: Optional[pulumi.Input[_builtins.str]] = ..., key_usage: Optional[pulumi.Input[_builtins.str]] = ..., multi_region: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., valid_to: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_material_base64.setter
    def key_material_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_spec.setter
    def key_spec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_to.setter
    def valid_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ExternalKeyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., bypass_policy_lockout_safety_check: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expiration_model: Optional[pulumi.Input[_builtins.str]] = ..., key_material_base64: Optional[pulumi.Input[_builtins.str]] = ..., key_spec: Optional[pulumi.Input[_builtins.str]] = ..., key_state: Optional[pulumi.Input[_builtins.str]] = ..., key_usage: Optional[pulumi.Input[_builtins.str]] = ..., multi_region: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., valid_to: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationModel")
    def expiration_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_model.setter
    def expiration_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_material_base64.setter
    def key_material_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_spec.setter
    def key_spec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_state.setter
    def key_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_to.setter
    def valid_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:kms/externalKey:ExternalKey")
class ExternalKey(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bypass_policy_lockout_safety_check: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_material_base64: Optional[pulumi.Input[_builtins.str]] = ..., key_spec: Optional[pulumi.Input[_builtins.str]] = ..., key_usage: Optional[pulumi.Input[_builtins.str]] = ..., multi_region: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., valid_to: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ExternalKeyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bypass_policy_lockout_safety_check: Optional[pulumi.Input[_builtins.bool]] = ..., deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expiration_model: Optional[pulumi.Input[_builtins.str]] = ..., key_material_base64: Optional[pulumi.Input[_builtins.str]] = ..., key_spec: Optional[pulumi.Input[_builtins.str]] = ..., key_state: Optional[pulumi.Input[_builtins.str]] = ..., key_usage: Optional[pulumi.Input[_builtins.str]] = ..., multi_region: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., valid_to: Optional[pulumi.Input[_builtins.str]] = ...) -> ExternalKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationModel")
    def expiration_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


