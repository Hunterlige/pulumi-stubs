import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FactoryArgs", "Factory"]

@pulumi.input_type
class FactoryArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        encryption: Optional[pulumi.Input[EncryptionConfigurationArgs]] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        global_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[GlobalParameterSpecificationArgs]]]
        ] = ...,
        identity: Optional[pulumi.Input[FactoryIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        purview_configuration: Optional[pulumi.Input[PurviewConfigurationArgs]] = ...,
        repo_configuration: Optional[
            pulumi.Input[
                Union[FactoryGitHubConfigurationArgs, FactoryVSTSConfigurationArgs]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionConfigurationArgs]]: ...
    @encryption.setter
    def encryption(
        self, value: Optional[pulumi.Input[EncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @factory_name.setter
    def factory_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalParameters")
    def global_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[GlobalParameterSpecificationArgs]]]
    ]: ...
    @global_parameters.setter
    def global_parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[GlobalParameterSpecificationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[FactoryIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[FactoryIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(
        self,
    ) -> Optional[pulumi.Input[PurviewConfigurationArgs]]: ...
    @purview_configuration.setter
    def purview_configuration(
        self, value: Optional[pulumi.Input[PurviewConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[FactoryGitHubConfigurationArgs, FactoryVSTSConfigurationArgs]
        ]
    ]: ...
    @repo_configuration.setter
    def repo_configuration(
        self,
        value: Optional[
            pulumi.Input[
                Union[FactoryGitHubConfigurationArgs, FactoryVSTSConfigurationArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:datafactory:Factory")
class Factory(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption: Optional[
            pulumi.Input[
                Union[EncryptionConfigurationArgs, EncryptionConfigurationArgsDict]
            ]
        ] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        global_parameters: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            GlobalParameterSpecificationArgs,
                            GlobalParameterSpecificationArgsDict,
                        ]
                    ],
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[Union[FactoryIdentityArgs, FactoryIdentityArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        purview_configuration: Optional[
            pulumi.Input[Union[PurviewConfigurationArgs, PurviewConfigurationArgsDict]]
        ] = ...,
        repo_configuration: Optional[
            pulumi.Input[
                Union[
                    Union[
                        FactoryGitHubConfigurationArgs,
                        FactoryGitHubConfigurationArgsDict,
                    ],
                    Union[
                        FactoryVSTSConfigurationArgs, FactoryVSTSConfigurationArgsDict
                    ],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FactoryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Factory: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.EncryptionConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="globalParameters")
    def global_parameters(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.GlobalParameterSpecificationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.FactoryIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.PurviewConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
