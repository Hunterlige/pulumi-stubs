import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EncryptionSpecArgs", "EncryptionSpec"]

@pulumi.input_type
class EncryptionSpecArgs:
    def __init__(
        __self__,
        *,
        encryption_spec: pulumi.Input[EncryptionSpecEncryptionSpecArgs],
        location: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> pulumi.Input[EncryptionSpecEncryptionSpecArgs]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: pulumi.Input[EncryptionSpecEncryptionSpecArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EncryptionSpecState:
    def __init__(
        __self__,
        *,
        encryption_spec: Optional[pulumi.Input[EncryptionSpecEncryptionSpecArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> Optional[pulumi.Input[EncryptionSpecEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[EncryptionSpecEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:diagflow/encryptionSpec:EncryptionSpec")
class EncryptionSpec(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[
                    EncryptionSpecEncryptionSpecArgs,
                    EncryptionSpecEncryptionSpecArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EncryptionSpecArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[
                    EncryptionSpecEncryptionSpecArgs,
                    EncryptionSpecEncryptionSpecArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EncryptionSpec: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> pulumi.Output[outputs.EncryptionSpecEncryptionSpec]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
