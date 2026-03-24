import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainSamlOptionsArgs", "DomainSamlOptions"]

@pulumi.input_type
class DomainSamlOptionsArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_options: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlOptions")
    def saml_options(
        self,
    ) -> Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]]: ...
    @saml_options.setter
    def saml_options(
        self, value: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]]
    ): ...

@pulumi.input_type
class _DomainSamlOptionsState:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_options: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlOptions")
    def saml_options(
        self,
    ) -> Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]]: ...
    @saml_options.setter
    def saml_options(
        self, value: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsArgs]]
    ): ...

@pulumi.type_token(...)
class DomainSamlOptions(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_options: Optional[
            pulumi.Input[
                Union[
                    DomainSamlOptionsSamlOptionsArgs,
                    DomainSamlOptionsSamlOptionsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainSamlOptionsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_options: Optional[
            pulumi.Input[
                Union[
                    DomainSamlOptionsSamlOptionsArgs,
                    DomainSamlOptionsSamlOptionsArgsDict,
                ]
            ]
        ] = ...,
    ) -> DomainSamlOptions: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samlOptions")
    def saml_options(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainSamlOptionsSamlOptions]]: ...
