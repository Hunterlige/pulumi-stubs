import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Hl7StoreIamPolicyArgs", "Hl7StoreIamPolicy"]

@pulumi.input_type
class Hl7StoreIamPolicyArgs:
    def __init__(
        __self__,
        *,
        hl7_v2_store_id: pulumi.Input[_builtins.str],
        policy_data: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @hl7_v2_store_id.setter
    def hl7_v2_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]: ...
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _Hl7StoreIamPolicyState:
    def __init__(
        __self__,
        *,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        hl7_v2_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hl7_v2_store_id.setter
    def hl7_v2_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:healthcare/hl7StoreIamPolicy:Hl7StoreIamPolicy")
class Hl7StoreIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        hl7_v2_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Hl7StoreIamPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        hl7_v2_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Hl7StoreIamPolicy: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]: ...
