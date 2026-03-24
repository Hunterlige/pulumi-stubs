

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIoMAMPolicyByNameResult', 'AwaitableGetIoMAMPolicyByNameResult', 'get_io_mam_policy_by_name', 'get_io_mam_policy_by_name_output']
@pulumi.output_type
class GetIoMAMPolicyByNameResult:
    
    def __init__(__self__, access_recheck_offline_timeout=..., access_recheck_online_timeout=..., app_sharing_from_level=..., app_sharing_to_level=..., authentication=..., azure_api_version=..., clipboard_sharing_level=..., data_backup=..., description=..., device_compliance=..., file_encryption_level=..., file_sharing_save_as=..., friendly_name=..., group_status=..., id=..., last_modified_time=..., location=..., managed_browser=..., name=..., num_of_apps=..., offline_wipe_timeout=..., pin=..., pin_num_retry=..., tags=..., touch_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRecheckOfflineTimeout")
    def access_recheck_offline_timeout(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRecheckOnlineTimeout")
    def access_recheck_online_timeout(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSharingFromLevel")
    def app_sharing_from_level(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSharingToLevel")
    def app_sharing_to_level(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clipboardSharingLevel")
    def clipboard_sharing_level(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataBackup")
    def data_backup(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceCompliance")
    def device_compliance(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileEncryptionLevel")
    def file_encryption_level(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSharingSaveAs")
    def file_sharing_save_as(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBrowser")
    def managed_browser(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numOfApps")
    def num_of_apps(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineWipeTimeout")
    def offline_wipe_timeout(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pinNumRetry")
    def pin_num_retry(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="touchId")
    def touch_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIoMAMPolicyByNameResult(GetIoMAMPolicyByNameResult):
    def __await__(self): # -> Generator[Never, Any, GetIoMAMPolicyByNameResult]:
        ...
    


def get_io_mam_policy_by_name(host_name: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., select: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIoMAMPolicyByNameResult:
    
    ...

def get_io_mam_policy_by_name_output(host_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., select: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIoMAMPolicyByNameResult]:
    
    ...

