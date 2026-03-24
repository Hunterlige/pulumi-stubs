import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiArgs", "Api"]

@pulumi.input_type
class ApiArgs:
    def __init__(
        __self__,
        *,
        config_bundle: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configBundle")
    def config_bundle(self) -> pulumi.Input[_builtins.str]: ...
    @config_bundle.setter
    def config_bundle(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detect_md5hash.setter
    def detect_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ApiState:
    def __init__(
        __self__,
        *,
        config_bundle: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        meta_datas: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiMetaDataArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        revisions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configBundle")
    def config_bundle(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_bundle.setter
    def config_bundle(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detect_md5hash.setter
    def detect_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestRevisionId")
    def latest_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_revision_id.setter
    def latest_revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @md5hash.setter
    def md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metaDatas")
    def meta_datas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiMetaDataArgs]]]]: ...
    @meta_datas.setter
    def meta_datas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiMetaDataArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revisions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @revisions.setter
    def revisions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:apigee/api:Api")
class Api(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config_bundle: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        config_bundle: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        meta_datas: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ApiMetaDataArgs, ApiMetaDataArgsDict]]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        revisions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> Api: ...
    @_builtins.property
    @pulumi.getter(name="configBundle")
    def config_bundle(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="latestRevisionId")
    def latest_revision_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def md5hash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metaDatas")
    def meta_datas(self) -> pulumi.Output[Sequence[outputs.ApiMetaData]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revisions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
