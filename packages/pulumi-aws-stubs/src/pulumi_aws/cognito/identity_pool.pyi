import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IdentityPoolArgs", "IdentityPool"]

@pulumi.input_type
class IdentityPoolArgs:
    def __init__(
        __self__,
        *,
        identity_pool_name: pulumi.Input[_builtins.str],
        allow_classic_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_unauthenticated_identities: Optional[pulumi.Input[_builtins.bool]] = ...,
        cognito_identity_providers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]
            ]
        ] = ...,
        developer_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_login_providers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> pulumi.Input[_builtins.str]: ...
    @identity_pool_name.setter
    def identity_pool_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_classic_flow.setter
    def allow_classic_flow(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]]
    ]: ...
    @cognito_identity_providers.setter
    def cognito_identity_providers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_provider_name.setter
    def developer_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @openid_connect_provider_arns.setter
    def openid_connect_provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @saml_provider_arns.setter
    def saml_provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @supported_login_providers.setter
    def supported_login_providers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _IdentityPoolState:
    def __init__(
        __self__,
        *,
        allow_classic_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_unauthenticated_identities: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cognito_identity_providers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]
            ]
        ] = ...,
        developer_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_login_providers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_classic_flow.setter
    def allow_classic_flow(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]]
    ]: ...
    @cognito_identity_providers.setter
    def cognito_identity_providers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolCognitoIdentityProviderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_provider_name.setter
    def developer_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_pool_name.setter
    def identity_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @openid_connect_provider_arns.setter
    def openid_connect_provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @saml_provider_arns.setter
    def saml_provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @supported_login_providers.setter
    def supported_login_providers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:cognito/identityPool:IdentityPool")
class IdentityPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_classic_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_unauthenticated_identities: Optional[pulumi.Input[_builtins.bool]] = ...,
        cognito_identity_providers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IdentityPoolCognitoIdentityProviderArgs,
                            IdentityPoolCognitoIdentityProviderArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        developer_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_login_providers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IdentityPoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_classic_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_unauthenticated_identities: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cognito_identity_providers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IdentityPoolCognitoIdentityProviderArgs,
                            IdentityPoolCognitoIdentityProviderArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        developer_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_login_providers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> IdentityPool: ...
    @_builtins.property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.IdentityPoolCognitoIdentityProvider]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
