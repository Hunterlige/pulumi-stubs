import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContainerAppArgs", "ContainerApp"]

@pulumi.input_type
class ContainerAppArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        configuration: Optional[pulumi.Input[ConfigurationArgs]] = ...,
        container_app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        patching_configuration: Optional[
            pulumi.Input[ContainerAppPatchingConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template: Optional[pulumi.Input[TemplateArgs]] = ...,
        workload_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[ConfigurationArgs]]: ...
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[ConfigurationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="containerAppName")
    def container_app_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_app_name.setter
    def container_app_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, Kind]]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, Kind]]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedEnvironmentId")
    def managed_environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_environment_id.setter
    def managed_environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="patchingConfiguration")
    def patching_configuration(
        self,
    ) -> Optional[pulumi.Input[ContainerAppPatchingConfigurationArgs]]: ...
    @patching_configuration.setter
    def patching_configuration(
        self, value: Optional[pulumi.Input[ContainerAppPatchingConfigurationArgs]]
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
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[TemplateArgs]]: ...
    @template.setter
    def template(self, value: Optional[pulumi.Input[TemplateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_profile_name.setter
    def workload_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:app:ContainerApp")
class ContainerApp(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration: Optional[
            pulumi.Input[Union[ConfigurationArgs, ConfigurationArgsDict]]
        ] = ...,
        container_app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        patching_configuration: Optional[
            pulumi.Input[
                Union[
                    ContainerAppPatchingConfigurationArgs,
                    ContainerAppPatchingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template: Optional[pulumi.Input[Union[TemplateArgs, TemplateArgsDict]]] = ...,
        workload_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContainerAppArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ContainerApp: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevisionName")
    def latest_ready_revision_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestRevisionFqdn")
    def latest_revision_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestRevisionName")
    def latest_revision_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedEnvironmentId")
    def managed_environment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="patchingConfiguration")
    def patching_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerAppResponsePatchingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runningStatus")
    def running_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[outputs.TemplateResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
