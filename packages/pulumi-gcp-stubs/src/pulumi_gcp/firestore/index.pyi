import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IndexArgs", "Index"]

@pulumi.input_type
class IndexArgs:
    def __init__(
        __self__,
        *,
        collection: pulumi.Input[_builtins.str],
        fields: pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]],
        api_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        density: Optional[pulumi.Input[_builtins.str]] = ...,
        multikey: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_wait: Optional[pulumi.Input[_builtins.bool]] = ...,
        unique: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Input[_builtins.str]: ...
    @collection.setter
    def collection(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]]: ...
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="apiScope")
    def api_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_scope.setter
    def api_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def density(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @density.setter
    def density(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def multikey(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multikey.setter
    def multikey(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_scope.setter
    def query_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipWait")
    def skip_wait(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_wait.setter
    def skip_wait(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def unique(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique.setter
    def unique(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _IndexState:
    def __init__(
        __self__,
        *,
        api_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        density: Optional[pulumi.Input[_builtins.str]] = ...,
        fields: Optional[pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]]] = ...,
        multikey: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_wait: Optional[pulumi.Input[_builtins.bool]] = ...,
        unique: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiScope")
    def api_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_scope.setter
    def api_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def density(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @density.setter
    def density(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]]]: ...
    @fields.setter
    def fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexFieldArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def multikey(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multikey.setter
    def multikey(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_scope.setter
    def query_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipWait")
    def skip_wait(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_wait.setter
    def skip_wait(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def unique(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique.setter
    def unique(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("gcp:firestore/index:Index")
class Index(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        density: Optional[pulumi.Input[_builtins.str]] = ...,
        fields: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[IndexFieldArgs, IndexFieldArgsDict]]]
            ]
        ] = ...,
        multikey: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_wait: Optional[pulumi.Input[_builtins.bool]] = ...,
        unique: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IndexArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        density: Optional[pulumi.Input[_builtins.str]] = ...,
        fields: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[IndexFieldArgs, IndexFieldArgsDict]]]
            ]
        ] = ...,
        multikey: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_wait: Optional[pulumi.Input[_builtins.bool]] = ...,
        unique: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> Index: ...
    @_builtins.property
    @pulumi.getter(name="apiScope")
    def api_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def density(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[outputs.IndexField]]: ...
    @_builtins.property
    @pulumi.getter
    def multikey(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skipWait")
    def skip_wait(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def unique(self) -> pulumi.Output[_builtins.bool]: ...
