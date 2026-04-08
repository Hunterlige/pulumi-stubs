import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatastoreArgs", "Datastore"]

@pulumi.input_type
class DatastoreArgs:
    def __init__(
        __self__,
        *,
        properties: pulumi.Input[
            Union[
                AzureBlobDatastoreArgs,
                AzureDataLakeGen1DatastoreArgs,
                AzureDataLakeGen2DatastoreArgs,
                AzureFileDatastoreArgs,
                OneLakeDatastoreArgs,
            ]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Input[
        Union[
            AzureBlobDatastoreArgs,
            AzureDataLakeGen1DatastoreArgs,
            AzureDataLakeGen2DatastoreArgs,
            AzureFileDatastoreArgs,
            OneLakeDatastoreArgs,
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: pulumi.Input[
            Union[
                AzureBlobDatastoreArgs,
                AzureDataLakeGen1DatastoreArgs,
                AzureDataLakeGen2DatastoreArgs,
                AzureFileDatastoreArgs,
                OneLakeDatastoreArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:machinelearningservices:Datastore")
class Datastore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[AzureBlobDatastoreArgs, AzureBlobDatastoreArgsDict],
                    Union[
                        AzureDataLakeGen1DatastoreArgs,
                        AzureDataLakeGen1DatastoreArgsDict,
                    ],
                    Union[
                        AzureDataLakeGen2DatastoreArgs,
                        AzureDataLakeGen2DatastoreArgsDict,
                    ],
                    Union[AzureFileDatastoreArgs, AzureFileDatastoreArgsDict],
                    Union[OneLakeDatastoreArgs, OneLakeDatastoreArgsDict],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatastoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Datastore: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
