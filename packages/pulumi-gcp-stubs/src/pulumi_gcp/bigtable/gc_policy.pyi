import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GCPolicyArgs", "GCPolicy"]

@pulumi.input_type
class GCPolicyArgs:
    def __init__(
        __self__,
        *,
        column_family: pulumi.Input[_builtins.str],
        instance_name: pulumi.Input[_builtins.str],
        table: pulumi.Input[_builtins.str],
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        gc_rules: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_age: Optional[pulumi.Input[GCPolicyMaxAgeArgs]] = ...,
        max_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> pulumi.Input[_builtins.str]: ...
    @column_family.setter
    def column_family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gc_rules.setter
    def gc_rules(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[GCPolicyMaxAgeArgs]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[GCPolicyMaxAgeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="maxVersions")
    def max_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]]: ...
    @max_versions.setter
    def max_versions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GCPolicyState:
    def __init__(
        __self__,
        *,
        column_family: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        gc_rules: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        max_age: Optional[pulumi.Input[GCPolicyMaxAgeArgs]] = ...,
        max_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column_family.setter
    def column_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gc_rules.setter
    def gc_rules(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[GCPolicyMaxAgeArgs]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[GCPolicyMaxAgeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="maxVersions")
    def max_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]]: ...
    @max_versions.setter
    def max_versions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GCPolicyMaxVersionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigtable/gCPolicy:GCPolicy")
class GCPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        column_family: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        gc_rules: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        max_age: Optional[
            pulumi.Input[Union[GCPolicyMaxAgeArgs, GCPolicyMaxAgeArgsDict]]
        ] = ...,
        max_versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GCPolicyMaxVersionArgs, GCPolicyMaxVersionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GCPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        column_family: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        gc_rules: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        max_age: Optional[
            pulumi.Input[Union[GCPolicyMaxAgeArgs, GCPolicyMaxAgeArgsDict]]
        ] = ...,
        max_versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GCPolicyMaxVersionArgs, GCPolicyMaxVersionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GCPolicy: ...
    @_builtins.property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> pulumi.Output[Optional[outputs.GCPolicyMaxAge]]: ...
    @_builtins.property
    @pulumi.getter(name="maxVersions")
    def max_versions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.GCPolicyMaxVersion]]]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Output[_builtins.str]: ...
