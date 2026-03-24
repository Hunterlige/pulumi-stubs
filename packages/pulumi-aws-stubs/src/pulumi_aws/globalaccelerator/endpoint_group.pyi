import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EndpointGroupArgs", "EndpointGroup"]

@pulumi.input_type
class EndpointGroupArgs:
    def __init__(
        __self__,
        *,
        listener_arn: pulumi.Input[_builtins.str],
        endpoint_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
        ] = ...,
        endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_path: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_port: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        port_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
        ] = ...,
        threshold_count: Optional[pulumi.Input[_builtins.int]] = ...,
        traffic_dial_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Input[_builtins.str]: ...
    @listener_arn.setter
    def listener_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
    ]: ...
    @endpoint_configurations.setter
    def endpoint_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_group_region.setter
    def endpoint_group_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @health_check_interval_seconds.setter
    def health_check_interval_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPort")
    def health_check_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @health_check_port.setter
    def health_check_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckProtocol")
    def health_check_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_protocol.setter
    def health_check_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portOverrides")
    def port_overrides(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
    ]: ...
    @port_overrides.setter
    def port_overrides(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="thresholdCount")
    def threshold_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @threshold_count.setter
    def threshold_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficDialPercentage")
    def traffic_dial_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @traffic_dial_percentage.setter
    def traffic_dial_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

@pulumi.input_type
class _EndpointGroupState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
        ] = ...,
        endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_path: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_port: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
        ] = ...,
        threshold_count: Optional[pulumi.Input[_builtins.int]] = ...,
        traffic_dial_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
    ]: ...
    @endpoint_configurations.setter
    def endpoint_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupEndpointConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_group_region.setter
    def endpoint_group_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @health_check_interval_seconds.setter
    def health_check_interval_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPort")
    def health_check_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @health_check_port.setter
    def health_check_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckProtocol")
    def health_check_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_protocol.setter
    def health_check_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listener_arn.setter
    def listener_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portOverrides")
    def port_overrides(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
    ]: ...
    @port_overrides.setter
    def port_overrides(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointGroupPortOverrideArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="thresholdCount")
    def threshold_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @threshold_count.setter
    def threshold_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficDialPercentage")
    def traffic_dial_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @traffic_dial_percentage.setter
    def traffic_dial_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

@pulumi.type_token("aws:globalaccelerator/endpointGroup:EndpointGroup")
class EndpointGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        endpoint_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointGroupEndpointConfigurationArgs,
                            EndpointGroupEndpointConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_path: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_port: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointGroupPortOverrideArgs,
                            EndpointGroupPortOverrideArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        threshold_count: Optional[pulumi.Input[_builtins.int]] = ...,
        traffic_dial_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointGroupEndpointConfigurationArgs,
                            EndpointGroupEndpointConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_path: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_port: Optional[pulumi.Input[_builtins.int]] = ...,
        health_check_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointGroupPortOverrideArgs,
                            EndpointGroupPortOverrideArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        threshold_count: Optional[pulumi.Input[_builtins.int]] = ...,
        traffic_dial_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> EndpointGroup: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.EndpointGroupEndpointConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckPort")
    def health_check_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckProtocol")
    def health_check_protocol(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="portOverrides")
    def port_overrides(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EndpointGroupPortOverride]]]: ...
    @_builtins.property
    @pulumi.getter(name="thresholdCount")
    def threshold_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficDialPercentage")
    def traffic_dial_percentage(self) -> pulumi.Output[Optional[_builtins.float]]: ...
