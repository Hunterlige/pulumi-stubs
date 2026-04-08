import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecretSyncArgs", "SecretSync"]

@pulumi.input_type
class SecretSyncArgs:
    def __init__(
        __self__,
        *,
        kubernetes_secret_type: pulumi.Input[
            Union[_builtins.str, KubernetesSecretType]
        ],
        object_secret_mapping: pulumi.Input[
            Sequence[pulumi.Input[KubernetesSecretObjectMappingArgs]]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        secret_provider_class_name: pulumi.Input[_builtins.str],
        service_account_name: pulumi.Input[_builtins.str],
        extended_location: Optional[
            pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
        ] = ...,
        force_synchronization: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_sync_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSecretType")
    def kubernetes_secret_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, KubernetesSecretType]]: ...
    @kubernetes_secret_type.setter
    def kubernetes_secret_type(
        self, value: pulumi.Input[Union[_builtins.str, KubernetesSecretType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectSecretMapping")
    def object_secret_mapping(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[KubernetesSecretObjectMappingArgs]]]: ...
    @object_secret_mapping.setter
    def object_secret_mapping(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[KubernetesSecretObjectMappingArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretProviderClassName")
    def secret_provider_class_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_provider_class_name.setter
    def secret_provider_class_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_account_name.setter
    def service_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> Optional[
        pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
    ]: ...
    @extended_location.setter
    def extended_location(
        self,
        value: Optional[
            pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceSynchronization")
    def force_synchronization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_synchronization.setter
    def force_synchronization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretSyncName")
    def secret_sync_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_sync_name.setter
    def secret_sync_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:secretsynccontroller:SecretSync")
class SecretSync(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        extended_location: Optional[
            pulumi.Input[
                Union[
                    AzureResourceManagerCommonTypesExtendedLocationArgs,
                    AzureResourceManagerCommonTypesExtendedLocationArgsDict,
                ]
            ]
        ] = ...,
        force_synchronization: Optional[pulumi.Input[_builtins.str]] = ...,
        kubernetes_secret_type: Optional[
            pulumi.Input[Union[_builtins.str, KubernetesSecretType]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        object_secret_mapping: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KubernetesSecretObjectMappingArgs,
                            KubernetesSecretObjectMappingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_provider_class_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_sync_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecretSyncArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SecretSync: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureResourceManagerCommonTypesExtendedLocationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="forceSynchronization")
    def force_synchronization(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSecretType")
    def kubernetes_secret_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectSecretMapping")
    def object_secret_mapping(
        self,
    ) -> pulumi.Output[Sequence[outputs.KubernetesSecretObjectMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretProviderClassName")
    def secret_provider_class_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.SecretSyncStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
