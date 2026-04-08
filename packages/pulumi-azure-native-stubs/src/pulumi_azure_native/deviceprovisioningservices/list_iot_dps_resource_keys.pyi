import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListIotDpsResourceKeysResult",
    "AwaitableListIotDpsResourceKeysResult",
    "list_iot_dps_resource_keys",
    "list_iot_dps_resource_keys_output",
]

@pulumi.output_type
class ListIotDpsResourceKeysResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        Sequence[
            outputs.SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionResponse
        ]
    ]: ...

class AwaitableListIotDpsResourceKeysResult(ListIotDpsResourceKeysResult):
    def __await__(self): ...

def list_iot_dps_resource_keys(
    provisioning_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListIotDpsResourceKeysResult: ...
def list_iot_dps_resource_keys_output(
    provisioning_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListIotDpsResourceKeysResult]: ...
