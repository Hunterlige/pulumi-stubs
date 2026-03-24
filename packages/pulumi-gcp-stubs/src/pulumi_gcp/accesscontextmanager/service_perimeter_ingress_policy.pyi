import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServicePerimeterIngressPolicyArgs", "ServicePerimeterIngressPolicy"]

@pulumi.input_type
class ServicePerimeterIngressPolicyArgs:
    def __init__(
        __self__,
        *,
        perimeter: pulumi.Input[_builtins.str],
        ingress_from: Optional[
            pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> pulumi.Input[_builtins.str]: ...
    @perimeter.setter
    def perimeter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]]: ...
    @ingress_to.setter
    def ingress_to(
        self, value: Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServicePerimeterIngressPolicyState:
    def __init__(
        __self__,
        *,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_from: Optional[
            pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]
        ] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]]: ...
    @ingress_from.setter
    def ingress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]]: ...
    @ingress_to.setter
    def ingress_to(
        self, value: Optional[pulumi.Input[ServicePerimeterIngressPolicyIngressToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perimeter.setter
    def perimeter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ServicePerimeterIngressPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ingress_from: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterIngressPolicyIngressFromArgs,
                    ServicePerimeterIngressPolicyIngressFromArgsDict,
                ]
            ]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterIngressPolicyIngressToArgs,
                    ServicePerimeterIngressPolicyIngressToArgsDict,
                ]
            ]
        ] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServicePerimeterIngressPolicyArgs,
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
        ingress_from: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterIngressPolicyIngressFromArgs,
                    ServicePerimeterIngressPolicyIngressFromArgsDict,
                ]
            ]
        ] = ...,
        ingress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterIngressPolicyIngressToArgs,
                    ServicePerimeterIngressPolicyIngressToArgsDict,
                ]
            ]
        ] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServicePerimeterIngressPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressFrom")
    def ingress_from(
        self,
    ) -> pulumi.Output[Optional[outputs.ServicePerimeterIngressPolicyIngressFrom]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressTo")
    def ingress_to(
        self,
    ) -> pulumi.Output[Optional[outputs.ServicePerimeterIngressPolicyIngressTo]]: ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
