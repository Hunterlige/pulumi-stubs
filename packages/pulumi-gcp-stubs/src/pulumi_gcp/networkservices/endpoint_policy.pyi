import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EndpointPolicyArgs", "EndpointPolicy"]

@pulumi.input_type
class EndpointPolicyArgs:
    def __init__(
        __self__,
        *,
        endpoint_matcher: pulumi.Input[EndpointPolicyEndpointMatcherArgs],
        type: pulumi.Input[_builtins.str],
        authorization_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        client_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_port_selector: Optional[
            pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointMatcher")
    def endpoint_matcher(self) -> pulumi.Input[EndpointPolicyEndpointMatcherArgs]: ...
    @endpoint_matcher.setter
    def endpoint_matcher(
        self, value: pulumi.Input[EndpointPolicyEndpointMatcherArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicy")
    def authorization_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_policy.setter
    def authorization_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientTlsPolicy")
    def client_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_tls_policy.setter
    def client_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_tls_policy.setter
    def server_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPortSelector")
    def traffic_port_selector(
        self,
    ) -> Optional[pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]]: ...
    @traffic_port_selector.setter
    def traffic_port_selector(
        self, value: Optional[pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]]
    ): ...

@pulumi.input_type
class _EndpointPolicyState:
    def __init__(
        __self__,
        *,
        authorization_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        client_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_matcher: Optional[
            pulumi.Input[EndpointPolicyEndpointMatcherArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_port_selector: Optional[
            pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicy")
    def authorization_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_policy.setter
    def authorization_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientTlsPolicy")
    def client_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_tls_policy.setter
    def client_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="endpointMatcher")
    def endpoint_matcher(
        self,
    ) -> Optional[pulumi.Input[EndpointPolicyEndpointMatcherArgs]]: ...
    @endpoint_matcher.setter
    def endpoint_matcher(
        self, value: Optional[pulumi.Input[EndpointPolicyEndpointMatcherArgs]]
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_tls_policy.setter
    def server_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPortSelector")
    def traffic_port_selector(
        self,
    ) -> Optional[pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]]: ...
    @traffic_port_selector.setter
    def traffic_port_selector(
        self, value: Optional[pulumi.Input[EndpointPolicyTrafficPortSelectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:networkservices/endpointPolicy:EndpointPolicy")
class EndpointPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        client_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_matcher: Optional[
            pulumi.Input[
                Union[
                    EndpointPolicyEndpointMatcherArgs,
                    EndpointPolicyEndpointMatcherArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_port_selector: Optional[
            pulumi.Input[
                Union[
                    EndpointPolicyTrafficPortSelectorArgs,
                    EndpointPolicyTrafficPortSelectorArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        client_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_matcher: Optional[
            pulumi.Input[
                Union[
                    EndpointPolicyEndpointMatcherArgs,
                    EndpointPolicyEndpointMatcherArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_port_selector: Optional[
            pulumi.Input[
                Union[
                    EndpointPolicyTrafficPortSelectorArgs,
                    EndpointPolicyTrafficPortSelectorArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EndpointPolicy: ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicy")
    def authorization_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientTlsPolicy")
    def client_tls_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointMatcher")
    def endpoint_matcher(
        self,
    ) -> pulumi.Output[outputs.EndpointPolicyEndpointMatcher]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficPortSelector")
    def traffic_port_selector(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointPolicyTrafficPortSelector]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
