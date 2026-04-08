import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IoMAMPolicyByNameArgs", "IoMAMPolicyByName"]

@pulumi.input_type
class IoMAMPolicyByNameArgs:
    def __init__(
        __self__,
        *,
        friendly_name: pulumi.Input[_builtins.str],
        host_name: pulumi.Input[_builtins.str],
        access_recheck_offline_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        access_recheck_online_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        app_sharing_from_level: Optional[pulumi.Input[_builtins.str]] = ...,
        app_sharing_to_level: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        clipboard_sharing_level: Optional[pulumi.Input[_builtins.str]] = ...,
        data_backup: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        device_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        file_encryption_level: Optional[pulumi.Input[_builtins.str]] = ...,
        file_sharing_save_as: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_browser: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_wipe_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        pin: Optional[pulumi.Input[_builtins.str]] = ...,
        pin_num_retry: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        touch_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Input[_builtins.str]: ...
    @friendly_name.setter
    def friendly_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]: ...
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessRecheckOfflineTimeout")
    def access_recheck_offline_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_recheck_offline_timeout.setter
    def access_recheck_offline_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="accessRecheckOnlineTimeout")
    def access_recheck_online_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_recheck_online_timeout.setter
    def access_recheck_online_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appSharingFromLevel")
    def app_sharing_from_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_sharing_from_level.setter
    def app_sharing_from_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appSharingToLevel")
    def app_sharing_to_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_sharing_to_level.setter
    def app_sharing_to_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clipboardSharingLevel")
    def clipboard_sharing_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @clipboard_sharing_level.setter
    def clipboard_sharing_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataBackup")
    def data_backup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_backup.setter
    def data_backup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceCompliance")
    def device_compliance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_compliance.setter
    def device_compliance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileEncryptionLevel")
    def file_encryption_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_encryption_level.setter
    def file_encryption_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSharingSaveAs")
    def file_sharing_save_as(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_sharing_save_as.setter
    def file_sharing_save_as(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBrowser")
    def managed_browser(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_browser.setter
    def managed_browser(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="offlineWipeTimeout")
    def offline_wipe_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_wipe_timeout.setter
    def offline_wipe_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pin.setter
    def pin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pinNumRetry")
    def pin_num_retry(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pin_num_retry.setter
    def pin_num_retry(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="touchId")
    def touch_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @touch_id.setter
    def touch_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:intune:IoMAMPolicyByName")
class IoMAMPolicyByName(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_recheck_offline_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        access_recheck_online_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        app_sharing_from_level: Optional[pulumi.Input[_builtins.str]] = ...,
        app_sharing_to_level: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        clipboard_sharing_level: Optional[pulumi.Input[_builtins.str]] = ...,
        data_backup: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        device_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        file_encryption_level: Optional[pulumi.Input[_builtins.str]] = ...,
        file_sharing_save_as: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_browser: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_wipe_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        pin: Optional[pulumi.Input[_builtins.str]] = ...,
        pin_num_retry: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        touch_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IoMAMPolicyByNameArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> IoMAMPolicyByName: ...
    @_builtins.property
    @pulumi.getter(name="accessRecheckOfflineTimeout")
    def access_recheck_offline_timeout(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="accessRecheckOnlineTimeout")
    def access_recheck_online_timeout(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="appSharingFromLevel")
    def app_sharing_from_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="appSharingToLevel")
    def app_sharing_to_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clipboardSharingLevel")
    def clipboard_sharing_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataBackup")
    def data_backup(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deviceCompliance")
    def device_compliance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileEncryptionLevel")
    def file_encryption_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileSharingSaveAs")
    def file_sharing_save_as(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedBrowser")
    def managed_browser(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numOfApps")
    def num_of_apps(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="offlineWipeTimeout")
    def offline_wipe_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def pin(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pinNumRetry")
    def pin_num_retry(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="touchId")
    def touch_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
