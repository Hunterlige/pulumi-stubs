import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkSecurityPerimeterLinkResult",
    "AwaitableGetNetworkSecurityPerimeterLinkResult",
    "get_network_security_perimeter_link",
    "get_network_security_perimeter_link_output",
]

@pulumi.output_type
class GetNetworkSecurityPerimeterLinkResult:
    def __init__(
        __self__,
        auto_approved_remote_perimeter_resource_id=...,
        azure_api_version=...,
        description=...,
        etag=...,
        id=...,
        local_inbound_profiles=...,
        local_outbound_profiles=...,
        name=...,
        provisioning_state=...,
        remote_inbound_profiles=...,
        remote_outbound_profiles=...,
        remote_perimeter_guid=...,
        remote_perimeter_location=...,
        status=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoApprovedRemotePerimeterResourceId")
    def auto_approved_remote_perimeter_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localInboundProfiles")
    def local_inbound_profiles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localOutboundProfiles")
    def local_outbound_profiles(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remoteInboundProfiles")
    def remote_inbound_profiles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="remoteOutboundProfiles")
    def remote_outbound_profiles(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remotePerimeterGuid")
    def remote_perimeter_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remotePerimeterLocation")
    def remote_perimeter_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNetworkSecurityPerimeterLinkResult(
    GetNetworkSecurityPerimeterLinkResult
):
    def __await__(self): ...

def get_network_security_perimeter_link(
    link_name: Optional[_builtins.str] = ...,
    network_security_perimeter_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkSecurityPerimeterLinkResult: ...
def get_network_security_perimeter_link_output(
    link_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkSecurityPerimeterLinkResult]: ...
