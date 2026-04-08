import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateEndpointResult",
    "AwaitableGetPrivateEndpointResult",
    "get_private_endpoint",
    "get_private_endpoint_output",
]

@pulumi.output_type
class GetPrivateEndpointResult:
    def __init__(
        __self__,
        application_security_groups=...,
        azure_api_version=...,
        custom_dns_configs=...,
        custom_network_interface_name=...,
        etag=...,
        extended_location=...,
        id=...,
        ip_configurations=...,
        location=...,
        manual_private_link_service_connections=...,
        name=...,
        network_interfaces=...,
        private_link_service_connections=...,
        provisioning_state=...,
        subnet=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(
        self,
    ) -> Optional[Sequence[outputs.ApplicationSecurityGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigs")
    def custom_dns_configs(
        self,
    ) -> Optional[Sequence[outputs.CustomDnsConfigPropertiesFormatResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="customNetworkInterfaceName")
    def custom_network_interface_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Optional[Sequence[outputs.PrivateEndpointIPConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.NetworkInterfaceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubnetResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    def __await__(self): ...

def get_private_endpoint(
    expand: Optional[_builtins.str] = ...,
    private_endpoint_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateEndpointResult: ...
def get_private_endpoint_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateEndpointResult]: ...
