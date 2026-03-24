import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainEndpointOptions", "DomainIndexField", "DomainScalingParameters"]

@pulumi.output_type
class DomainEndpointOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enforce_https: Optional[_builtins.bool] = ...,
        tls_security_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainIndexField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        analysis_scheme: Optional[_builtins.str] = ...,
        default_value: Optional[_builtins.str] = ...,
        facet: Optional[_builtins.bool] = ...,
        highlight: Optional[_builtins.bool] = ...,
        return_: Optional[_builtins.bool] = ...,
        search: Optional[_builtins.bool] = ...,
        sort: Optional[_builtins.bool] = ...,
        source_fields: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="analysisScheme")
    def analysis_scheme(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def facet(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def highlight(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="return")
    def return_(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def search(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def sort(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFields")
    def source_fields(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainScalingParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_instance_type: Optional[_builtins.str] = ...,
        desired_partition_count: Optional[_builtins.int] = ...,
        desired_replication_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredInstanceType")
    def desired_instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="desiredPartitionCount")
    def desired_partition_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="desiredReplicationCount")
    def desired_replication_count(self) -> Optional[_builtins.int]: ...
