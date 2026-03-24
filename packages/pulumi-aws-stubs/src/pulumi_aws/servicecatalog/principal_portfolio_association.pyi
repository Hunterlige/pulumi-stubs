import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrincipalPortfolioAssociationArgs", "PrincipalPortfolioAssociation"]

@pulumi.input_type
class PrincipalPortfolioAssociationArgs:
    def __init__(
        __self__,
        *,
        portfolio_id: pulumi.Input[_builtins.str],
        principal_arn: pulumi.Input[_builtins.str],
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[_builtins.str]: ...
    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Input[_builtins.str]: ...
    @principal_arn.setter
    def principal_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_type.setter
    def principal_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PrincipalPortfolioAssociationState:
    def __init__(
        __self__,
        *,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        portfolio_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @portfolio_id.setter
    def portfolio_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_arn.setter
    def principal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_type.setter
    def principal_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PrincipalPortfolioAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        portfolio_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrincipalPortfolioAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        portfolio_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PrincipalPortfolioAssociation: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
