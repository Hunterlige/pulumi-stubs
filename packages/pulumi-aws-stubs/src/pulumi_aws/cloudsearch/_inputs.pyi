import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainEndpointOptionsArgs",
    "DomainEndpointOptionsArgsDict",
    "DomainIndexFieldArgs",
    "DomainIndexFieldArgsDict",
    "DomainScalingParametersArgs",
    "DomainScalingParametersArgsDict",
]

class DomainEndpointOptionsArgsDict(TypedDict):
    enforce_https: NotRequired[pulumi.Input[_builtins.bool]]
    tls_security_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainEndpointOptionsArgs:
    def __init__(
        __self__,
        *,
        enforce_https: Optional[pulumi.Input[_builtins.bool]] = ...,
        tls_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_https.setter
    def enforce_https(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_security_policy.setter
    def tls_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainIndexFieldArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    analysis_scheme: NotRequired[pulumi.Input[_builtins.str]]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    facet: NotRequired[pulumi.Input[_builtins.bool]]
    highlight: NotRequired[pulumi.Input[_builtins.bool]]
    return_: NotRequired[pulumi.Input[_builtins.bool]]
    search: NotRequired[pulumi.Input[_builtins.bool]]
    sort: NotRequired[pulumi.Input[_builtins.bool]]
    source_fields: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainIndexFieldArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        analysis_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        facet: Optional[pulumi.Input[_builtins.bool]] = ...,
        highlight: Optional[pulumi.Input[_builtins.bool]] = ...,
        return_: Optional[pulumi.Input[_builtins.bool]] = ...,
        search: Optional[pulumi.Input[_builtins.bool]] = ...,
        sort: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_fields: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="analysisScheme")
    def analysis_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @analysis_scheme.setter
    def analysis_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def facet(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @facet.setter
    def facet(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def highlight(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @highlight.setter
    def highlight(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="return")
    def return_(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_.setter
    def return_(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def search(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @search.setter
    def search(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def sort(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sort.setter
    def sort(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFields")
    def source_fields(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_fields.setter
    def source_fields(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainScalingParametersArgsDict(TypedDict):
    desired_instance_type: NotRequired[pulumi.Input[_builtins.str]]
    desired_partition_count: NotRequired[pulumi.Input[_builtins.int]]
    desired_replication_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DomainScalingParametersArgs:
    def __init__(
        __self__,
        *,
        desired_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_partition_count: Optional[pulumi.Input[_builtins.int]] = ...,
        desired_replication_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredInstanceType")
    def desired_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_instance_type.setter
    def desired_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredPartitionCount")
    def desired_partition_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_partition_count.setter
    def desired_partition_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredReplicationCount")
    def desired_replication_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_replication_count.setter
    def desired_replication_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
