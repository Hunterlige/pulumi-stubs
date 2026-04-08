import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserSolutionArgs", "UserSolution"]

@pulumi.input_type
class UserSolutionArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        products: Optional[pulumi.Input[Sequence[pulumi.Input[ProductArgs]]]] = ...,
        solution_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def products(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProductArgs]]]]: ...
    @products.setter
    def products(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProductArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="solutionId")
    def solution_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @solution_id.setter
    def solution_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:marketplace:UserSolution")
class UserSolution(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        products: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[ProductArgs, ProductArgsDict]]]]
        ] = ...,
        solution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[UserSolutionArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> UserSolution: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def products(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProductResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
