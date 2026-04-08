import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetZoneResult", "AwaitableGetZoneResult", "get_zone", "get_zone_output"]

@pulumi.output_type
class GetZoneResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        location=...,
        max_number_of_record_sets=...,
        max_number_of_records_per_record_set=...,
        name=...,
        name_servers=...,
        number_of_record_sets=...,
        registration_virtual_networks=...,
        resolution_virtual_networks=...,
        signing_keys=...,
        system_data=...,
        tags=...,
        type=...,
        zone_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="maxNumberOfRecordsPerRecordSet")
    def max_number_of_records_per_record_set(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="signingKeys")
    def signing_keys(self) -> Sequence[outputs.SigningKeyResponse]: ...
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
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetZoneResult(GetZoneResult):
    def __await__(self): ...

def get_zone(
    resource_group_name: Optional[_builtins.str] = ...,
    zone_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetZoneResult: ...
def get_zone_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetZoneResult]: ...
