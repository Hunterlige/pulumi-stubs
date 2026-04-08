import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProfileArgs", "Profile"]

@pulumi.input_type
class ProfileArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        allowed_endpoint_record_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AllowedEndpointRecordType]]]
            ]
        ] = ...,
        dns_config: Optional[pulumi.Input[DnsConfigArgs]] = ...,
        endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_return: Optional[pulumi.Input[_builtins.float]] = ...,
        monitor_config: Optional[pulumi.Input[MonitorConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_status: Optional[
            pulumi.Input[Union[_builtins.str, ProfileStatus]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        traffic_routing_method: Optional[
            pulumi.Input[Union[_builtins.str, TrafficRoutingMethod]]
        ] = ...,
        traffic_view_enrollment_status: Optional[
            pulumi.Input[Union[_builtins.str, TrafficViewEnrollmentStatus]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedEndpointRecordTypes")
    def allowed_endpoint_record_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AllowedEndpointRecordType]]]
        ]
    ]: ...
    @allowed_endpoint_record_types.setter
    def allowed_endpoint_record_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AllowedEndpointRecordType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input[DnsConfigArgs]]: ...
    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input[DnsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_return.setter
    def max_return(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> Optional[pulumi.Input[MonitorConfigArgs]]: ...
    @monitor_config.setter
    def monitor_config(self, value: Optional[pulumi.Input[MonitorConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileStatus")
    def profile_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProfileStatus]]]: ...
    @profile_status.setter
    def profile_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProfileStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TrafficRoutingMethod]]]: ...
    @traffic_routing_method.setter
    def traffic_routing_method(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TrafficRoutingMethod]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trafficViewEnrollmentStatus")
    def traffic_view_enrollment_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TrafficViewEnrollmentStatus]]]: ...
    @traffic_view_enrollment_status.setter
    def traffic_view_enrollment_status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, TrafficViewEnrollmentStatus]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:trafficmanager:Profile")
class Profile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowed_endpoint_record_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AllowedEndpointRecordType]]]
            ]
        ] = ...,
        dns_config: Optional[
            pulumi.Input[Union[DnsConfigArgs, DnsConfigArgsDict]]
        ] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[EndpointArgs, EndpointArgsDict]]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_return: Optional[pulumi.Input[_builtins.float]] = ...,
        monitor_config: Optional[
            pulumi.Input[Union[MonitorConfigArgs, MonitorConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_status: Optional[
            pulumi.Input[Union[_builtins.str, ProfileStatus]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        traffic_routing_method: Optional[
            pulumi.Input[Union[_builtins.str, TrafficRoutingMethod]]
        ] = ...,
        traffic_view_enrollment_status: Optional[
            pulumi.Input[Union[_builtins.str, TrafficViewEnrollmentStatus]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Profile: ...
    @_builtins.property
    @pulumi.getter(name="allowedEndpointRecordTypes")
    def allowed_endpoint_record_types(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Output[Optional[outputs.DnsConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EndpointResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(
        self,
    ) -> pulumi.Output[Optional[outputs.MonitorConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficViewEnrollmentStatus")
    def traffic_view_enrollment_status(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
