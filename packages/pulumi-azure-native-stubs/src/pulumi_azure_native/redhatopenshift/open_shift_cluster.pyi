import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OpenShiftClusterArgs", "OpenShiftCluster"]

@pulumi.input_type
class OpenShiftClusterArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        apiserver_profile: Optional[pulumi.Input[APIServerProfileArgs]] = ...,
        cluster_profile: Optional[pulumi.Input[ClusterProfileArgs]] = ...,
        ingress_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[IngressProfileArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        master_profile: Optional[pulumi.Input[MasterProfileArgs]] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_principal_profile: Optional[
            pulumi.Input[ServicePrincipalProfileArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        worker_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerProfileArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiserverProfile")
    def apiserver_profile(self) -> Optional[pulumi.Input[APIServerProfileArgs]]: ...
    @apiserver_profile.setter
    def apiserver_profile(
        self, value: Optional[pulumi.Input[APIServerProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterProfile")
    def cluster_profile(self) -> Optional[pulumi.Input[ClusterProfileArgs]]: ...
    @cluster_profile.setter
    def cluster_profile(self, value: Optional[pulumi.Input[ClusterProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressProfiles")
    def ingress_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IngressProfileArgs]]]]: ...
    @ingress_profiles.setter
    def ingress_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IngressProfileArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterProfile")
    def master_profile(self) -> Optional[pulumi.Input[MasterProfileArgs]]: ...
    @master_profile.setter
    def master_profile(self, value: Optional[pulumi.Input[MasterProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(
        self,
    ) -> Optional[pulumi.Input[ServicePrincipalProfileArgs]]: ...
    @service_principal_profile.setter
    def service_principal_profile(
        self, value: Optional[pulumi.Input[ServicePrincipalProfileArgs]]
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
    @pulumi.getter(name="workerProfiles")
    def worker_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerProfileArgs]]]]: ...
    @worker_profiles.setter
    def worker_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerProfileArgs]]]]
    ): ...

@pulumi.type_token("azure-native:redhatopenshift:OpenShiftCluster")
class OpenShiftCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apiserver_profile: Optional[
            pulumi.Input[Union[APIServerProfileArgs, APIServerProfileArgsDict]]
        ] = ...,
        cluster_profile: Optional[
            pulumi.Input[Union[ClusterProfileArgs, ClusterProfileArgsDict]]
        ] = ...,
        ingress_profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[IngressProfileArgs, IngressProfileArgsDict]]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        master_profile: Optional[
            pulumi.Input[Union[MasterProfileArgs, MasterProfileArgsDict]]
        ] = ...,
        network_profile: Optional[
            pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        service_principal_profile: Optional[
            pulumi.Input[
                Union[ServicePrincipalProfileArgs, ServicePrincipalProfileArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        worker_profiles: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WorkerProfileArgs, WorkerProfileArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OpenShiftClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> OpenShiftCluster: ...
    @_builtins.property
    @pulumi.getter(name="apiserverProfile")
    def apiserver_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.APIServerProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterProfile")
    def cluster_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="consoleProfile")
    def console_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConsoleProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressProfiles")
    def ingress_profiles(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.IngressProfileResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterProfile")
    def master_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.MasterProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ServicePrincipalProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerProfiles")
    def worker_profiles(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WorkerProfileResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="workerProfilesStatus")
    def worker_profiles_status(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkerProfileResponse]]: ...
