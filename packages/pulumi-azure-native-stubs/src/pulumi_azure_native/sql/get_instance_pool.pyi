import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstancePoolResult",
    "AwaitableGetInstancePoolResult",
    "get_instance_pool",
    "get_instance_pool_output",
]

@pulumi.output_type
class GetInstancePoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        dns_zone=...,
        id=...,
        license_type=...,
        location=...,
        maintenance_configuration_id=...,
        name=...,
        sku=...,
        subnet_id=...,
        tags=...,
        type=...,
        v_cores=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsZone")
    def dns_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> _builtins.int: ...

class AwaitableGetInstancePoolResult(GetInstancePoolResult):
    def __await__(self): ...

def get_instance_pool(
    instance_pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstancePoolResult: ...
def get_instance_pool_output(
    instance_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstancePoolResult]: ...
