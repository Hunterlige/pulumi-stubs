import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FhirServiceArgs", "FhirService"]

@pulumi.input_type
class FhirServiceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        acr_configuration: Optional[
            pulumi.Input[FhirServiceAcrConfigurationArgs]
        ] = ...,
        authentication_configuration: Optional[
            pulumi.Input[FhirServiceAuthenticationConfigurationArgs]
        ] = ...,
        cors_configuration: Optional[
            pulumi.Input[FhirServiceCorsConfigurationArgs]
        ] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        export_configuration: Optional[
            pulumi.Input[FhirServiceExportConfigurationArgs]
        ] = ...,
        fhir_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]] = ...,
        implementation_guides_configuration: Optional[
            pulumi.Input[ImplementationGuidesConfigurationArgs]
        ] = ...,
        import_configuration: Optional[
            pulumi.Input[FhirServiceImportConfigurationArgs]
        ] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, FhirServiceKind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_version_policy_configuration: Optional[
            pulumi.Input[ResourceVersionPolicyConfigurationArgs]
        ] = ...,
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
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(
        self,
    ) -> Optional[pulumi.Input[FhirServiceAcrConfigurationArgs]]: ...
    @acr_configuration.setter
    def acr_configuration(
        self, value: Optional[pulumi.Input[FhirServiceAcrConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[pulumi.Input[FhirServiceAuthenticationConfigurationArgs]]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self, value: Optional[pulumi.Input[FhirServiceAuthenticationConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> Optional[pulumi.Input[FhirServiceCorsConfigurationArgs]]: ...
    @cors_configuration.setter
    def cors_configuration(
        self, value: Optional[pulumi.Input[FhirServiceCorsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(
        self,
    ) -> Optional[pulumi.Input[FhirServiceExportConfigurationArgs]]: ...
    @export_configuration.setter
    def export_configuration(
        self, value: Optional[pulumi.Input[FhirServiceExportConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fhirServiceName")
    def fhir_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fhir_service_name.setter
    def fhir_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="implementationGuidesConfiguration")
    def implementation_guides_configuration(
        self,
    ) -> Optional[pulumi.Input[ImplementationGuidesConfigurationArgs]]: ...
    @implementation_guides_configuration.setter
    def implementation_guides_configuration(
        self, value: Optional[pulumi.Input[ImplementationGuidesConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(
        self,
    ) -> Optional[pulumi.Input[FhirServiceImportConfigurationArgs]]: ...
    @import_configuration.setter
    def import_configuration(
        self, value: Optional[pulumi.Input[FhirServiceImportConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, FhirServiceKind]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FhirServiceKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[ResourceVersionPolicyConfigurationArgs]]: ...
    @resource_version_policy_configuration.setter
    def resource_version_policy_configuration(
        self, value: Optional[pulumi.Input[ResourceVersionPolicyConfigurationArgs]]
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

@pulumi.type_token("azure-native:healthcareapis:FhirService")
class FhirService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        acr_configuration: Optional[
            pulumi.Input[
                Union[
                    FhirServiceAcrConfigurationArgs, FhirServiceAcrConfigurationArgsDict
                ]
            ]
        ] = ...,
        authentication_configuration: Optional[
            pulumi.Input[
                Union[
                    FhirServiceAuthenticationConfigurationArgs,
                    FhirServiceAuthenticationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        cors_configuration: Optional[
            pulumi.Input[
                Union[
                    FhirServiceCorsConfigurationArgs,
                    FhirServiceCorsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionArgs, EncryptionArgsDict]]
        ] = ...,
        export_configuration: Optional[
            pulumi.Input[
                Union[
                    FhirServiceExportConfigurationArgs,
                    FhirServiceExportConfigurationArgsDict,
                ]
            ]
        ] = ...,
        fhir_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    ServiceManagedIdentityIdentityArgs,
                    ServiceManagedIdentityIdentityArgsDict,
                ]
            ]
        ] = ...,
        implementation_guides_configuration: Optional[
            pulumi.Input[
                Union[
                    ImplementationGuidesConfigurationArgs,
                    ImplementationGuidesConfigurationArgsDict,
                ]
            ]
        ] = ...,
        import_configuration: Optional[
            pulumi.Input[
                Union[
                    FhirServiceImportConfigurationArgs,
                    FhirServiceImportConfigurationArgsDict,
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, FhirServiceKind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_version_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    ResourceVersionPolicyConfigurationArgs,
                    ResourceVersionPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FhirServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FhirService: ...
    @_builtins.property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirServiceAcrConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FhirServiceAuthenticationConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirServiceCorsConfigurationResponse]]: ...
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
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirServiceExportConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceManagedIdentityResponseIdentity]]: ...
    @_builtins.property
    @pulumi.getter(name="implementationGuidesConfiguration")
    def implementation_guides_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ImplementationGuidesConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirServiceImportConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ResourceVersionPolicyConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
