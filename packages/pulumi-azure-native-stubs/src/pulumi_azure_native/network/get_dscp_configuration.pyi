import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDscpConfigurationResult",
    "AwaitableGetDscpConfigurationResult",
    "get_dscp_configuration",
    "get_dscp_configuration_output",
]

@pulumi.output_type
class GetDscpConfigurationResult:
    def __init__(
        __self__,
        associated_network_interfaces=...,
        azure_api_version=...,
        destination_ip_ranges=...,
        destination_port_ranges=...,
        etag=...,
        id=...,
        location=...,
        markings=...,
        name=...,
        protocol=...,
        provisioning_state=...,
        qos_collection_id=...,
        qos_definition_collection=...,
        resource_guid=...,
        source_ip_ranges=...,
        source_port_ranges=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedNetworkInterfaces")
    def associated_network_interfaces(
        self,
    ) -> Sequence[outputs.NetworkInterfaceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(
        self,
    ) -> Optional[Sequence[outputs.QosIpRangeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Optional[Sequence[outputs.QosPortRangeResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def markings(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qosCollectionId")
    def qos_collection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qosDefinitionCollection")
    def qos_definition_collection(
        self,
    ) -> Optional[Sequence[outputs.QosDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Optional[Sequence[outputs.QosIpRangeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> Optional[Sequence[outputs.QosPortRangeResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDscpConfigurationResult(GetDscpConfigurationResult):
    def __await__(self): ...

def get_dscp_configuration(
    dscp_configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDscpConfigurationResult: ...
def get_dscp_configuration_output(
    dscp_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDscpConfigurationResult]: ...
