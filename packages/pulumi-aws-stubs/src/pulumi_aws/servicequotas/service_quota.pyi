import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceQuotaArgs", "ServiceQuota"]

@pulumi.input_type
class ServiceQuotaArgs:
    def __init__(
        __self__,
        *,
        quota_code: pulumi.Input[_builtins.str],
        service_code: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.float],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> pulumi.Input[_builtins.str]: ...
    @quota_code.setter
    def quota_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> pulumi.Input[_builtins.str]: ...
    @service_code.setter
    def service_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServiceQuotaState:
    def __init__(
        __self__,
        *,
        adjustable: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_value: Optional[pulumi.Input[_builtins.float]] = ...,
        quota_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_id: Optional[pulumi.Input[_builtins.str]] = ...,
        request_status: Optional[pulumi.Input[_builtins.str]] = ...,
        service_code: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceQuotaUsageMetricArgs]]]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def adjustable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @adjustable.setter
    def adjustable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_code.setter
    def quota_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_name.setter
    def quota_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestStatus")
    def request_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_status.setter
    def request_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_code.setter
    def service_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usageMetrics")
    def usage_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceQuotaUsageMetricArgs]]]
    ]: ...
    @usage_metrics.setter
    def usage_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceQuotaUsageMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

@pulumi.type_token("aws:servicequotas/serviceQuota:ServiceQuota")
class ServiceQuota(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        quota_code: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_code: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceQuotaArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        adjustable: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_value: Optional[pulumi.Input[_builtins.float]] = ...,
        quota_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_id: Optional[pulumi.Input[_builtins.str]] = ...,
        request_status: Optional[pulumi.Input[_builtins.str]] = ...,
        service_code: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServiceQuotaUsageMetricArgs, ServiceQuotaUsageMetricArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> ServiceQuota: ...
    @_builtins.property
    @pulumi.getter
    def adjustable(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestStatus")
    def request_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usageMetrics")
    def usage_metrics(
        self,
    ) -> pulumi.Output[Sequence[outputs.ServiceQuotaUsageMetric]]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[_builtins.float]: ...
