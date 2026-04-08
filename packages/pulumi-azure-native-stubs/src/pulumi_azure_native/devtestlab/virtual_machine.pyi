import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineArgs", "VirtualMachine"]

@pulumi.input_type
class VirtualMachineArgs:
    def __init__(
        __self__,
        *,
        lab_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        allow_claim: Optional[pulumi.Input[_builtins.bool]] = ...,
        artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
        ] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]
        ] = ...,
        disallow_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_date: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_image_reference: Optional[
            pulumi.Input[GalleryImageReferenceArgs]
        ] = ...,
        is_authentication_with_ssh_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        lab_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface: Optional[pulumi.Input[NetworkInterfacePropertiesArgs]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
        ] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[_builtins.str]: ...
    @lab_name.setter
    def lab_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_claim.setter
    def allow_claim(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
    ]: ...
    @artifacts.setter
    def artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_image_id.setter
    def custom_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]]: ...
    @data_disk_parameters.setter
    def data_disk_parameters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disallow_public_ip_address.setter
    def disallow_public_ip_address(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(
        self,
    ) -> Optional[pulumi.Input[GalleryImageReferenceArgs]]: ...
    @gallery_image_reference.setter
    def gallery_image_reference(
        self, value: Optional[pulumi.Input[GalleryImageReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_authentication_with_ssh_key.setter
    def is_authentication_with_ssh_key(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_subnet_name.setter
    def lab_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_virtual_network_id.setter
    def lab_virtual_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(
        self,
    ) -> Optional[pulumi.Input[NetworkInterfacePropertiesArgs]]: ...
    @network_interface.setter
    def network_interface(
        self, value: Optional[pulumi.Input[NetworkInterfacePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_object_id.setter
    def owner_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_user_principal_name.setter
    def owner_user_principal_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plan_id.setter
    def plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
    ]: ...
    @schedule_parameters.setter
    def schedule_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssh_key.setter
    def ssh_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:devtestlab:VirtualMachine")
class VirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_claim: Optional[pulumi.Input[_builtins.bool]] = ...,
        artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ArtifactInstallPropertiesArgs,
                            ArtifactInstallPropertiesArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DataDiskPropertiesArgs, DataDiskPropertiesArgsDict]
                    ]
                ]
            ]
        ] = ...,
        disallow_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_date: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_image_reference: Optional[
            pulumi.Input[
                Union[GalleryImageReferenceArgs, GalleryImageReferenceArgsDict]
            ]
        ] = ...,
        is_authentication_with_ssh_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface: Optional[
            pulumi.Input[
                Union[
                    NetworkInterfacePropertiesArgs, NetworkInterfacePropertiesArgsDict
                ]
            ]
        ] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ScheduleCreationParameterArgs,
                            ScheduleCreationParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachine: ...
    @_builtins.property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="applicableSchedule")
    def applicable_schedule(
        self,
    ) -> pulumi.Output[outputs.ApplicableScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="artifactDeploymentStatus")
    def artifact_deployment_status(
        self,
    ) -> pulumi.Output[outputs.ArtifactDeploymentStatusPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ArtifactInstallPropertiesResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeVm")
    def compute_vm(self) -> pulumi.Output[outputs.ComputeVmPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DataDiskPropertiesResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(
        self,
    ) -> pulumi.Output[Optional[outputs.GalleryImageReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastKnownPowerState")
    def last_known_power_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkInterfacePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ScheduleCreationParameterResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineCreationSource")
    def virtual_machine_creation_source(self) -> pulumi.Output[_builtins.str]: ...
