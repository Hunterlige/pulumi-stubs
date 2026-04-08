import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessKeyInfoBaseArgs",
    "AccessKeyInfoBaseArgsDict",
    "AzureKeyVaultPropertiesArgs",
    "AzureKeyVaultPropertiesArgsDict",
    "AzureResourceArgs",
    "AzureResourceArgsDict",
    "ConfigurationInfoArgs",
    "ConfigurationInfoArgsDict",
    "ConfigurationStoreArgs",
    "ConfigurationStoreArgsDict",
    "ConfluentBootstrapServerArgs",
    "ConfluentBootstrapServerArgsDict",
    "ConfluentSchemaRegistryArgs",
    "ConfluentSchemaRegistryArgsDict",
    "CreateOrUpdateDryrunParametersArgs",
    "CreateOrUpdateDryrunParametersArgsDict",
    "DaprMetadataArgs",
    "DaprMetadataArgsDict",
    "DaprPropertiesArgs",
    "DaprPropertiesArgsDict",
    "EasyAuthMicrosoftEntraIDAuthInfoArgs",
    "EasyAuthMicrosoftEntraIDAuthInfoArgsDict",
    "FirewallRulesArgs",
    "FirewallRulesArgsDict",
    "KeyVaultSecretReferenceSecretInfoArgs",
    "KeyVaultSecretReferenceSecretInfoArgsDict",
    "KeyVaultSecretUriSecretInfoArgs",
    "KeyVaultSecretUriSecretInfoArgsDict",
    "PublicNetworkSolutionArgs",
    "PublicNetworkSolutionArgsDict",
    "SecretAuthInfoArgs",
    "SecretAuthInfoArgsDict",
    "SecretStoreArgs",
    "SecretStoreArgsDict",
    "SelfHostedServerArgs",
    "SelfHostedServerArgsDict",
    "ServicePrincipalCertificateAuthInfoArgs",
    "ServicePrincipalCertificateAuthInfoArgsDict",
    "ServicePrincipalSecretAuthInfoArgs",
    "ServicePrincipalSecretAuthInfoArgsDict",
    "SystemAssignedIdentityAuthInfoArgs",
    "SystemAssignedIdentityAuthInfoArgsDict",
    "UserAccountAuthInfoArgs",
    "UserAccountAuthInfoArgsDict",
    "UserAssignedIdentityAuthInfoArgs",
    "UserAssignedIdentityAuthInfoArgsDict",
    "VNetSolutionArgs",
    "VNetSolutionArgsDict",
    "ValueSecretInfoArgs",
    "ValueSecretInfoArgsDict",
]

class AccessKeyInfoBaseArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    permissions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessKeyPermissions]]]]
    ]

@pulumi.input_type
class AccessKeyInfoBaseArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        permissions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AccessKeyPermissions]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessKeyPermissions]]]]
    ]: ...
    @permissions.setter
    def permissions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AccessKeyPermissions]]]
            ]
        ],
    ): ...

class AzureKeyVaultPropertiesArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    connect_as_kubernetes_csi_driver: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AzureKeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        connect_as_kubernetes_csi_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectAsKubernetesCsiDriver")
    def connect_as_kubernetes_csi_driver(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @connect_as_kubernetes_csi_driver.setter
    def connect_as_kubernetes_csi_driver(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AzureResourceArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    resource_properties: NotRequired[pulumi.Input[AzureKeyVaultPropertiesArgsDict]]

@pulumi.input_type
class AzureResourceArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_properties: Optional[pulumi.Input[AzureKeyVaultPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceProperties")
    def resource_properties(
        self,
    ) -> Optional[pulumi.Input[AzureKeyVaultPropertiesArgs]]: ...
    @resource_properties.setter
    def resource_properties(
        self, value: Optional[pulumi.Input[AzureKeyVaultPropertiesArgs]]
    ): ...

class ConfigurationInfoArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, ActionType]]]
    additional_configurations: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    additional_connection_string_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    configuration_store: NotRequired[pulumi.Input[ConfigurationStoreArgsDict]]
    customized_keys: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    dapr_properties: NotRequired[pulumi.Input[DaprPropertiesArgsDict]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]

@pulumi.input_type
class ConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, ActionType]]] = ...,
        additional_configurations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_connection_string_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        configuration_store: Optional[pulumi.Input[ConfigurationStoreArgs]] = ...,
        customized_keys: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        dapr_properties: Optional[pulumi.Input[DaprPropertiesArgs]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionType]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_configurations.setter
    def additional_configurations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalConnectionStringProperties")
    def additional_connection_string_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_connection_string_properties.setter
    def additional_connection_string_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configurationStore")
    def configuration_store(self) -> Optional[pulumi.Input[ConfigurationStoreArgs]]: ...
    @configuration_store.setter
    def configuration_store(
        self, value: Optional[pulumi.Input[ConfigurationStoreArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedKeys")
    def customized_keys(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @customized_keys.setter
    def customized_keys(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daprProperties")
    def dapr_properties(self) -> Optional[pulumi.Input[DaprPropertiesArgs]]: ...
    @dapr_properties.setter
    def dapr_properties(self, value: Optional[pulumi.Input[DaprPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...

class ConfigurationStoreArgsDict(TypedDict):
    app_configuration_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationStoreArgs:
    def __init__(
        __self__, *, app_configuration_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appConfigurationId")
    def app_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_configuration_id.setter
    def app_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfluentBootstrapServerArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfluentBootstrapServerArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfluentSchemaRegistryArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfluentSchemaRegistryArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CreateOrUpdateDryrunParametersArgsDict(TypedDict):
    action_name: pulumi.Input[_builtins.str]
    auth_info: NotRequired[
        pulumi.Input[
            Union[
                AccessKeyInfoBaseArgsDict,
                EasyAuthMicrosoftEntraIDAuthInfoArgsDict,
                SecretAuthInfoArgsDict,
                ServicePrincipalCertificateAuthInfoArgsDict,
                ServicePrincipalSecretAuthInfoArgsDict,
                SystemAssignedIdentityAuthInfoArgsDict,
                UserAccountAuthInfoArgsDict,
                UserAssignedIdentityAuthInfoArgsDict,
            ]
        ]
    ]
    client_type: NotRequired[pulumi.Input[Union[_builtins.str, ClientType]]]
    configuration_info: NotRequired[pulumi.Input[ConfigurationInfoArgsDict]]
    public_network_solution: NotRequired[pulumi.Input[PublicNetworkSolutionArgsDict]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    secret_store: NotRequired[pulumi.Input[SecretStoreArgsDict]]
    target_service: NotRequired[
        pulumi.Input[
            Union[
                AzureResourceArgsDict,
                ConfluentBootstrapServerArgsDict,
                ConfluentSchemaRegistryArgsDict,
                SelfHostedServerArgsDict,
            ]
        ]
    ]
    v_net_solution: NotRequired[pulumi.Input[VNetSolutionArgsDict]]

@pulumi.input_type
class CreateOrUpdateDryrunParametersArgs:
    def __init__(
        __self__,
        *,
        action_name: pulumi.Input[_builtins.str],
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
        public_network_solution: Optional[
            pulumi.Input[PublicNetworkSolutionArgs]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_store: Optional[pulumi.Input[SecretStoreArgs]] = ...,
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
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Input[_builtins.str]: ...
    @action_name.setter
    def action_name(self, value: pulumi.Input[_builtins.str]): ...
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

class DaprMetadataArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[Union[_builtins.str, DaprMetadataRequired]]]
    secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DaprMetadataArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[
            pulumi.Input[Union[_builtins.str, DaprMetadataRequired]]
        ] = ...,
        secret_ref: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DaprMetadataRequired]]]: ...
    @required.setter
    def required(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DaprMetadataRequired]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_ref.setter
    def secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DaprPropertiesArgsDict(TypedDict):
    component_type: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgsDict]]]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_store_component: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DaprPropertiesArgs:
    def __init__(
        __self__,
        *,
        component_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]
        ] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        secret_store_component: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreComponent")
    def secret_store_component(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_store_component.setter
    def secret_store_component(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EasyAuthMicrosoftEntraIDAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    secret: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EasyAuthMicrosoftEntraIDAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallRulesArgsDict(TypedDict):
    azure_services: NotRequired[pulumi.Input[Union[_builtins.str, AllowType]]]
    caller_client_ip: NotRequired[pulumi.Input[Union[_builtins.str, AllowType]]]
    ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FirewallRulesArgs:
    def __init__(
        __self__,
        *,
        azure_services: Optional[pulumi.Input[Union[_builtins.str, AllowType]]] = ...,
        caller_client_ip: Optional[pulumi.Input[Union[_builtins.str, AllowType]]] = ...,
        ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureServices")
    def azure_services(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AllowType]]]: ...
    @azure_services.setter
    def azure_services(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AllowType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="callerClientIP")
    def caller_client_ip(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AllowType]]]: ...
    @caller_client_ip.setter
    def caller_client_ip(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AllowType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_ranges.setter
    def ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KeyVaultSecretReferenceSecretInfoArgsDict(TypedDict):
    secret_type: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultSecretReferenceSecretInfoArgs:
    def __init__(
        __self__,
        *,
        secret_type: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Input[_builtins.str]: ...
    @secret_type.setter
    def secret_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultSecretUriSecretInfoArgsDict(TypedDict):
    secret_type: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultSecretUriSecretInfoArgs:
    def __init__(
        __self__,
        *,
        secret_type: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Input[_builtins.str]: ...
    @secret_type.setter
    def secret_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PublicNetworkSolutionArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, ActionType]]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    firewall_rules: NotRequired[pulumi.Input[FirewallRulesArgsDict]]

@pulumi.input_type
class PublicNetworkSolutionArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, ActionType]]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        firewall_rules: Optional[pulumi.Input[FirewallRulesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionType]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[pulumi.Input[FirewallRulesArgs]]: ...
    @firewall_rules.setter
    def firewall_rules(self, value: Optional[pulumi.Input[FirewallRulesArgs]]): ...

class SecretAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    secret_info: NotRequired[
        pulumi.Input[
            Union[
                KeyVaultSecretReferenceSecretInfoArgsDict,
                KeyVaultSecretUriSecretInfoArgsDict,
                ValueSecretInfoArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class SecretAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_info: Optional[
            pulumi.Input[
                Union[
                    KeyVaultSecretReferenceSecretInfoArgs,
                    KeyVaultSecretUriSecretInfoArgs,
                    ValueSecretInfoArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretInfo")
    def secret_info(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                KeyVaultSecretReferenceSecretInfoArgs,
                KeyVaultSecretUriSecretInfoArgs,
                ValueSecretInfoArgs,
            ]
        ]
    ]: ...
    @secret_info.setter
    def secret_info(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    KeyVaultSecretReferenceSecretInfoArgs,
                    KeyVaultSecretUriSecretInfoArgs,
                    ValueSecretInfoArgs,
                ]
            ]
        ],
    ): ...

class SecretStoreArgsDict(TypedDict):
    key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_secret_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretStoreArgs:
    def __init__(
        __self__,
        *,
        key_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_secret_name.setter
    def key_vault_secret_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SelfHostedServerArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SelfHostedServerArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePrincipalCertificateAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    certificate: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    principal_id: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServicePrincipalCertificateAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        certificate: pulumi.Input[_builtins.str],
        client_id: pulumi.Input[_builtins.str],
        principal_id: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[_builtins.str]: ...
    @certificate.setter
    def certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServicePrincipalSecretAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    principal_id: pulumi.Input[_builtins.str]
    secret: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePrincipalSecretAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        client_id: pulumi.Input[_builtins.str],
        principal_id: pulumi.Input[_builtins.str],
        secret: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SystemAssignedIdentityAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SystemAssignedIdentityAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAccountAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAccountAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAssignedIdentityAuthInfoArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    auth_mode: NotRequired[pulumi.Input[Union[_builtins.str, AuthMode]]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityAuthInfoArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        auth_mode: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VNetSolutionArgsDict(TypedDict):
    delete_or_update_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
    ]
    type: NotRequired[pulumi.Input[Union[_builtins.str, VNetSolutionType]]]

@pulumi.input_type
class VNetSolutionArgs:
    def __init__(
        __self__,
        *,
        delete_or_update_behavior: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, VNetSolutionType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOrUpdateBehavior")
    def delete_or_update_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]]: ...
    @delete_or_update_behavior.setter
    def delete_or_update_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DeleteOrUpdateBehavior]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VNetSolutionType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VNetSolutionType]]]
    ): ...

class ValueSecretInfoArgsDict(TypedDict):
    secret_type: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ValueSecretInfoArgs:
    def __init__(
        __self__,
        *,
        secret_type: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Input[_builtins.str]: ...
    @secret_type.setter
    def secret_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
