

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProviderBatchingArgs', 'ProviderBatchingArgsDict', 'ProviderExternalCredentialsArgs', 'ProviderExternalCredentialsArgsDict']
class ProviderBatchingArgsDict(TypedDict):
    enable_batching: NotRequired[pulumi.Input[_builtins.bool]]
    send_after: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProviderBatchingArgs:
    def __init__(__self__, *, enable_batching: Optional[pulumi.Input[_builtins.bool]] = ..., send_after: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBatching")
    def enable_batching(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @enable_batching.setter
    def enable_batching(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAfter")
    def send_after(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @send_after.setter
    def send_after(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProviderExternalCredentialsArgsDict(TypedDict):
    audience: pulumi.Input[_builtins.str]
    identity_token: pulumi.Input[_builtins.str]
    service_account_email: pulumi.Input[_builtins.str]


@pulumi.input_type
class ProviderExternalCredentialsArgs:
    def __init__(__self__, *, audience: pulumi.Input[_builtins.str], identity_token: pulumi.Input[_builtins.str], service_account_email: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @audience.setter
    def audience(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityToken")
    def identity_token(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @identity_token.setter
    def identity_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


