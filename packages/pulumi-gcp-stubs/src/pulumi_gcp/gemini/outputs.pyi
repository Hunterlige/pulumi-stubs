import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CodeToolsSettingEnabledTool",
    "CodeToolsSettingEnabledToolConfig",
    "RepositoryGroupIamBindingCondition",
    "RepositoryGroupIamMemberCondition",
    "RepositoryGroupRepository",
]

@pulumi.output_type
class CodeToolsSettingEnabledTool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        handle: _builtins.str,
        tool: _builtins.str,
        account_connector: Optional[_builtins.str] = ...,
        configs: Optional[Sequence[outputs.CodeToolsSettingEnabledToolConfig]] = ...,
        uri_override: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def handle(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountConnector")
    def account_connector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configs(
        self,
    ) -> Optional[Sequence[outputs.CodeToolsSettingEnabledToolConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="uriOverride")
    def uri_override(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CodeToolsSettingEnabledToolConfig(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryGroupIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryGroupIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryGroupRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, branch_pattern: _builtins.str, resource: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchPattern")
    def branch_pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
