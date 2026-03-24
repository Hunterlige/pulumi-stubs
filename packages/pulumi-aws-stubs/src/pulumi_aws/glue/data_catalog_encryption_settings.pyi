import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataCatalogEncryptionSettingsArgs", "DataCatalogEncryptionSettings"]

@pulumi.input_type
class DataCatalogEncryptionSettingsArgs:
    def __init__(
        __self__,
        *,
        data_catalog_encryption_settings: pulumi.Input[
            DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs
        ],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(
        self,
    ) -> pulumi.Input[
        DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs
    ]: ...
    @data_catalog_encryption_settings.setter
    def data_catalog_encryption_settings(
        self,
        value: pulumi.Input[
            DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DataCatalogEncryptionSettingsState:
    def __init__(
        __self__,
        *,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_catalog_encryption_settings: Optional[
            pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(
        self,
    ) -> Optional[
        pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs]
    ]: ...
    @data_catalog_encryption_settings.setter
    def data_catalog_encryption_settings(
        self,
        value: Optional[
            pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DataCatalogEncryptionSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_catalog_encryption_settings: Optional[
            pulumi.Input[
                Union[
                    DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs,
                    DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataCatalogEncryptionSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_catalog_encryption_settings: Optional[
            pulumi.Input[
                Union[
                    DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs,
                    DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DataCatalogEncryptionSettings: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(
        self,
    ) -> pulumi.Output[
        outputs.DataCatalogEncryptionSettingsDataCatalogEncryptionSettings
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
