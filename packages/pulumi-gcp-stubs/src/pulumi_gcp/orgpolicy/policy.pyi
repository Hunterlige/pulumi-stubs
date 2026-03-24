import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyArgs", "Policy"]

@pulumi.input_type
class PolicyArgs:
    def __init__(
        __self__,
        *,
        parent: pulumi.Input[_builtins.str],
        dry_run_spec: Optional[pulumi.Input[PolicyDryRunSpecArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[PolicySpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dryRunSpec")
    def dry_run_spec(self) -> Optional[pulumi.Input[PolicyDryRunSpecArgs]]: ...
    @dry_run_spec.setter
    def dry_run_spec(self, value: Optional[pulumi.Input[PolicyDryRunSpecArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[PolicySpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[PolicySpecArgs]]): ...

@pulumi.input_type
class _PolicyState:
    def __init__(
        __self__,
        *,
        dry_run_spec: Optional[pulumi.Input[PolicyDryRunSpecArgs]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[PolicySpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dryRunSpec")
    def dry_run_spec(self) -> Optional[pulumi.Input[PolicyDryRunSpecArgs]]: ...
    @dry_run_spec.setter
    def dry_run_spec(self, value: Optional[pulumi.Input[PolicyDryRunSpecArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[PolicySpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[PolicySpecArgs]]): ...

@pulumi.type_token("gcp:orgpolicy/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dry_run_spec: Optional[
            pulumi.Input[Union[PolicyDryRunSpecArgs, PolicyDryRunSpecArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[Union[PolicySpecArgs, PolicySpecArgsDict]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        dry_run_spec: Optional[
            pulumi.Input[Union[PolicyDryRunSpecArgs, PolicyDryRunSpecArgsDict]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[Union[PolicySpecArgs, PolicySpecArgsDict]]] = ...,
    ) -> Policy: ...
    @_builtins.property
    @pulumi.getter(name="dryRunSpec")
    def dry_run_spec(self) -> pulumi.Output[Optional[outputs.PolicyDryRunSpec]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional[outputs.PolicySpec]]: ...
