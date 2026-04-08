import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ArchifeArgs", "Archife"]

@pulumi.input_type
class ArchifeArgs:
    def __init__(
        __self__,
        *,
        package_type: pulumi.Input[_builtins.str],
        registry_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        archive_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_source: Optional[
            pulumi.Input[ArchivePackageSourcePropertiesArgs]
        ] = ...,
        published_version: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_endpoint_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Input[_builtins.str]: ...
    @package_type.setter
    def package_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]: ...
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveName")
    def archive_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @archive_name.setter
    def archive_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageSource")
    def package_source(
        self,
    ) -> Optional[pulumi.Input[ArchivePackageSourcePropertiesArgs]]: ...
    @package_source.setter
    def package_source(
        self, value: Optional[pulumi.Input[ArchivePackageSourcePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishedVersion")
    def published_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @published_version.setter
    def published_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpointPrefix")
    def repository_endpoint_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_endpoint_prefix.setter
    def repository_endpoint_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:containerregistry:Archife")
class Archife(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        archive_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_source: Optional[
            pulumi.Input[
                Union[
                    ArchivePackageSourcePropertiesArgs,
                    ArchivePackageSourcePropertiesArgsDict,
                ]
            ]
        ] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        published_version: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_endpoint_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ArchifeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Archife: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageSource")
    def package_source(
        self,
    ) -> pulumi.Output[Optional[outputs.ArchivePackageSourcePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishedVersion")
    def published_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpoint")
    def repository_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpointPrefix")
    def repository_endpoint_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
