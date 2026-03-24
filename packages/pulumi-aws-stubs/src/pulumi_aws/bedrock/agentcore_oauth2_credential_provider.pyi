import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentcoreOauth2CredentialProviderArgs", "AgentcoreOauth2CredentialProvider"]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderArgs:
    def __init__(
        __self__,
        *,
        credential_provider_vendor: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth2_provider_config: Optional[
            pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderVendor")
    def credential_provider_vendor(self) -> pulumi.Input[_builtins.str]: ...
    @credential_provider_vendor.setter
    def credential_provider_vendor(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ProviderConfig")
    def oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
    ]: ...
    @oauth2_provider_config.setter
    def oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _AgentcoreOauth2CredentialProviderState:
    def __init__(
        __self__,
        *,
        client_secret_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentcoreOauth2CredentialProviderClientSecretArnArgs]
                ]
            ]
        ] = ...,
        credential_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_provider_vendor: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth2_provider_config: Optional[
            pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretArns")
    def client_secret_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AgentcoreOauth2CredentialProviderClientSecretArnArgs]]
        ]
    ]: ...
    @client_secret_arns.setter
    def client_secret_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentcoreOauth2CredentialProviderClientSecretArnArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderArn")
    def credential_provider_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_provider_arn.setter
    def credential_provider_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderVendor")
    def credential_provider_vendor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_provider_vendor.setter
    def credential_provider_vendor(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ProviderConfig")
    def oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
    ]: ...
    @oauth2_provider_config.setter
    def oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token(...)
class AgentcoreOauth2CredentialProvider(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        credential_provider_vendor: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth2_provider_config: Optional[
            pulumi.Input[
                Union[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs,
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentcoreOauth2CredentialProviderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        client_secret_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AgentcoreOauth2CredentialProviderClientSecretArnArgs,
                            AgentcoreOauth2CredentialProviderClientSecretArnArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        credential_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_provider_vendor: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth2_provider_config: Optional[
            pulumi.Input[
                Union[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs,
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AgentcoreOauth2CredentialProvider: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretArns")
    def client_secret_arns(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.AgentcoreOauth2CredentialProviderClientSecretArn]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderArn")
    def credential_provider_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderVendor")
    def credential_provider_vendor(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2ProviderConfig")
    def oauth2_provider_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
