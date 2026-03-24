import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServicePerimeterDryRunResourceArgs", "ServicePerimeterDryRunResource"]

@pulumi.input_type
class ServicePerimeterDryRunResourceArgs:
    def __init__(
        __self__,
        *,
        perimeter_name: pulumi.Input[_builtins.str],
        resource: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> pulumi.Input[_builtins.str]: ...
    @perimeter_name.setter
    def perimeter_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _ServicePerimeterDryRunResourceState:
    def __init__(
        __self__,
        *,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_policy_id.setter
    def access_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perimeter_name.setter
    def perimeter_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ServicePerimeterDryRunResource(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServicePerimeterDryRunResourceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServicePerimeterDryRunResource: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Output[_builtins.str]: ...
