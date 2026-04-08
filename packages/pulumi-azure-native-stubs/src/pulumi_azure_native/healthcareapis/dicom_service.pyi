import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DicomServiceArgs", "DicomService"]

@pulumi.input_type
class DicomServiceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        cors_configuration: Optional[pulumi.Input[CorsConfigurationArgs]] = ...,
        dicom_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_data_partitions: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        identity: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_configuration: Optional[pulumi.Input[StorageConfigurationArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[pulumi.Input[CorsConfigurationArgs]]: ...
    @cors_configuration.setter
    def cors_configuration(
        self, value: Optional[pulumi.Input[CorsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dicomServiceName")
    def dicom_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dicom_service_name.setter
    def dicom_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDataPartitions")
    def enable_data_partitions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_data_partitions.setter
    def enable_data_partitions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> Optional[pulumi.Input[StorageConfigurationArgs]]: ...
    @storage_configuration.setter
    def storage_configuration(
        self, value: Optional[pulumi.Input[StorageConfigurationArgs]]
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

@pulumi.type_token("azure-native:healthcareapis:DicomService")
class DicomService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cors_configuration: Optional[
            pulumi.Input[Union[CorsConfigurationArgs, CorsConfigurationArgsDict]]
        ] = ...,
        dicom_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_data_partitions: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionArgs, EncryptionArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    ServiceManagedIdentityIdentityArgs,
                    ServiceManagedIdentityIdentityArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_configuration: Optional[
            pulumi.Input[Union[StorageConfigurationArgs, StorageConfigurationArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DicomServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DicomService: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.DicomServiceAuthenticationConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.CorsConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDataPartitions")
    def enable_data_partitions(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[outputs.EncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventState")
    def event_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceManagedIdentityResponseIdentity]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.StorageConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
