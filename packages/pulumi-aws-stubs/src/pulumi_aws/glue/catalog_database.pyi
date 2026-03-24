import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CatalogDatabaseArgs", "CatalogDatabase"]

@pulumi.input_type
class CatalogDatabaseArgs:
    def __init__(
        __self__,
        *,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_table_default_permissions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        federated_database: Optional[
            pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]
        ] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_database: Optional[
            pulumi.Input[CatalogDatabaseTargetDatabaseArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
        ]
    ]: ...
    @create_table_default_permissions.setter
    def create_table_default_permissions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="federatedDatabase")
    def federated_database(
        self,
    ) -> Optional[pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]]: ...
    @federated_database.setter
    def federated_database(
        self, value: Optional[pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDatabase")
    def target_database(
        self,
    ) -> Optional[pulumi.Input[CatalogDatabaseTargetDatabaseArgs]]: ...
    @target_database.setter
    def target_database(
        self, value: Optional[pulumi.Input[CatalogDatabaseTargetDatabaseArgs]]
    ): ...

@pulumi.input_type
class _CatalogDatabaseState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_table_default_permissions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        federated_database: Optional[
            pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]
        ] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_database: Optional[
            pulumi.Input[CatalogDatabaseTargetDatabaseArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
        ]
    ]: ...
    @create_table_default_permissions.setter
    def create_table_default_permissions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="federatedDatabase")
    def federated_database(
        self,
    ) -> Optional[pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]]: ...
    @federated_database.setter
    def federated_database(
        self, value: Optional[pulumi.Input[CatalogDatabaseFederatedDatabaseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDatabase")
    def target_database(
        self,
    ) -> Optional[pulumi.Input[CatalogDatabaseTargetDatabaseArgs]]: ...
    @target_database.setter
    def target_database(
        self, value: Optional[pulumi.Input[CatalogDatabaseTargetDatabaseArgs]]
    ): ...

@pulumi.type_token("aws:glue/catalogDatabase:CatalogDatabase")
class CatalogDatabase(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_table_default_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CatalogDatabaseCreateTableDefaultPermissionArgs,
                            CatalogDatabaseCreateTableDefaultPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        federated_database: Optional[
            pulumi.Input[
                Union[
                    CatalogDatabaseFederatedDatabaseArgs,
                    CatalogDatabaseFederatedDatabaseArgsDict,
                ]
            ]
        ] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_database: Optional[
            pulumi.Input[
                Union[
                    CatalogDatabaseTargetDatabaseArgs,
                    CatalogDatabaseTargetDatabaseArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[CatalogDatabaseArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_table_default_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CatalogDatabaseCreateTableDefaultPermissionArgs,
                            CatalogDatabaseCreateTableDefaultPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        federated_database: Optional[
            pulumi.Input[
                Union[
                    CatalogDatabaseFederatedDatabaseArgs,
                    CatalogDatabaseFederatedDatabaseArgsDict,
                ]
            ]
        ] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_database: Optional[
            pulumi.Input[
                Union[
                    CatalogDatabaseTargetDatabaseArgs,
                    CatalogDatabaseTargetDatabaseArgsDict,
                ]
            ]
        ] = ...,
    ) -> CatalogDatabase: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.CatalogDatabaseCreateTableDefaultPermission]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="federatedDatabase")
    def federated_database(
        self,
    ) -> pulumi.Output[Optional[outputs.CatalogDatabaseFederatedDatabase]]: ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDatabase")
    def target_database(
        self,
    ) -> pulumi.Output[Optional[outputs.CatalogDatabaseTargetDatabase]]: ...
