import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentcoreGatewayTargetArgs", "AgentcoreGatewayTarget"]

@pulumi.input_type
class AgentcoreGatewayTargetArgs:
    def __init__(
        __self__,
        *,
        gateway_identifier: pulumi.Input[_builtins.str],
        target_configuration: pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationArgs
        ],
        credential_provider_configuration: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_configuration: Optional[
            pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIdentifier")
    def gateway_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @gateway_identifier.setter
    def gateway_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(
        self,
    ) -> pulumi.Input[AgentcoreGatewayTargetTargetConfigurationArgs]: ...
    @target_configuration.setter
    def target_configuration(
        self, value: pulumi.Input[AgentcoreGatewayTargetTargetConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderConfiguration")
    def credential_provider_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
    ]: ...
    @credential_provider_configuration.setter
    def credential_provider_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]]: ...
    @metadata_configuration.setter
    def metadata_configuration(
        self,
        value: Optional[pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]],
    ): ...
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
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _AgentcoreGatewayTargetState:
    def __init__(
        __self__,
        *,
        credential_provider_configuration: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_configuration: Optional[
            pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_configuration: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationArgs]
        ] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderConfiguration")
    def credential_provider_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
    ]: ...
    @credential_provider_configuration.setter
    def credential_provider_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIdentifier")
    def gateway_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_identifier.setter
    def gateway_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]]: ...
    @metadata_configuration.setter
    def metadata_configuration(
        self,
        value: Optional[pulumi.Input[AgentcoreGatewayTargetMetadataConfigurationArgs]],
    ): ...
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
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetTargetConfigurationArgs]]: ...
    @target_configuration.setter
    def target_configuration(
        self,
        value: Optional[pulumi.Input[AgentcoreGatewayTargetTargetConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AgentcoreGatewayTargetTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class AgentcoreGatewayTarget(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        credential_provider_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetCredentialProviderConfigurationArgs,
                    AgentcoreGatewayTargetCredentialProviderConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetMetadataConfigurationArgs,
                    AgentcoreGatewayTargetMetadataConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetTargetConfigurationArgs,
                    AgentcoreGatewayTargetTargetConfigurationArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetTimeoutsArgs,
                    AgentcoreGatewayTargetTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentcoreGatewayTargetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        credential_provider_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetCredentialProviderConfigurationArgs,
                    AgentcoreGatewayTargetCredentialProviderConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetMetadataConfigurationArgs,
                    AgentcoreGatewayTargetMetadataConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetTargetConfigurationArgs,
                    AgentcoreGatewayTargetTargetConfigurationArgsDict,
                ]
            ]
        ] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AgentcoreGatewayTargetTimeoutsArgs,
                    AgentcoreGatewayTargetTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> AgentcoreGatewayTarget: ...
    @_builtins.property
    @pulumi.getter(name="credentialProviderConfiguration")
    def credential_provider_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AgentcoreGatewayTargetCredentialProviderConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIdentifier")
    def gateway_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AgentcoreGatewayTargetMetadataConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(
        self,
    ) -> pulumi.Output[outputs.AgentcoreGatewayTargetTargetConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentcoreGatewayTargetTimeouts]]: ...
