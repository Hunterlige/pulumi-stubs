import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegistryPolicyArgs", "RegistryPolicy"]

@pulumi.input_type
class RegistryPolicyArgs:
    def __init__(
        __self__,
        *,
        policy: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RegistryPolicyState:
    def __init__(
        __self__,
        *,
        policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]: ...
    @policy.setter
    def policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ecr/registryPolicy:RegistryPolicy")
class RegistryPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy: Optional[
            pulumi.Input[
                Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegistryPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy: Optional[
            pulumi.Input[
                Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RegistryPolicy: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
