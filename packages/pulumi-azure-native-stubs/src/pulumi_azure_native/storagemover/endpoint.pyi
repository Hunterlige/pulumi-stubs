import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EndpointArgs", "Endpoint"]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        properties: pulumi.Input[
            Union[
                AzureStorageBlobContainerEndpointPropertiesArgs,
                AzureStorageSmbFileShareEndpointPropertiesArgs,
                NfsMountEndpointPropertiesArgs,
                SmbMountEndpointPropertiesArgs,
            ]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        storage_mover_name: pulumi.Input[_builtins.str],
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Input[
        Union[
            AzureStorageBlobContainerEndpointPropertiesArgs,
            AzureStorageSmbFileShareEndpointPropertiesArgs,
            NfsMountEndpointPropertiesArgs,
            SmbMountEndpointPropertiesArgs,
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: pulumi.Input[
            Union[
                AzureStorageBlobContainerEndpointPropertiesArgs,
                AzureStorageSmbFileShareEndpointPropertiesArgs,
                NfsMountEndpointPropertiesArgs,
                SmbMountEndpointPropertiesArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageMoverName")
    def storage_mover_name(self) -> pulumi.Input[_builtins.str]: ...
    @storage_mover_name.setter
    def storage_mover_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:storagemover:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[
                        AzureStorageBlobContainerEndpointPropertiesArgs,
                        AzureStorageBlobContainerEndpointPropertiesArgsDict,
                    ],
                    Union[
                        AzureStorageSmbFileShareEndpointPropertiesArgs,
                        AzureStorageSmbFileShareEndpointPropertiesArgsDict,
                    ],
                    Union[
                        NfsMountEndpointPropertiesArgs,
                        NfsMountEndpointPropertiesArgsDict,
                    ],
                    Union[
                        SmbMountEndpointPropertiesArgs,
                        SmbMountEndpointPropertiesArgsDict,
                    ],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_mover_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Endpoint: ...
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
