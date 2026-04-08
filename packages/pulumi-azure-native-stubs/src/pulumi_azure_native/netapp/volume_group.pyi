import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VolumeGroupArgs", "VolumeGroup"]

@pulumi.input_type
class VolumeGroupArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        group_meta_data: Optional[pulumi.Input[VolumeGroupMetaDataArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeGroupVolumePropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(self) -> Optional[pulumi.Input[VolumeGroupMetaDataArgs]]: ...
    @group_meta_data.setter
    def group_meta_data(
        self, value: Optional[pulumi.Input[VolumeGroupMetaDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_group_name.setter
    def volume_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VolumeGroupVolumePropertiesArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeGroupVolumePropertiesArgs]]]
        ],
    ): ...

@pulumi.type_token("azure-native:netapp:VolumeGroup")
class VolumeGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        group_meta_data: Optional[
            pulumi.Input[Union[VolumeGroupMetaDataArgs, VolumeGroupMetaDataArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VolumeGroupVolumePropertiesArgs,
                            VolumeGroupVolumePropertiesArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VolumeGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VolumeGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(
        self,
    ) -> pulumi.Output[Optional[outputs.VolumeGroupMetaDataResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.VolumeGroupVolumePropertiesResponse]]
    ]: ...
