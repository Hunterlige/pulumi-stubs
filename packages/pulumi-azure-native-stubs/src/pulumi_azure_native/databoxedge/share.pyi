import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ShareArgs", "Share"]

@pulumi.input_type
class ShareArgs:
    def __init__(
        __self__,
        *,
        access_protocol: pulumi.Input[Union[_builtins.str, ShareAccessProtocol]],
        device_name: pulumi.Input[_builtins.str],
        monitoring_status: pulumi.Input[Union[_builtins.str, MonitoringStatus]],
        resource_group_name: pulumi.Input[_builtins.str],
        share_status: pulumi.Input[Union[_builtins.str, ShareStatus]],
        azure_container_info: Optional[pulumi.Input[AzureContainerInfoArgs]] = ...,
        client_access_rights: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClientAccessRightArgs]]]
        ] = ...,
        data_policy: Optional[pulumi.Input[Union[_builtins.str, DataPolicy]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_details: Optional[pulumi.Input[RefreshDetailsArgs]] = ...,
        user_access_rights: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserAccessRightArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessProtocol")
    def access_protocol(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ShareAccessProtocol]]: ...
    @access_protocol.setter
    def access_protocol(
        self, value: pulumi.Input[Union[_builtins.str, ShareAccessProtocol]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, MonitoringStatus]]: ...
    @monitoring_status.setter
    def monitoring_status(
        self, value: pulumi.Input[Union[_builtins.str, MonitoringStatus]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> pulumi.Input[Union[_builtins.str, ShareStatus]]: ...
    @share_status.setter
    def share_status(self, value: pulumi.Input[Union[_builtins.str, ShareStatus]]): ...
    @_builtins.property
    @pulumi.getter(name="azureContainerInfo")
    def azure_container_info(
        self,
    ) -> Optional[pulumi.Input[AzureContainerInfoArgs]]: ...
    @azure_container_info.setter
    def azure_container_info(
        self, value: Optional[pulumi.Input[AzureContainerInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientAccessRights")
    def client_access_rights(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClientAccessRightArgs]]]]: ...
    @client_access_rights.setter
    def client_access_rights(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClientAccessRightArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataPolicy]]]: ...
    @data_policy.setter
    def data_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataPolicy]]]
    ): ...
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
    @pulumi.getter(name="refreshDetails")
    def refresh_details(self) -> Optional[pulumi.Input[RefreshDetailsArgs]]: ...
    @refresh_details.setter
    def refresh_details(self, value: Optional[pulumi.Input[RefreshDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userAccessRights")
    def user_access_rights(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserAccessRightArgs]]]]: ...
    @user_access_rights.setter
    def user_access_rights(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserAccessRightArgs]]]]
    ): ...

@pulumi.type_token("azure-native:databoxedge:Share")
class Share(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_protocol: Optional[
            pulumi.Input[Union[_builtins.str, ShareAccessProtocol]]
        ] = ...,
        azure_container_info: Optional[
            pulumi.Input[Union[AzureContainerInfoArgs, AzureContainerInfoArgsDict]]
        ] = ...,
        client_access_rights: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClientAccessRightArgs, ClientAccessRightArgsDict]
                    ]
                ]
            ]
        ] = ...,
        data_policy: Optional[pulumi.Input[Union[_builtins.str, DataPolicy]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_status: Optional[
            pulumi.Input[Union[_builtins.str, MonitoringStatus]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_details: Optional[
            pulumi.Input[Union[RefreshDetailsArgs, RefreshDetailsArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_status: Optional[pulumi.Input[Union[_builtins.str, ShareStatus]]] = ...,
        user_access_rights: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[UserAccessRightArgs, UserAccessRightArgsDict]]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ShareArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Share: ...
    @_builtins.property
    @pulumi.getter(name="accessProtocol")
    def access_protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureContainerInfo")
    def azure_container_info(
        self,
    ) -> pulumi.Output[Optional[outputs.AzureContainerInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="clientAccessRights")
    def client_access_rights(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ClientAccessRightResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshDetails")
    def refresh_details(
        self,
    ) -> pulumi.Output[Optional[outputs.RefreshDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="shareMappings")
    def share_mappings(
        self,
    ) -> pulumi.Output[Sequence[outputs.MountPointMapResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAccessRights")
    def user_access_rights(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UserAccessRightResponse]]]: ...
