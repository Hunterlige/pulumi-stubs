import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDelegatedSubnetServiceDetailsResult",
    "AwaitableGetDelegatedSubnetServiceDetailsResult",
    "get_delegated_subnet_service_details",
    "get_delegated_subnet_service_details_output",
]

@pulumi.output_type
class GetDelegatedSubnetServiceDetailsResult:
    def __init__(
        __self__,
        allocation_block_prefix_size=...,
        azure_api_version=...,
        controller_details=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        resource_guid=...,
        subnet_details=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationBlockPrefixSize")
    def allocation_block_prefix_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> Optional[outputs.ControllerDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetDetails")
    def subnet_details(self) -> Optional[outputs.SubnetDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDelegatedSubnetServiceDetailsResult(
    GetDelegatedSubnetServiceDetailsResult
):
    def __await__(self): ...

def get_delegated_subnet_service_details(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDelegatedSubnetServiceDetailsResult: ...
def get_delegated_subnet_service_details_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDelegatedSubnetServiceDetailsResult]: ...
