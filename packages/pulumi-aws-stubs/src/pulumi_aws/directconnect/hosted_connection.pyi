import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HostedConnectionArgs", "HostedConnection"]

@pulumi.input_type
class HostedConnectionArgs:
    def __init__(
        __self__,
        *,
        bandwidth: pulumi.Input[_builtins.str],
        connection_id: pulumi.Input[_builtins.str],
        owner_account_id: pulumi.Input[_builtins.str],
        vlan: pulumi.Input[_builtins.int],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Input[_builtins.str]: ...
    @bandwidth.setter
    def bandwidth(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @owner_account_id.setter
    def owner_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> pulumi.Input[_builtins.int]: ...
    @vlan.setter
    def vlan(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _HostedConnectionState:
    def __init__(
        __self__,
        *,
        aws_device: Optional[pulumi.Input[_builtins.str]] = ...,
        bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_region: Optional[pulumi.Input[_builtins.str]] = ...,
        has_logical_redundancy: Optional[pulumi.Input[_builtins.str]] = ...,
        jumbo_frame_capable: Optional[pulumi.Input[_builtins.bool]] = ...,
        lag_id: Optional[pulumi.Input[_builtins.str]] = ...,
        loa_issue_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vlan: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_device.setter
    def aws_device(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionRegion")
    def connection_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_region.setter
    def connection_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hasLogicalRedundancy")
    def has_logical_redundancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @has_logical_redundancy.setter
    def has_logical_redundancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @jumbo_frame_capable.setter
    def jumbo_frame_capable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lagId")
    def lag_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lag_id.setter
    def lag_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loaIssueTime")
    def loa_issue_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @loa_issue_time.setter
    def loa_issue_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_name.setter
    def partner_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class HostedConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vlan: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HostedConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_device: Optional[pulumi.Input[_builtins.str]] = ...,
        bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_region: Optional[pulumi.Input[_builtins.str]] = ...,
        has_logical_redundancy: Optional[pulumi.Input[_builtins.str]] = ...,
        jumbo_frame_capable: Optional[pulumi.Input[_builtins.bool]] = ...,
        lag_id: Optional[pulumi.Input[_builtins.str]] = ...,
        loa_issue_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vlan: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> HostedConnection: ...
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionRegion")
    def connection_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasLogicalRedundancy")
    def has_logical_redundancy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lagId")
    def lag_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loaIssueTime")
    def loa_issue_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> pulumi.Output[_builtins.int]: ...
