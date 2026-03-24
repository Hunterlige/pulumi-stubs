import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceArgs", "Service"]

@pulumi.input_type
class ServiceArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_config: Optional[pulumi.Input[ServiceDnsConfigArgs]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_check_config: Optional[pulumi.Input[ServiceHealthCheckConfigArgs]] = ...,
        health_check_custom_config: Optional[
            pulumi.Input[ServiceHealthCheckCustomConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input[ServiceDnsConfigArgs]]: ...
    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input[ServiceDnsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckConfigArgs]]: ...
    @health_check_config.setter
    def health_check_config(
        self, value: Optional[pulumi.Input[ServiceHealthCheckConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckCustomConfig")
    def health_check_custom_config(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckCustomConfigArgs]]: ...
    @health_check_custom_config.setter
    def health_check_custom_config(
        self, value: Optional[pulumi.Input[ServiceHealthCheckCustomConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServiceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_config: Optional[pulumi.Input[ServiceDnsConfigArgs]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_check_config: Optional[pulumi.Input[ServiceHealthCheckConfigArgs]] = ...,
        health_check_custom_config: Optional[
            pulumi.Input[ServiceHealthCheckCustomConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input[ServiceDnsConfigArgs]]: ...
    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input[ServiceDnsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckConfigArgs]]: ...
    @health_check_config.setter
    def health_check_config(
        self, value: Optional[pulumi.Input[ServiceHealthCheckConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckCustomConfig")
    def health_check_custom_config(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckCustomConfigArgs]]: ...
    @health_check_custom_config.setter
    def health_check_custom_config(
        self, value: Optional[pulumi.Input[ServiceHealthCheckCustomConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:servicediscovery/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_config: Optional[
            pulumi.Input[Union[ServiceDnsConfigArgs, ServiceDnsConfigArgsDict]]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_check_config: Optional[
            pulumi.Input[
                Union[ServiceHealthCheckConfigArgs, ServiceHealthCheckConfigArgsDict]
            ]
        ] = ...,
        health_check_custom_config: Optional[
            pulumi.Input[
                Union[
                    ServiceHealthCheckCustomConfigArgs,
                    ServiceHealthCheckCustomConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ServiceArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_config: Optional[
            pulumi.Input[Union[ServiceDnsConfigArgs, ServiceDnsConfigArgsDict]]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_check_config: Optional[
            pulumi.Input[
                Union[ServiceHealthCheckConfigArgs, ServiceHealthCheckConfigArgsDict]
            ]
        ] = ...,
        health_check_custom_config: Optional[
            pulumi.Input[
                Union[
                    ServiceHealthCheckCustomConfigArgs,
                    ServiceHealthCheckCustomConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Service: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Output[Optional[outputs.ServiceDnsConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceHealthCheckConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckCustomConfig")
    def health_check_custom_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceHealthCheckCustomConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
