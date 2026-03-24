import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EdgeCacheOriginArgs", "EdgeCacheOrigin"]

@pulumi.input_type
class EdgeCacheOriginArgs:
    def __init__(
        __self__,
        *,
        origin_address: pulumi.Input[_builtins.str],
        aws_v4_authentication: Optional[
            pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        flex_shielding: Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_override_action: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]
        ] = ...,
        origin_redirect: Optional[
            pulumi.Input[EdgeCacheOriginOriginRedirectArgs]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originAddress")
    def origin_address(self) -> pulumi.Input[_builtins.str]: ...
    @origin_address.setter
    def origin_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsV4Authentication")
    def aws_v4_authentication(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]]: ...
    @aws_v4_authentication.setter
    def aws_v4_authentication(
        self, value: Optional[pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverOrigin")
    def failover_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover_origin.setter
    def failover_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flexShielding")
    def flex_shielding(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]]: ...
    @flex_shielding.setter
    def flex_shielding(
        self, value: Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_attempts.setter
    def max_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originOverrideAction")
    def origin_override_action(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]]: ...
    @origin_override_action.setter
    def origin_override_action(
        self, value: Optional[pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="originRedirect")
    def origin_redirect(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginOriginRedirectArgs]]: ...
    @origin_redirect.setter
    def origin_redirect(
        self, value: Optional[pulumi.Input[EdgeCacheOriginOriginRedirectArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retry_conditions.setter
    def retry_conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]]): ...

@pulumi.input_type
class _EdgeCacheOriginState:
    def __init__(
        __self__,
        *,
        aws_v4_authentication: Optional[
            pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        failover_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        flex_shielding: Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_address: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_override_action: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]
        ] = ...,
        origin_redirect: Optional[
            pulumi.Input[EdgeCacheOriginOriginRedirectArgs]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsV4Authentication")
    def aws_v4_authentication(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]]: ...
    @aws_v4_authentication.setter
    def aws_v4_authentication(
        self, value: Optional[pulumi.Input[EdgeCacheOriginAwsV4AuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverOrigin")
    def failover_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover_origin.setter
    def failover_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flexShielding")
    def flex_shielding(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]]: ...
    @flex_shielding.setter
    def flex_shielding(
        self, value: Optional[pulumi.Input[EdgeCacheOriginFlexShieldingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_attempts.setter
    def max_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originAddress")
    def origin_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_address.setter
    def origin_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originOverrideAction")
    def origin_override_action(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]]: ...
    @origin_override_action.setter
    def origin_override_action(
        self, value: Optional[pulumi.Input[EdgeCacheOriginOriginOverrideActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="originRedirect")
    def origin_redirect(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginOriginRedirectArgs]]: ...
    @origin_redirect.setter
    def origin_redirect(
        self, value: Optional[pulumi.Input[EdgeCacheOriginOriginRedirectArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retry_conditions.setter
    def retry_conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[EdgeCacheOriginTimeoutArgs]]): ...

@pulumi.type_token(...)
class EdgeCacheOrigin(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_v4_authentication: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginAwsV4AuthenticationArgs,
                    EdgeCacheOriginAwsV4AuthenticationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        flex_shielding: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginFlexShieldingArgs,
                    EdgeCacheOriginFlexShieldingArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_address: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_override_action: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginOriginOverrideActionArgs,
                    EdgeCacheOriginOriginOverrideActionArgsDict,
                ]
            ]
        ] = ...,
        origin_redirect: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginOriginRedirectArgs,
                    EdgeCacheOriginOriginRedirectArgsDict,
                ]
            ]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[
            pulumi.Input[
                Union[EdgeCacheOriginTimeoutArgs, EdgeCacheOriginTimeoutArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EdgeCacheOriginArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_v4_authentication: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginAwsV4AuthenticationArgs,
                    EdgeCacheOriginAwsV4AuthenticationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        failover_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        flex_shielding: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginFlexShieldingArgs,
                    EdgeCacheOriginFlexShieldingArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_address: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_override_action: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginOriginOverrideActionArgs,
                    EdgeCacheOriginOriginOverrideActionArgsDict,
                ]
            ]
        ] = ...,
        origin_redirect: Optional[
            pulumi.Input[
                Union[
                    EdgeCacheOriginOriginRedirectArgs,
                    EdgeCacheOriginOriginRedirectArgsDict,
                ]
            ]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[
            pulumi.Input[
                Union[EdgeCacheOriginTimeoutArgs, EdgeCacheOriginTimeoutArgsDict]
            ]
        ] = ...,
    ) -> EdgeCacheOrigin: ...
    @_builtins.property
    @pulumi.getter(name="awsV4Authentication")
    def aws_v4_authentication(
        self,
    ) -> pulumi.Output[Optional[outputs.EdgeCacheOriginAwsV4Authentication]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failoverOrigin")
    def failover_origin(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="flexShielding")
    def flex_shielding(
        self,
    ) -> pulumi.Output[Optional[outputs.EdgeCacheOriginFlexShielding]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originAddress")
    def origin_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originOverrideAction")
    def origin_override_action(
        self,
    ) -> pulumi.Output[Optional[outputs.EdgeCacheOriginOriginOverrideAction]]: ...
    @_builtins.property
    @pulumi.getter(name="originRedirect")
    def origin_redirect(
        self,
    ) -> pulumi.Output[Optional[outputs.EdgeCacheOriginOriginRedirect]]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[outputs.EdgeCacheOriginTimeout]]: ...
