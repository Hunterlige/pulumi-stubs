import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNamespacePnsCredentialsResult",
    "AwaitableGetNamespacePnsCredentialsResult",
    "get_namespace_pns_credentials",
    "get_namespace_pns_credentials_output",
]

@pulumi.output_type
class GetNamespacePnsCredentialsResult:
    def __init__(
        __self__,
        adm_credential=...,
        apns_credential=...,
        baidu_credential=...,
        browser_credential=...,
        fcm_v1_credential=...,
        gcm_credential=...,
        id=...,
        location=...,
        mpns_credential=...,
        name=...,
        system_data=...,
        tags=...,
        type=...,
        wns_credential=...,
        xiaomi_credential=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional[outputs.AdmCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional[outputs.ApnsCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional[outputs.BaiduCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="browserCredential")
    def browser_credential(self) -> Optional[outputs.BrowserCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(self) -> Optional[outputs.FcmV1CredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional[outputs.GcmCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional[outputs.MpnsCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional[outputs.WnsCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(self) -> Optional[outputs.XiaomiCredentialResponse]: ...

class AwaitableGetNamespacePnsCredentialsResult(GetNamespacePnsCredentialsResult):
    def __await__(self): ...

def get_namespace_pns_credentials(
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNamespacePnsCredentialsResult: ...
def get_namespace_pns_credentials_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNamespacePnsCredentialsResult]: ...
