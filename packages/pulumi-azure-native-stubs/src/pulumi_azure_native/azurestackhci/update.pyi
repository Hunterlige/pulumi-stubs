import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UpdateArgs", "Update"]

@pulumi.input_type
class UpdateArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_type: Optional[
            pulumi.Input[Union[_builtins.str, AvailabilityType]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_date: Optional[pulumi.Input[_builtins.str]] = ...,
        installed_date: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        min_sbe_version_required: Optional[pulumi.Input[_builtins.str]] = ...,
        notify_message: Optional[pulumi.Input[_builtins.str]] = ...,
        package_path: Optional[pulumi.Input[_builtins.str]] = ...,
        package_size_in_mb: Optional[pulumi.Input[_builtins.float]] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        prerequisites: Optional[
            pulumi.Input[Sequence[pulumi.Input[UpdatePrerequisiteArgs]]]
        ] = ...,
        progress_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        release_link: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...,
        update_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AvailabilityType]]]: ...
    @availability_type.setter
    def availability_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AvailabilityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_date.setter
    def health_check_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="installedDate")
    def installed_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @installed_date.setter
    def installed_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minSbeVersionRequired")
    def min_sbe_version_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_sbe_version_required.setter
    def min_sbe_version_required(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notifyMessage")
    def notify_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notify_message.setter
    def notify_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_path.setter
    def package_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageSizeInMb")
    def package_size_in_mb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @package_size_in_mb.setter
    def package_size_in_mb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_type.setter
    def package_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prerequisites(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UpdatePrerequisiteArgs]]]]: ...
    @prerequisites.setter
    def prerequisites(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[UpdatePrerequisiteArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress_percentage.setter
    def progress_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseLink")
    def release_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_link.setter
    def release_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): ...
    @_builtins.property
    @pulumi.getter(name="updateName")
    def update_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_name.setter
    def update_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:azurestackhci:Update")
class Update(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_type: Optional[
            pulumi.Input[Union[_builtins.str, AvailabilityType]]
        ] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_date: Optional[pulumi.Input[_builtins.str]] = ...,
        installed_date: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        min_sbe_version_required: Optional[pulumi.Input[_builtins.str]] = ...,
        notify_message: Optional[pulumi.Input[_builtins.str]] = ...,
        package_path: Optional[pulumi.Input[_builtins.str]] = ...,
        package_size_in_mb: Optional[pulumi.Input[_builtins.float]] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        prerequisites: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[UpdatePrerequisiteArgs, UpdatePrerequisiteArgsDict]
                    ]
                ]
            ]
        ] = ...,
        progress_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        release_link: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...,
        update_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UpdateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Update: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="installedDate")
    def installed_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="minSbeVersionRequired")
    def min_sbe_version_required(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notifyMessage")
    def notify_message(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="packageSizeInMb")
    def package_size_in_mb(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def prerequisites(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UpdatePrerequisiteResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="releaseLink")
    def release_link(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
