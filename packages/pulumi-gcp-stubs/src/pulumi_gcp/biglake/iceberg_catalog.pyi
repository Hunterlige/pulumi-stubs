import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IcebergCatalogArgs", "IcebergCatalog"]

@pulumi.input_type
class IcebergCatalogArgs:
    def __init__(
        __self__,
        *,
        catalog_type: pulumi.Input[_builtins.str],
        credential_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogType")
    def catalog_type(self) -> pulumi.Input[_builtins.str]: ...
    @catalog_type.setter
    def catalog_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialMode")
    def credential_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_mode.setter
    def credential_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_location.setter
    def primary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _IcebergCatalogState:
    def __init__(
        __self__,
        *,
        biglake_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_type: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas: Optional[
            pulumi.Input[Sequence[pulumi.Input[IcebergCatalogReplicaArgs]]]
        ] = ...,
        storage_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="biglakeServiceAccount")
    def biglake_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @biglake_service_account.setter
    def biglake_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogType")
    def catalog_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_type.setter
    def catalog_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialMode")
    def credential_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_mode.setter
    def credential_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_location.setter
    def default_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_location.setter
    def primary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IcebergCatalogReplicaArgs]]]]: ...
    @replicas.setter
    def replicas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IcebergCatalogReplicaArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageRegions")
    def storage_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_regions.setter
    def storage_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:biglake/icebergCatalog:IcebergCatalog")
class IcebergCatalog(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_type: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IcebergCatalogArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        biglake_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_type: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[IcebergCatalogReplicaArgs, IcebergCatalogReplicaArgsDict]
                    ]
                ]
            ]
        ] = ...,
        storage_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IcebergCatalog: ...
    @_builtins.property
    @pulumi.getter(name="biglakeServiceAccount")
    def biglake_service_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="catalogType")
    def catalog_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialMode")
    def credential_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Sequence[outputs.IcebergCatalogReplica]]: ...
    @_builtins.property
    @pulumi.getter(name="storageRegions")
    def storage_regions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
