import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackendBucketArgs", "BackendBucket"]

@pulumi.input_type
class BackendBucketArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        cdn_policy: Optional[pulumi.Input[BackendBucketCdnPolicyArgs]] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[BackendBucketParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> Optional[pulumi.Input[BackendBucketCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(self, value: Optional[pulumi.Input[BackendBucketCdnPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_mode.setter
    def compression_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_response_headers.setter
    def custom_response_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[BackendBucketParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[BackendBucketParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BackendBucketState:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cdn_policy: Optional[pulumi.Input[BackendBucketCdnPolicyArgs]] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[BackendBucketParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> Optional[pulumi.Input[BackendBucketCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(self, value: Optional[pulumi.Input[BackendBucketCdnPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_mode.setter
    def compression_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_response_headers.setter
    def custom_response_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[BackendBucketParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[BackendBucketParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/backendBucket:BackendBucket")
class BackendBucket(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[BackendBucketCdnPolicyArgs, BackendBucketCdnPolicyArgsDict]
            ]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[BackendBucketParamsArgs, BackendBucketParamsArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BackendBucketArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[BackendBucketCdnPolicyArgs, BackendBucketCdnPolicyArgsDict]
            ]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[BackendBucketParamsArgs, BackendBucketParamsArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BackendBucket: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> pulumi.Output[outputs.BackendBucketCdnPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.BackendBucketParams]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
