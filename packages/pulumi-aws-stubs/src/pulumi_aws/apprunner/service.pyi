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
        service_name: pulumi.Input[_builtins.str],
        source_configuration: pulumi.Input[ServiceSourceConfigurationArgs],
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[ServiceEncryptionConfigurationArgs]
        ] = ...,
        health_check_configuration: Optional[
            pulumi.Input[ServiceHealthCheckConfigurationArgs]
        ] = ...,
        instance_configuration: Optional[
            pulumi.Input[ServiceInstanceConfigurationArgs]
        ] = ...,
        network_configuration: Optional[
            pulumi.Input[ServiceNetworkConfigurationArgs]
        ] = ...,
        observability_configuration: Optional[
            pulumi.Input[ServiceObservabilityConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> pulumi.Input[ServiceSourceConfigurationArgs]: ...
    @source_configuration.setter
    def source_configuration(
        self, value: pulumi.Input[ServiceSourceConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[ServiceEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckConfigurationArgs]]: ...
    @health_check_configuration.setter
    def health_check_configuration(
        self, value: Optional[pulumi.Input[ServiceHealthCheckConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceInstanceConfigurationArgs]]: ...
    @instance_configuration.setter
    def instance_configuration(
        self, value: Optional[pulumi.Input[ServiceInstanceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceObservabilityConfigurationArgs]]: ...
    @observability_configuration.setter
    def observability_configuration(
        self, value: Optional[pulumi.Input[ServiceObservabilityConfigurationArgs]]
    ): ...
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

@pulumi.input_type
class _ServiceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[ServiceEncryptionConfigurationArgs]
        ] = ...,
        health_check_configuration: Optional[
            pulumi.Input[ServiceHealthCheckConfigurationArgs]
        ] = ...,
        instance_configuration: Optional[
            pulumi.Input[ServiceInstanceConfigurationArgs]
        ] = ...,
        network_configuration: Optional[
            pulumi.Input[ServiceNetworkConfigurationArgs]
        ] = ...,
        observability_configuration: Optional[
            pulumi.Input[ServiceObservabilityConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_url: Optional[pulumi.Input[_builtins.str]] = ...,
        source_configuration: Optional[
            pulumi.Input[ServiceSourceConfigurationArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[ServiceEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceHealthCheckConfigurationArgs]]: ...
    @health_check_configuration.setter
    def health_check_configuration(
        self, value: Optional[pulumi.Input[ServiceHealthCheckConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceInstanceConfigurationArgs]]: ...
    @instance_configuration.setter
    def instance_configuration(
        self, value: Optional[pulumi.Input[ServiceInstanceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceObservabilityConfigurationArgs]]: ...
    @observability_configuration.setter
    def observability_configuration(
        self, value: Optional[pulumi.Input[ServiceObservabilityConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_url.setter
    def service_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceSourceConfigurationArgs]]: ...
    @source_configuration.setter
    def source_configuration(
        self, value: Optional[pulumi.Input[ServiceSourceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:apprunner/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceEncryptionConfigurationArgs,
                    ServiceEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        health_check_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceHealthCheckConfigurationArgs,
                    ServiceHealthCheckConfigurationArgsDict,
                ]
            ]
        ] = ...,
        instance_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceInstanceConfigurationArgs,
                    ServiceInstanceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkConfigurationArgs, ServiceNetworkConfigurationArgsDict
                ]
            ]
        ] = ...,
        observability_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceObservabilityConfigurationArgs,
                    ServiceObservabilityConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceSourceConfigurationArgs, ServiceSourceConfigurationArgsDict
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceEncryptionConfigurationArgs,
                    ServiceEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        health_check_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceHealthCheckConfigurationArgs,
                    ServiceHealthCheckConfigurationArgsDict,
                ]
            ]
        ] = ...,
        instance_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceInstanceConfigurationArgs,
                    ServiceInstanceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        network_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkConfigurationArgs, ServiceNetworkConfigurationArgsDict
                ]
            ]
        ] = ...,
        observability_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceObservabilityConfigurationArgs,
                    ServiceObservabilityConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_url: Optional[pulumi.Input[_builtins.str]] = ...,
        source_configuration: Optional[
            pulumi.Input[
                Union[
                    ServiceSourceConfigurationArgs, ServiceSourceConfigurationArgsDict
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Service: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceEncryptionConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> pulumi.Output[outputs.ServiceHealthCheckConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> pulumi.Output[outputs.ServiceInstanceConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Output[outputs.ServiceNetworkConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceObservabilityConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> pulumi.Output[outputs.ServiceSourceConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
