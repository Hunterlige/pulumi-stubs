import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NGroupArgs", "NGroup"]

@pulumi.input_type
class NGroupArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        container_group_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerGroupProfileStubArgs]]]
        ] = ...,
        elastic_profile: Optional[pulumi.Input[ElasticProfileArgs]] = ...,
        identity: Optional[pulumi.Input[NGroupIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        ngroups_name: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_profile: Optional[pulumi.Input[PlacementProfileArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        update_profile: Optional[pulumi.Input[UpdateProfileArgs]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerGroupProfiles")
    def container_group_profiles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerGroupProfileStubArgs]]]
    ]: ...
    @container_group_profiles.setter
    def container_group_profiles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerGroupProfileStubArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="elasticProfile")
    def elastic_profile(self) -> Optional[pulumi.Input[ElasticProfileArgs]]: ...
    @elastic_profile.setter
    def elastic_profile(self, value: Optional[pulumi.Input[ElasticProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[NGroupIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[NGroupIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ngroupsName")
    def ngroups_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ngroups_name.setter
    def ngroups_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> Optional[pulumi.Input[PlacementProfileArgs]]: ...
    @placement_profile.setter
    def placement_profile(
        self, value: Optional[pulumi.Input[PlacementProfileArgs]]
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
    @pulumi.getter(name="updateProfile")
    def update_profile(self) -> Optional[pulumi.Input[UpdateProfileArgs]]: ...
    @update_profile.setter
    def update_profile(self, value: Optional[pulumi.Input[UpdateProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:containerinstance:NGroup")
class NGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        container_group_profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ContainerGroupProfileStubArgs,
                            ContainerGroupProfileStubArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        elastic_profile: Optional[
            pulumi.Input[Union[ElasticProfileArgs, ElasticProfileArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[Union[NGroupIdentityArgs, NGroupIdentityArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        ngroups_name: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_profile: Optional[
            pulumi.Input[Union[PlacementProfileArgs, PlacementProfileArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        update_profile: Optional[
            pulumi.Input[Union[UpdateProfileArgs, UpdateProfileArgsDict]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerGroupProfiles")
    def container_group_profiles(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ContainerGroupProfileStubResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="elasticProfile")
    def elastic_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ElasticProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.NGroupIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="placementProfile")
    def placement_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.PlacementProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="updateProfile")
    def update_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.UpdateProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
