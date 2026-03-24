import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SchemaBundleArgs", "SchemaBundle"]

@pulumi.input_type
class SchemaBundleArgs:
    def __init__(
        __self__,
        *,
        proto_schema: pulumi.Input[SchemaBundleProtoSchemaArgs],
        schema_bundle_id: pulumi.Input[_builtins.str],
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protoSchema")
    def proto_schema(self) -> pulumi.Input[SchemaBundleProtoSchemaArgs]: ...
    @proto_schema.setter
    def proto_schema(self, value: pulumi.Input[SchemaBundleProtoSchemaArgs]): ...
    @_builtins.property
    @pulumi.getter(name="schemaBundleId")
    def schema_bundle_id(self) -> pulumi.Input[_builtins.str]: ...
    @schema_bundle_id.setter
    def schema_bundle_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.input_type
class _SchemaBundleState:
    def __init__(
        __self__,
        *,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proto_schema: Optional[pulumi.Input[SchemaBundleProtoSchemaArgs]] = ...,
        schema_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="protoSchema")
    def proto_schema(self) -> Optional[pulumi.Input[SchemaBundleProtoSchemaArgs]]: ...
    @proto_schema.setter
    def proto_schema(
        self, value: Optional[pulumi.Input[SchemaBundleProtoSchemaArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaBundleId")
    def schema_bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_bundle_id.setter
    def schema_bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigtable/schemaBundle:SchemaBundle")
class SchemaBundle(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proto_schema: Optional[
            pulumi.Input[
                Union[SchemaBundleProtoSchemaArgs, SchemaBundleProtoSchemaArgsDict]
            ]
        ] = ...,
        schema_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SchemaBundleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proto_schema: Optional[
            pulumi.Input[
                Union[SchemaBundleProtoSchemaArgs, SchemaBundleProtoSchemaArgsDict]
            ]
        ] = ...,
        schema_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SchemaBundle: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protoSchema")
    def proto_schema(self) -> pulumi.Output[outputs.SchemaBundleProtoSchema]: ...
    @_builtins.property
    @pulumi.getter(name="schemaBundleId")
    def schema_bundle_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Output[Optional[_builtins.str]]: ...
