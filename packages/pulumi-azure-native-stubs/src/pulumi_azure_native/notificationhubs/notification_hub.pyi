import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotificationHubArgs", "NotificationHub"]

@pulumi.input_type
class NotificationHubArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        adm_credential: Optional[pulumi.Input[AdmCredentialArgs]] = ...,
        apns_credential: Optional[pulumi.Input[ApnsCredentialArgs]] = ...,
        baidu_credential: Optional[pulumi.Input[BaiduCredentialArgs]] = ...,
        browser_credential: Optional[pulumi.Input[BrowserCredentialArgs]] = ...,
        fcm_v1_credential: Optional[pulumi.Input[FcmV1CredentialArgs]] = ...,
        gcm_credential: Optional[pulumi.Input[GcmCredentialArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mpns_credential: Optional[pulumi.Input[MpnsCredentialArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        wns_credential: Optional[pulumi.Input[WnsCredentialArgs]] = ...,
        xiaomi_credential: Optional[pulumi.Input[XiaomiCredentialArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional[pulumi.Input[AdmCredentialArgs]]: ...
    @adm_credential.setter
    def adm_credential(self, value: Optional[pulumi.Input[AdmCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional[pulumi.Input[ApnsCredentialArgs]]: ...
    @apns_credential.setter
    def apns_credential(self, value: Optional[pulumi.Input[ApnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional[pulumi.Input[BaiduCredentialArgs]]: ...
    @baidu_credential.setter
    def baidu_credential(self, value: Optional[pulumi.Input[BaiduCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="browserCredential")
    def browser_credential(self) -> Optional[pulumi.Input[BrowserCredentialArgs]]: ...
    @browser_credential.setter
    def browser_credential(
        self, value: Optional[pulumi.Input[BrowserCredentialArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(self) -> Optional[pulumi.Input[FcmV1CredentialArgs]]: ...
    @fcm_v1_credential.setter
    def fcm_v1_credential(self, value: Optional[pulumi.Input[FcmV1CredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional[pulumi.Input[GcmCredentialArgs]]: ...
    @gcm_credential.setter
    def gcm_credential(self, value: Optional[pulumi.Input[GcmCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional[pulumi.Input[MpnsCredentialArgs]]: ...
    @mpns_credential.setter
    def mpns_credential(self, value: Optional[pulumi.Input[MpnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationHubName")
    def notification_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_hub_name.setter
    def notification_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_ttl.setter
    def registration_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
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
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional[pulumi.Input[WnsCredentialArgs]]: ...
    @wns_credential.setter
    def wns_credential(self, value: Optional[pulumi.Input[WnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(self) -> Optional[pulumi.Input[XiaomiCredentialArgs]]: ...
    @xiaomi_credential.setter
    def xiaomi_credential(
        self, value: Optional[pulumi.Input[XiaomiCredentialArgs]]
    ): ...

@pulumi.type_token("azure-native:notificationhubs:NotificationHub")
class NotificationHub(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        adm_credential: Optional[
            pulumi.Input[Union[AdmCredentialArgs, AdmCredentialArgsDict]]
        ] = ...,
        apns_credential: Optional[
            pulumi.Input[Union[ApnsCredentialArgs, ApnsCredentialArgsDict]]
        ] = ...,
        baidu_credential: Optional[
            pulumi.Input[Union[BaiduCredentialArgs, BaiduCredentialArgsDict]]
        ] = ...,
        browser_credential: Optional[
            pulumi.Input[Union[BrowserCredentialArgs, BrowserCredentialArgsDict]]
        ] = ...,
        fcm_v1_credential: Optional[
            pulumi.Input[Union[FcmV1CredentialArgs, FcmV1CredentialArgsDict]]
        ] = ...,
        gcm_credential: Optional[
            pulumi.Input[Union[GcmCredentialArgs, GcmCredentialArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mpns_credential: Optional[
            pulumi.Input[Union[MpnsCredentialArgs, MpnsCredentialArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        wns_credential: Optional[
            pulumi.Input[Union[WnsCredentialArgs, WnsCredentialArgsDict]]
        ] = ...,
        xiaomi_credential: Optional[
            pulumi.Input[Union[XiaomiCredentialArgs, XiaomiCredentialArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotificationHubArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NotificationHub: ...
    @_builtins.property
    @pulumi.getter(name="admCredential")
    def adm_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.AdmCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.ApnsCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationRules")
    def authorization_rules(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.SharedAccessAuthorizationRulePropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.BaiduCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="browserCredential")
    def browser_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.BrowserCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dailyMaxActiveDevices")
    def daily_max_active_devices(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.FcmV1CredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.GcmCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.MpnsCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
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
    @pulumi.getter(name="wnsCredential")
    def wns_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.WnsCredentialResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.XiaomiCredentialResponse]]: ...
