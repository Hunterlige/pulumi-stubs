import builtins as _builtins
import sys
import pulumi
from typing import Any, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceNetworkAccessControl", "WorkspaceVpcConfiguration"]

@pulumi.output_type
class WorkspaceNetworkAccessControl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prefix_list_ids: Sequence[_builtins.str],
        vpce_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class WorkspaceVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
