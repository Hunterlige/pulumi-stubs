import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotebookInstanceArgs", "NotebookInstance"]

@pulumi.input_type
class NotebookInstanceArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        additional_code_repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_code_repository: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_internet_access: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_metadata_service_configuration: Optional[
            pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_access: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_code_repositories.setter
    def additional_code_repositories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultCodeRepository")
    def default_code_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_code_repository.setter
    def default_code_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directInternetAccess")
    def direct_internet_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direct_internet_access.setter
    def direct_internet_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceMetadataServiceConfiguration")
    def instance_metadata_service_configuration(
        self,
    ) -> Optional[
        pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
    ]: ...
    @instance_metadata_service_configuration.setter
    def instance_metadata_service_configuration(
        self,
        value: Optional[
            pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigName")
    def lifecycle_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_config_name.setter
    def lifecycle_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformIdentifier")
    def platform_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_identifier.setter
    def platform_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootAccess")
    def root_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_access.setter
    def root_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _NotebookInstanceState:
    def __init__(
        __self__,
        *,
        additional_code_repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_code_repository: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_internet_access: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_metadata_service_configuration: Optional[
            pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        root_access: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_code_repositories.setter
    def additional_code_repositories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultCodeRepository")
    def default_code_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_code_repository.setter
    def default_code_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directInternetAccess")
    def direct_internet_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direct_internet_access.setter
    def direct_internet_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceMetadataServiceConfiguration")
    def instance_metadata_service_configuration(
        self,
    ) -> Optional[
        pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
    ]: ...
    @instance_metadata_service_configuration.setter
    def instance_metadata_service_configuration(
        self,
        value: Optional[
            pulumi.Input[NotebookInstanceInstanceMetadataServiceConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigName")
    def lifecycle_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_config_name.setter
    def lifecycle_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformIdentifier")
    def platform_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_identifier.setter
    def platform_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootAccess")
    def root_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_access.setter
    def root_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:sagemaker/notebookInstance:NotebookInstance")
class NotebookInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_code_repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_code_repository: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_internet_access: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_metadata_service_configuration: Optional[
            pulumi.Input[
                Union[
                    NotebookInstanceInstanceMetadataServiceConfigurationArgs,
                    NotebookInstanceInstanceMetadataServiceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        root_access: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotebookInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_code_repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_code_repository: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_internet_access: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_metadata_service_configuration: Optional[
            pulumi.Input[
                Union[
                    NotebookInstanceInstanceMetadataServiceConfigurationArgs,
                    NotebookInstanceInstanceMetadataServiceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        root_access: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> NotebookInstance: ...
    @_builtins.property
    @pulumi.getter(name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultCodeRepository")
    def default_code_repository(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="directInternetAccess")
    def direct_internet_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceMetadataServiceConfiguration")
    def instance_metadata_service_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.NotebookInstanceInstanceMetadataServiceConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigName")
    def lifecycle_config_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformIdentifier")
    def platform_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootAccess")
    def root_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
