import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectorArgs", "Connector"]

@pulumi.input_type
class ConnectorArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        auth_info: Optional[
            pulumi.Input[
                Union[
                    AccessKeyInfoBaseArgs,
                    EasyAuthMicrosoftEntraIDAuthInfoArgs,
                    SecretAuthInfoArgs,
                    ServicePrincipalCertificateAuthInfoArgs,
                    ServicePrincipalSecretAuthInfoArgs,
                    SystemAssignedIdentityAuthInfoArgs,
                    UserAccountAuthInfoArgs,
                    UserAssignedIdentityAuthInfoArgs,
                ]
            ]
        ] = ...,
        client_type: Optional[pulumi.Input[Union[_builtins.str, ClientType]]] = ...,
        configuration_info: Optional[pulumi.Input[ConfigurationInfoArgs]] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_solution: Optional[
            pulumi.Input[PublicNetworkSolutionArgs]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store: Optional[pulumi.Input[SecretStoreArgs]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_service: Optional[
            pulumi.Input[
                Union[
                    AzureResourceArgs,
                    ConfluentBootstrapServerArgs,
                    ConfluentSchemaRegistryArgs,
                    SelfHostedServerArgs,
                ]
            ]
        ] = ...,
        v_net_solution: Optional[pulumi.Input[VNetSolutionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authInfo")
    def auth_info(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AccessKeyInfoBaseArgs,
                EasyAuthMicrosoftEntraIDAuthInfoArgs,
                SecretAuthInfoArgs,
                ServicePrincipalCertificateAuthInfoArgs,
                ServicePrincipalSecretAuthInfoArgs,
                SystemAssignedIdentityAuthInfoArgs,
                UserAccountAuthInfoArgs,
                UserAssignedIdentityAuthInfoArgs,
            ]
        ]
    ]: ...
    @auth_info.setter
    def auth_info(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AccessKeyInfoBaseArgs,
                    EasyAuthMicrosoftEntraIDAuthInfoArgs,
                    SecretAuthInfoArgs,
                    ServicePrincipalCertificateAuthInfoArgs,
                    ServicePrincipalSecretAuthInfoArgs,
                    SystemAssignedIdentityAuthInfoArgs,
                    UserAccountAuthInfoArgs,
                    UserAssignedIdentityAuthInfoArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientType")
    def client_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClientType]]]: ...
    @client_type.setter
    def client_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ClientType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[pulumi.Input[ConfigurationInfoArgs]]: ...
    @configuration_info.setter
    def configuration_info(
        self, value: Optional[pulumi.Input[ConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(
        self,
    ) -> Optional[pulumi.Input[PublicNetworkSolutionArgs]]: ...
    @public_network_solution.setter
    def public_network_solution(
        self, value: Optional[pulumi.Input[PublicNetworkSolutionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input[SecretStoreArgs]]: ...
    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input[SecretStoreArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureResourceArgs,
                ConfluentBootstrapServerArgs,
                ConfluentSchemaRegistryArgs,
                SelfHostedServerArgs,
            ]
        ]
    ]: ...
    @target_service.setter
    def target_service(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureResourceArgs,
                    ConfluentBootstrapServerArgs,
                    ConfluentSchemaRegistryArgs,
                    SelfHostedServerArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> Optional[pulumi.Input[VNetSolutionArgs]]: ...
    @v_net_solution.setter
    def v_net_solution(self, value: Optional[pulumi.Input[VNetSolutionArgs]]): ...

@pulumi.type_token("azure-native:servicelinker:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auth_info: Optional[
            pulumi.Input[
                Union[
                    Union[AccessKeyInfoBaseArgs, AccessKeyInfoBaseArgsDict],
                    Union[
                        EasyAuthMicrosoftEntraIDAuthInfoArgs,
                        EasyAuthMicrosoftEntraIDAuthInfoArgsDict,
                    ],
                    Union[SecretAuthInfoArgs, SecretAuthInfoArgsDict],
                    Union[
                        ServicePrincipalCertificateAuthInfoArgs,
                        ServicePrincipalCertificateAuthInfoArgsDict,
                    ],
                    Union[
                        ServicePrincipalSecretAuthInfoArgs,
                        ServicePrincipalSecretAuthInfoArgsDict,
                    ],
                    Union[
                        SystemAssignedIdentityAuthInfoArgs,
                        SystemAssignedIdentityAuthInfoArgsDict,
                    ],
                    Union[UserAccountAuthInfoArgs, UserAccountAuthInfoArgsDict],
                    Union[
                        UserAssignedIdentityAuthInfoArgs,
                        UserAssignedIdentityAuthInfoArgsDict,
                    ],
                ]
            ]
        ] = ...,
        client_type: Optional[pulumi.Input[Union[_builtins.str, ClientType]]] = ...,
        configuration_info: Optional[
            pulumi.Input[Union[ConfigurationInfoArgs, ConfigurationInfoArgsDict]]
        ] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_solution: Optional[
            pulumi.Input[
                Union[PublicNetworkSolutionArgs, PublicNetworkSolutionArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store: Optional[
            pulumi.Input[Union[SecretStoreArgs, SecretStoreArgsDict]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_service: Optional[
            pulumi.Input[
                Union[
                    Union[AzureResourceArgs, AzureResourceArgsDict],
                    Union[
                        ConfluentBootstrapServerArgs, ConfluentBootstrapServerArgsDict
                    ],
                    Union[ConfluentSchemaRegistryArgs, ConfluentSchemaRegistryArgsDict],
                    Union[SelfHostedServerArgs, SelfHostedServerArgsDict],
                ]
            ]
        ] = ...,
        v_net_solution: Optional[
            pulumi.Input[Union[VNetSolutionArgs, VNetSolutionArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Connector: ...
    @_builtins.property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientType")
    def client_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(
        self,
    ) -> pulumi.Output[Optional[outputs.PublicNetworkSolutionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> pulumi.Output[Optional[outputs.SecretStoreResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(
        self,
    ) -> pulumi.Output[Optional[outputs.VNetSolutionResponse]]: ...
