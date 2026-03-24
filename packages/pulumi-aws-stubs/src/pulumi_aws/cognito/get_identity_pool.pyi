import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIdentityPoolResult",
    "AwaitableGetIdentityPoolResult",
    "get_identity_pool",
    "get_identity_pool_output",
]

@pulumi.output_type
class GetIdentityPoolResult:
    def __init__(
        __self__,
        allow_classic_flow=...,
        allow_unauthenticated_identities=...,
        arn=...,
        cognito_identity_providers=...,
        developer_provider_name=...,
        id=...,
        identity_pool_name=...,
        openid_connect_provider_arns=...,
        region=...,
        saml_provider_arns=...,
        supported_login_providers=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(
        self,
    ) -> Sequence[outputs.GetIdentityPoolCognitoIdentityProviderResult]: ...
    @_builtins.property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetIdentityPoolResult(GetIdentityPoolResult):
    def __await__(self): ...

def get_identity_pool(
    identity_pool_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIdentityPoolResult: ...
def get_identity_pool_output(
    identity_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIdentityPoolResult]: ...
