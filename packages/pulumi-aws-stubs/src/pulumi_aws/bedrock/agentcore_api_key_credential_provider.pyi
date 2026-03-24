import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentcoreApiKeyCredentialProviderArgs", "AgentcoreApiKeyCredentialProvider"]

@pulumi.input_type
class AgentcoreApiKeyCredentialProviderArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWo")
    def api_key_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_wo.setter
    def api_key_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWoVersion")
    def api_key_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @api_key_wo_version.setter
    def api_key_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _AgentcoreApiKeyCredentialProviderState:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_secret_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentcoreApiKeyCredentialProviderApiKeySecretArnArgs]
                ]
            ]
        ] = ...,
        api_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        credential_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretArns")
    def api_key_secret_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AgentcoreApiKeyCredentialProviderApiKeySecretArnArgs]]
        ]
    ]: ...
    @api_key_secret_arns.setter
    def api_key_secret_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentcoreApiKeyCredentialProviderApiKeySecretArnArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWo")
    def api_key_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_wo.setter
    def api_key_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWoVersion")
    def api_key_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @api_key_wo_version.setter
    def api_key_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderArn")
    def credential_provider_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_provider_arn.setter
    def credential_provider_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class AgentcoreApiKeyCredentialProvider(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AgentcoreApiKeyCredentialProviderArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_secret_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AgentcoreApiKeyCredentialProviderApiKeySecretArnArgs,
                            AgentcoreApiKeyCredentialProviderApiKeySecretArnArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        api_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        credential_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AgentcoreApiKeyCredentialProvider: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretArns")
    def api_key_secret_arns(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.AgentcoreApiKeyCredentialProviderApiKeySecretArn]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWo")
    def api_key_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWoVersion")
    def api_key_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderArn")
    def credential_provider_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
