import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebhookCallbackConfigResult",
    "AwaitableGetWebhookCallbackConfigResult",
    "get_webhook_callback_config",
    "get_webhook_callback_config_output",
]

@pulumi.output_type
class GetWebhookCallbackConfigResult:
    def __init__(__self__, custom_headers=..., service_uri=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> _builtins.str: ...

class AwaitableGetWebhookCallbackConfigResult(GetWebhookCallbackConfigResult):
    def __await__(self): ...

def get_webhook_callback_config(
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    webhook_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebhookCallbackConfigResult: ...
def get_webhook_callback_config_output(
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    webhook_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebhookCallbackConfigResult]: ...
