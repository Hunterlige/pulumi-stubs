import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IngressPolicyArgs", "IngressPolicy"]

@pulumi.input_type
class IngressPolicyArgs:
    def __init__(
        __self__,
        *,
        ingress_policy_name: pulumi.Input[_builtins.str],
        resource: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicyName")
    def ingress_policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @ingress_policy_name.setter
    def ingress_policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _IngressPolicyState:
    def __init__(
        __self__,
        *,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_policy_id.setter
    def access_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicyName")
    def ingress_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_policy_name.setter
    def ingress_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class IngressPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ingress_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IngressPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IngressPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPolicyName")
    def ingress_policy_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Output[_builtins.str]: ...
