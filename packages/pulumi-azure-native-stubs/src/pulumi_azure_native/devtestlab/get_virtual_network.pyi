import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNetworkResult",
    "AwaitableGetVirtualNetworkResult",
    "get_virtual_network",
    "get_virtual_network_output",
]

@pulumi.output_type
class GetVirtualNetworkResult:
    def __init__(
        __self__,
        allowed_subnets=...,
        azure_api_version=...,
        created_date=...,
        description=...,
        external_provider_resource_id=...,
        external_subnets=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        subnet_overrides=...,
        system_data=...,
        tags=...,
        type=...,
        unique_identifier=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(self) -> Optional[Sequence[outputs.SubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalProviderResourceId")
    def external_provider_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalSubnets")
    def external_subnets(self) -> Sequence[outputs.ExternalSubnetResponse]: ...
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
    @pulumi.getter(name="subnetOverrides")
    def subnet_overrides(
        self,
    ) -> Optional[Sequence[outputs.SubnetOverrideResponse]]: ...
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
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...

class AwaitableGetVirtualNetworkResult(GetVirtualNetworkResult):
    def __await__(self): ...

def get_virtual_network(
    expand: Optional[_builtins.str] = ...,
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkResult: ...
def get_virtual_network_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkResult]: ...
