import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    "ArmResourceDefinitionResourceElementTemplateArgs",
    ...,
    "ArmTemplateArtifactProfileArgs",
    "ArmTemplateArtifactProfileArgsDict",
    "ArmTemplateMappingRuleProfileArgs",
    "ArmTemplateMappingRuleProfileArgsDict",
    "ArtifactManifestPropertiesFormatArgs",
    "ArtifactManifestPropertiesFormatArgsDict",
    ...,
    ...,
    "ArtifactStorePropertiesFormatArgs",
    "ArtifactStorePropertiesFormatArgsDict",
    "AzureArcK8sClusterNFVIDetailsArgs",
    "AzureArcK8sClusterNFVIDetailsArgsDict",
    "AzureArcKubernetesArtifactProfileArgs",
    "AzureArcKubernetesArtifactProfileArgsDict",
    "AzureArcKubernetesDeployMappingRuleProfileArgs",
    "AzureArcKubernetesDeployMappingRuleProfileArgsDict",
    "AzureArcKubernetesHelmApplicationArgs",
    "AzureArcKubernetesHelmApplicationArgsDict",
    "AzureArcKubernetesNetworkFunctionTemplateArgs",
    "AzureArcKubernetesNetworkFunctionTemplateArgsDict",
    "AzureCoreArmTemplateArtifactProfileArgs",
    "AzureCoreArmTemplateArtifactProfileArgsDict",
    "AzureCoreArmTemplateDeployMappingRuleProfileArgs",
    ...,
    "AzureCoreNFVIDetailsArgs",
    "AzureCoreNFVIDetailsArgsDict",
    "AzureCoreNetworkFunctionArmTemplateApplicationArgs",
    ...,
    "AzureCoreNetworkFunctionTemplateArgs",
    "AzureCoreNetworkFunctionTemplateArgsDict",
    "AzureCoreNetworkFunctionVhdApplicationArgs",
    "AzureCoreNetworkFunctionVhdApplicationArgsDict",
    "AzureCoreVhdImageArtifactProfileArgs",
    "AzureCoreVhdImageArtifactProfileArgsDict",
    "AzureCoreVhdImageDeployMappingRuleProfileArgs",
    "AzureCoreVhdImageDeployMappingRuleProfileArgsDict",
    "AzureOperatorNexusArmTemplateArtifactProfileArgs",
    ...,
    ...,
    ...,
    "AzureOperatorNexusClusterNFVIDetailsArgs",
    "AzureOperatorNexusClusterNFVIDetailsArgsDict",
    "AzureOperatorNexusImageArtifactProfileArgs",
    "AzureOperatorNexusImageArtifactProfileArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AzureOperatorNexusNetworkFunctionTemplateArgs",
    "AzureOperatorNexusNetworkFunctionTemplateArgsDict",
    "ConfigurationGroupSchemaPropertiesFormatArgs",
    "ConfigurationGroupSchemaPropertiesFormatArgsDict",
    "ConfigurationValueWithSecretsArgs",
    "ConfigurationValueWithSecretsArgsDict",
    "ConfigurationValueWithoutSecretsArgs",
    "ConfigurationValueWithoutSecretsArgsDict",
    "ContainerizedNetworkFunctionDefinitionVersionArgs",
    ...,
    "CustomProfileArgs",
    "CustomProfileArgsDict",
    "DataDiskArgs",
    "DataDiskArgsDict",
    "DependsOnProfileArgs",
    "DependsOnProfileArgsDict",
    "HelmArtifactProfileArgs",
    "HelmArtifactProfileArgsDict",
    "HelmInstallOptionsArgs",
    "HelmInstallOptionsArgsDict",
    "HelmMappingRuleProfileOptionsArgs",
    "HelmMappingRuleProfileOptionsArgsDict",
    "HelmMappingRuleProfileArgs",
    "HelmMappingRuleProfileArgsDict",
    "HelmUpgradeOptionsArgs",
    "HelmUpgradeOptionsArgsDict",
    "ImageArtifactProfileArgs",
    "ImageArtifactProfileArgsDict",
    "ImageMappingRuleProfileArgs",
    "ImageMappingRuleProfileArgsDict",
    "ImageReferenceArgs",
    "ImageReferenceArgsDict",
    "LinuxConfigurationArgs",
    "LinuxConfigurationArgsDict",
    "ManagedResourceGroupConfigurationArgs",
    "ManagedResourceGroupConfigurationArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "ManifestArtifactFormatArgs",
    "ManifestArtifactFormatArgsDict",
    "NSDArtifactProfileArgs",
    "NSDArtifactProfileArgsDict",
    "NetworkFunctionDefinitionGroupPropertiesFormatArgs",
    ...,
    ...,
    ...,
    "NetworkFunctionRoleConfigurationArgs",
    "NetworkFunctionRoleConfigurationArgsDict",
    "NetworkFunctionTemplateArgs",
    "NetworkFunctionTemplateArgsDict",
    "NetworkFunctionValueWithSecretsArgs",
    "NetworkFunctionValueWithSecretsArgsDict",
    "NetworkFunctionValueWithoutSecretsArgs",
    "NetworkFunctionValueWithoutSecretsArgsDict",
    "NetworkInterfaceIPConfigurationArgs",
    "NetworkInterfaceIPConfigurationArgsDict",
    "NetworkInterfaceArgs",
    "NetworkInterfaceArgsDict",
    "NetworkServiceDesignGroupPropertiesFormatArgs",
    "NetworkServiceDesignGroupPropertiesFormatArgsDict",
    "NetworkServiceDesignVersionPropertiesFormatArgs",
    ...,
    "NfviDetailsArgs",
    "NfviDetailsArgsDict",
    "OpenDeploymentResourceReferenceArgs",
    "OpenDeploymentResourceReferenceArgsDict",
    "OsDiskArgs",
    "OsDiskArgsDict",
    "OsProfileArgs",
    "OsProfileArgsDict",
    "PublisherPropertiesFormatArgs",
    "PublisherPropertiesFormatArgsDict",
    "ReferencedResourceArgs",
    "ReferencedResourceArgsDict",
    "SecretDeploymentResourceReferenceArgs",
    "SecretDeploymentResourceReferenceArgsDict",
    "SiteNetworkServicePropertiesFormatArgs",
    "SiteNetworkServicePropertiesFormatArgsDict",
    "SitePropertiesFormatArgs",
    "SitePropertiesFormatArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SshConfigurationArgs",
    "SshConfigurationArgsDict",
    "SshPublicKeyArgs",
    "SshPublicKeyArgsDict",
    "StorageProfileArgs",
    "StorageProfileArgsDict",
    "VhdImageArtifactProfileArgs",
    "VhdImageArtifactProfileArgsDict",
    "VhdImageMappingRuleProfileArgs",
    "VhdImageMappingRuleProfileArgsDict",
    "VirtualHardDiskArgs",
    "VirtualHardDiskArgsDict",
    ...,
    ...,
]

class ArmResourceDefinitionResourceElementTemplateDetailsArgsDict(TypedDict):
    resource_element_type: pulumi.Input[_builtins.str]
    configuration: NotRequired[
        pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArmResourceDefinitionResourceElementTemplateDetailsArgs:
    def __init__(
        __self__,
        *,
        resource_element_type: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceElementType")
    def resource_element_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_element_type.setter
    def resource_element_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]]: ...
    @configuration.setter
    def configuration(
        self,
        value: Optional[pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArmResourceDefinitionResourceElementTemplateArgsDict(TypedDict):
    artifact_profile: NotRequired[pulumi.Input[NSDArtifactProfileArgsDict]]
    parameter_values: NotRequired[pulumi.Input[_builtins.str]]
    template_type: NotRequired[pulumi.Input[Union[_builtins.str, TemplateType]]]

@pulumi.input_type
class ArmResourceDefinitionResourceElementTemplateArgs:
    def __init__(
        __self__,
        *,
        artifact_profile: Optional[pulumi.Input[NSDArtifactProfileArgs]] = ...,
        parameter_values: Optional[pulumi.Input[_builtins.str]] = ...,
        template_type: Optional[pulumi.Input[Union[_builtins.str, TemplateType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(self) -> Optional[pulumi.Input[NSDArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self, value: Optional[pulumi.Input[NSDArtifactProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameter_values.setter
    def parameter_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateType")
    def template_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TemplateType]]]: ...
    @template_type.setter
    def template_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TemplateType]]]
    ): ...

class ArmTemplateArtifactProfileArgsDict(TypedDict):
    template_name: NotRequired[pulumi.Input[_builtins.str]]
    template_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArmTemplateArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        template_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_version.setter
    def template_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArmTemplateMappingRuleProfileArgsDict(TypedDict):
    template_parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArmTemplateMappingRuleProfileArgs:
    def __init__(
        __self__, *, template_parameters: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_parameters.setter
    def template_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArtifactManifestPropertiesFormatArgsDict(TypedDict):
    artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManifestArtifactFormatArgsDict]]]
    ]

@pulumi.input_type
class ArtifactManifestPropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManifestArtifactFormatArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManifestArtifactFormatArgs]]]]: ...
    @artifacts.setter
    def artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManifestArtifactFormatArgs]]]
        ],
    ): ...

class ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArtifactStorePropertiesFormatArgsDict(TypedDict):
    backing_resource_public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, BackingResourcePublicNetworkAccess]]
    ]
    managed_resource_group_configuration: NotRequired[
        pulumi.Input[
            ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgsDict
        ]
    ]
    replication_strategy: NotRequired[
        pulumi.Input[Union[_builtins.str, ArtifactReplicationStrategy]]
    ]
    store_type: NotRequired[pulumi.Input[Union[_builtins.str, ArtifactStoreType]]]

@pulumi.input_type
class ArtifactStorePropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        backing_resource_public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, BackingResourcePublicNetworkAccess]]
        ] = ...,
        managed_resource_group_configuration: Optional[
            pulumi.Input[
                ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgs
            ]
        ] = ...,
        replication_strategy: Optional[
            pulumi.Input[Union[_builtins.str, ArtifactReplicationStrategy]]
        ] = ...,
        store_type: Optional[
            pulumi.Input[Union[_builtins.str, ArtifactStoreType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backingResourcePublicNetworkAccess")
    def backing_resource_public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, BackingResourcePublicNetworkAccess]]
    ]: ...
    @backing_resource_public_network_access.setter
    def backing_resource_public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, BackingResourcePublicNetworkAccess]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgs]
    ]: ...
    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ArtifactStorePropertiesFormatManagedResourceGroupConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationStrategy")
    def replication_strategy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ArtifactReplicationStrategy]]]: ...
    @replication_strategy.setter
    def replication_strategy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ArtifactReplicationStrategy]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storeType")
    def store_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ArtifactStoreType]]]: ...
    @store_type.setter
    def store_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ArtifactStoreType]]]
    ): ...

class AzureArcK8sClusterNFVIDetailsArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    custom_location_reference: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureArcK8sClusterNFVIDetailsArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        custom_location_reference: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customLocationReference")
    def custom_location_reference(
        self,
    ) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @custom_location_reference.setter
    def custom_location_reference(
        self, value: Optional[pulumi.Input[ReferencedResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureArcKubernetesArtifactProfileArgsDict(TypedDict):
    artifact_store: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    helm_artifact_profile: NotRequired[pulumi.Input[HelmArtifactProfileArgsDict]]

@pulumi.input_type
class AzureArcKubernetesArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_store: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        helm_artifact_profile: Optional[pulumi.Input[HelmArtifactProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="helmArtifactProfile")
    def helm_artifact_profile(
        self,
    ) -> Optional[pulumi.Input[HelmArtifactProfileArgs]]: ...
    @helm_artifact_profile.setter
    def helm_artifact_profile(
        self, value: Optional[pulumi.Input[HelmArtifactProfileArgs]]
    ): ...

class AzureArcKubernetesDeployMappingRuleProfileArgsDict(TypedDict):
    application_enablement: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
    ]
    helm_mapping_rule_profile: NotRequired[pulumi.Input[HelmMappingRuleProfileArgsDict]]

@pulumi.input_type
class AzureArcKubernetesDeployMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        application_enablement: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
        ] = ...,
        helm_mapping_rule_profile: Optional[
            pulumi.Input[HelmMappingRuleProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnablement")
    def application_enablement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]: ...
    @application_enablement.setter
    def application_enablement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="helmMappingRuleProfile")
    def helm_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[HelmMappingRuleProfileArgs]]: ...
    @helm_mapping_rule_profile.setter
    def helm_mapping_rule_profile(
        self, value: Optional[pulumi.Input[HelmMappingRuleProfileArgs]]
    ): ...

class AzureArcKubernetesHelmApplicationArgsDict(TypedDict):
    artifact_type: pulumi.Input[_builtins.str]
    artifact_profile: NotRequired[
        pulumi.Input[AzureArcKubernetesArtifactProfileArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    deploy_parameters_mapping_rule_profile: NotRequired[
        pulumi.Input[AzureArcKubernetesDeployMappingRuleProfileArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureArcKubernetesHelmApplicationArgs:
    def __init__(
        __self__,
        *,
        artifact_type: pulumi.Input[_builtins.str],
        artifact_profile: Optional[
            pulumi.Input[AzureArcKubernetesArtifactProfileArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        deploy_parameters_mapping_rule_profile: Optional[
            pulumi.Input[AzureArcKubernetesDeployMappingRuleProfileArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(
        self,
    ) -> Optional[pulumi.Input[AzureArcKubernetesArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self, value: Optional[pulumi.Input[AzureArcKubernetesArtifactProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployParametersMappingRuleProfile")
    def deploy_parameters_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[AzureArcKubernetesDeployMappingRuleProfileArgs]]: ...
    @deploy_parameters_mapping_rule_profile.setter
    def deploy_parameters_mapping_rule_profile(
        self,
        value: Optional[pulumi.Input[AzureArcKubernetesDeployMappingRuleProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureArcKubernetesNetworkFunctionTemplateArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    network_function_applications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AzureArcKubernetesHelmApplicationArgsDict]]]
    ]

@pulumi.input_type
class AzureArcKubernetesNetworkFunctionTemplateArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        network_function_applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[AzureArcKubernetesHelmApplicationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionApplications")
    def network_function_applications(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AzureArcKubernetesHelmApplicationArgs]]]
    ]: ...
    @network_function_applications.setter
    def network_function_applications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AzureArcKubernetesHelmApplicationArgs]]]
        ],
    ): ...

class AzureCoreArmTemplateArtifactProfileArgsDict(TypedDict):
    artifact_store: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    template_artifact_profile: NotRequired[
        pulumi.Input[ArmTemplateArtifactProfileArgsDict]
    ]

@pulumi.input_type
class AzureCoreArmTemplateArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_store: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        template_artifact_profile: Optional[
            pulumi.Input[ArmTemplateArtifactProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="templateArtifactProfile")
    def template_artifact_profile(
        self,
    ) -> Optional[pulumi.Input[ArmTemplateArtifactProfileArgs]]: ...
    @template_artifact_profile.setter
    def template_artifact_profile(
        self, value: Optional[pulumi.Input[ArmTemplateArtifactProfileArgs]]
    ): ...

class AzureCoreArmTemplateDeployMappingRuleProfileArgsDict(TypedDict):
    application_enablement: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
    ]
    template_mapping_rule_profile: NotRequired[
        pulumi.Input[ArmTemplateMappingRuleProfileArgsDict]
    ]

@pulumi.input_type
class AzureCoreArmTemplateDeployMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        application_enablement: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
        ] = ...,
        template_mapping_rule_profile: Optional[
            pulumi.Input[ArmTemplateMappingRuleProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnablement")
    def application_enablement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]: ...
    @application_enablement.setter
    def application_enablement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateMappingRuleProfile")
    def template_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[ArmTemplateMappingRuleProfileArgs]]: ...
    @template_mapping_rule_profile.setter
    def template_mapping_rule_profile(
        self, value: Optional[pulumi.Input[ArmTemplateMappingRuleProfileArgs]]
    ): ...

class AzureCoreNFVIDetailsArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureCoreNFVIDetailsArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureCoreNetworkFunctionArmTemplateApplicationArgsDict(TypedDict):
    artifact_type: pulumi.Input[_builtins.str]
    artifact_profile: NotRequired[
        pulumi.Input[AzureCoreArmTemplateArtifactProfileArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    deploy_parameters_mapping_rule_profile: NotRequired[
        pulumi.Input[AzureCoreArmTemplateDeployMappingRuleProfileArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureCoreNetworkFunctionArmTemplateApplicationArgs:
    def __init__(
        __self__,
        *,
        artifact_type: pulumi.Input[_builtins.str],
        artifact_profile: Optional[
            pulumi.Input[AzureCoreArmTemplateArtifactProfileArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        deploy_parameters_mapping_rule_profile: Optional[
            pulumi.Input[AzureCoreArmTemplateDeployMappingRuleProfileArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(
        self,
    ) -> Optional[pulumi.Input[AzureCoreArmTemplateArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self, value: Optional[pulumi.Input[AzureCoreArmTemplateArtifactProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployParametersMappingRuleProfile")
    def deploy_parameters_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[AzureCoreArmTemplateDeployMappingRuleProfileArgs]]: ...
    @deploy_parameters_mapping_rule_profile.setter
    def deploy_parameters_mapping_rule_profile(
        self,
        value: Optional[pulumi.Input[AzureCoreArmTemplateDeployMappingRuleProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureCoreNetworkFunctionTemplateArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    network_function_applications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureCoreNetworkFunctionArmTemplateApplicationArgsDict,
                        AzureCoreNetworkFunctionVhdApplicationArgsDict,
                    ]
                ]
            ]
        ]
    ]

@pulumi.input_type
class AzureCoreNetworkFunctionTemplateArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        network_function_applications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureCoreNetworkFunctionArmTemplateApplicationArgs,
                            AzureCoreNetworkFunctionVhdApplicationArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionApplications")
    def network_function_applications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureCoreNetworkFunctionArmTemplateApplicationArgs,
                        AzureCoreNetworkFunctionVhdApplicationArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @network_function_applications.setter
    def network_function_applications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureCoreNetworkFunctionArmTemplateApplicationArgs,
                            AzureCoreNetworkFunctionVhdApplicationArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...

class AzureCoreNetworkFunctionVhdApplicationArgsDict(TypedDict):
    artifact_type: pulumi.Input[_builtins.str]
    artifact_profile: NotRequired[
        pulumi.Input[AzureCoreVhdImageArtifactProfileArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    deploy_parameters_mapping_rule_profile: NotRequired[
        pulumi.Input[AzureCoreVhdImageDeployMappingRuleProfileArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureCoreNetworkFunctionVhdApplicationArgs:
    def __init__(
        __self__,
        *,
        artifact_type: pulumi.Input[_builtins.str],
        artifact_profile: Optional[
            pulumi.Input[AzureCoreVhdImageArtifactProfileArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        deploy_parameters_mapping_rule_profile: Optional[
            pulumi.Input[AzureCoreVhdImageDeployMappingRuleProfileArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(
        self,
    ) -> Optional[pulumi.Input[AzureCoreVhdImageArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self, value: Optional[pulumi.Input[AzureCoreVhdImageArtifactProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployParametersMappingRuleProfile")
    def deploy_parameters_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[AzureCoreVhdImageDeployMappingRuleProfileArgs]]: ...
    @deploy_parameters_mapping_rule_profile.setter
    def deploy_parameters_mapping_rule_profile(
        self,
        value: Optional[pulumi.Input[AzureCoreVhdImageDeployMappingRuleProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureCoreVhdImageArtifactProfileArgsDict(TypedDict):
    artifact_store: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    vhd_artifact_profile: NotRequired[pulumi.Input[VhdImageArtifactProfileArgsDict]]

@pulumi.input_type
class AzureCoreVhdImageArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_store: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        vhd_artifact_profile: Optional[pulumi.Input[VhdImageArtifactProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vhdArtifactProfile")
    def vhd_artifact_profile(
        self,
    ) -> Optional[pulumi.Input[VhdImageArtifactProfileArgs]]: ...
    @vhd_artifact_profile.setter
    def vhd_artifact_profile(
        self, value: Optional[pulumi.Input[VhdImageArtifactProfileArgs]]
    ): ...

class AzureCoreVhdImageDeployMappingRuleProfileArgsDict(TypedDict):
    application_enablement: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
    ]
    vhd_image_mapping_rule_profile: NotRequired[
        pulumi.Input[VhdImageMappingRuleProfileArgsDict]
    ]

@pulumi.input_type
class AzureCoreVhdImageDeployMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        application_enablement: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
        ] = ...,
        vhd_image_mapping_rule_profile: Optional[
            pulumi.Input[VhdImageMappingRuleProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnablement")
    def application_enablement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]: ...
    @application_enablement.setter
    def application_enablement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vhdImageMappingRuleProfile")
    def vhd_image_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[VhdImageMappingRuleProfileArgs]]: ...
    @vhd_image_mapping_rule_profile.setter
    def vhd_image_mapping_rule_profile(
        self, value: Optional[pulumi.Input[VhdImageMappingRuleProfileArgs]]
    ): ...

class AzureOperatorNexusArmTemplateArtifactProfileArgsDict(TypedDict):
    artifact_store: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    template_artifact_profile: NotRequired[
        pulumi.Input[ArmTemplateArtifactProfileArgsDict]
    ]

@pulumi.input_type
class AzureOperatorNexusArmTemplateArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_store: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        template_artifact_profile: Optional[
            pulumi.Input[ArmTemplateArtifactProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="templateArtifactProfile")
    def template_artifact_profile(
        self,
    ) -> Optional[pulumi.Input[ArmTemplateArtifactProfileArgs]]: ...
    @template_artifact_profile.setter
    def template_artifact_profile(
        self, value: Optional[pulumi.Input[ArmTemplateArtifactProfileArgs]]
    ): ...

class AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgsDict(TypedDict):
    application_enablement: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
    ]
    template_mapping_rule_profile: NotRequired[
        pulumi.Input[ArmTemplateMappingRuleProfileArgsDict]
    ]

@pulumi.input_type
class AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        application_enablement: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
        ] = ...,
        template_mapping_rule_profile: Optional[
            pulumi.Input[ArmTemplateMappingRuleProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnablement")
    def application_enablement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]: ...
    @application_enablement.setter
    def application_enablement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateMappingRuleProfile")
    def template_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[ArmTemplateMappingRuleProfileArgs]]: ...
    @template_mapping_rule_profile.setter
    def template_mapping_rule_profile(
        self, value: Optional[pulumi.Input[ArmTemplateMappingRuleProfileArgs]]
    ): ...

class AzureOperatorNexusClusterNFVIDetailsArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    custom_location_reference: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureOperatorNexusClusterNFVIDetailsArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        custom_location_reference: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customLocationReference")
    def custom_location_reference(
        self,
    ) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @custom_location_reference.setter
    def custom_location_reference(
        self, value: Optional[pulumi.Input[ReferencedResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureOperatorNexusImageArtifactProfileArgsDict(TypedDict):
    artifact_store: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    image_artifact_profile: NotRequired[pulumi.Input[ImageArtifactProfileArgsDict]]

@pulumi.input_type
class AzureOperatorNexusImageArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_store: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        image_artifact_profile: Optional[pulumi.Input[ImageArtifactProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="imageArtifactProfile")
    def image_artifact_profile(
        self,
    ) -> Optional[pulumi.Input[ImageArtifactProfileArgs]]: ...
    @image_artifact_profile.setter
    def image_artifact_profile(
        self, value: Optional[pulumi.Input[ImageArtifactProfileArgs]]
    ): ...

class AzureOperatorNexusImageDeployMappingRuleProfileArgsDict(TypedDict):
    application_enablement: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
    ]
    image_mapping_rule_profile: NotRequired[
        pulumi.Input[ImageMappingRuleProfileArgsDict]
    ]

@pulumi.input_type
class AzureOperatorNexusImageDeployMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        application_enablement: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationEnablement]]
        ] = ...,
        image_mapping_rule_profile: Optional[
            pulumi.Input[ImageMappingRuleProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEnablement")
    def application_enablement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]: ...
    @application_enablement.setter
    def application_enablement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationEnablement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageMappingRuleProfile")
    def image_mapping_rule_profile(
        self,
    ) -> Optional[pulumi.Input[ImageMappingRuleProfileArgs]]: ...
    @image_mapping_rule_profile.setter
    def image_mapping_rule_profile(
        self, value: Optional[pulumi.Input[ImageMappingRuleProfileArgs]]
    ): ...

class AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgsDict(TypedDict):
    artifact_type: pulumi.Input[_builtins.str]
    artifact_profile: NotRequired[
        pulumi.Input[AzureOperatorNexusArmTemplateArtifactProfileArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    deploy_parameters_mapping_rule_profile: NotRequired[
        pulumi.Input[AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgs:
    def __init__(
        __self__,
        *,
        artifact_type: pulumi.Input[_builtins.str],
        artifact_profile: Optional[
            pulumi.Input[AzureOperatorNexusArmTemplateArtifactProfileArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        deploy_parameters_mapping_rule_profile: Optional[
            pulumi.Input[AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(
        self,
    ) -> Optional[pulumi.Input[AzureOperatorNexusArmTemplateArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self,
        value: Optional[pulumi.Input[AzureOperatorNexusArmTemplateArtifactProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployParametersMappingRuleProfile")
    def deploy_parameters_mapping_rule_profile(
        self,
    ) -> Optional[
        pulumi.Input[AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgs]
    ]: ...
    @deploy_parameters_mapping_rule_profile.setter
    def deploy_parameters_mapping_rule_profile(
        self,
        value: Optional[
            pulumi.Input[AzureOperatorNexusArmTemplateDeployMappingRuleProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureOperatorNexusNetworkFunctionImageApplicationArgsDict(TypedDict):
    artifact_type: pulumi.Input[_builtins.str]
    artifact_profile: NotRequired[
        pulumi.Input[AzureOperatorNexusImageArtifactProfileArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    deploy_parameters_mapping_rule_profile: NotRequired[
        pulumi.Input[AzureOperatorNexusImageDeployMappingRuleProfileArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureOperatorNexusNetworkFunctionImageApplicationArgs:
    def __init__(
        __self__,
        *,
        artifact_type: pulumi.Input[_builtins.str],
        artifact_profile: Optional[
            pulumi.Input[AzureOperatorNexusImageArtifactProfileArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        deploy_parameters_mapping_rule_profile: Optional[
            pulumi.Input[AzureOperatorNexusImageDeployMappingRuleProfileArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactProfile")
    def artifact_profile(
        self,
    ) -> Optional[pulumi.Input[AzureOperatorNexusImageArtifactProfileArgs]]: ...
    @artifact_profile.setter
    def artifact_profile(
        self, value: Optional[pulumi.Input[AzureOperatorNexusImageArtifactProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployParametersMappingRuleProfile")
    def deploy_parameters_mapping_rule_profile(
        self,
    ) -> Optional[
        pulumi.Input[AzureOperatorNexusImageDeployMappingRuleProfileArgs]
    ]: ...
    @deploy_parameters_mapping_rule_profile.setter
    def deploy_parameters_mapping_rule_profile(
        self,
        value: Optional[
            pulumi.Input[AzureOperatorNexusImageDeployMappingRuleProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureOperatorNexusNetworkFunctionTemplateArgsDict(TypedDict):
    nfvi_type: pulumi.Input[_builtins.str]
    network_function_applications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgsDict,
                        AzureOperatorNexusNetworkFunctionImageApplicationArgsDict,
                    ]
                ]
            ]
        ]
    ]

@pulumi.input_type
class AzureOperatorNexusNetworkFunctionTemplateArgs:
    def __init__(
        __self__,
        *,
        nfvi_type: pulumi.Input[_builtins.str],
        network_function_applications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgs,
                            AzureOperatorNexusNetworkFunctionImageApplicationArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> pulumi.Input[_builtins.str]: ...
    @nfvi_type.setter
    def nfvi_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionApplications")
    def network_function_applications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgs,
                        AzureOperatorNexusNetworkFunctionImageApplicationArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @network_function_applications.setter
    def network_function_applications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureOperatorNexusNetworkFunctionArmTemplateApplicationArgs,
                            AzureOperatorNexusNetworkFunctionImageApplicationArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...

class ConfigurationGroupSchemaPropertiesFormatArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    schema_definition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationGroupSchemaPropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_definition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigurationValueWithSecretsArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    configuration_group_schema_resource_reference: NotRequired[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgsDict,
                SecretDeploymentResourceReferenceArgsDict,
            ]
        ]
    ]
    secret_configuration_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationValueWithSecretsArgs:
    def __init__(
        __self__,
        *,
        configuration_type: pulumi.Input[_builtins.str],
        configuration_group_schema_resource_reference: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ] = ...,
        secret_configuration_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationGroupSchemaResourceReference")
    def configuration_group_schema_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgs,
                SecretDeploymentResourceReferenceArgs,
            ]
        ]
    ]: ...
    @configuration_group_schema_resource_reference.setter
    def configuration_group_schema_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretConfigurationValue")
    def secret_configuration_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_configuration_value.setter
    def secret_configuration_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConfigurationValueWithoutSecretsArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    configuration_group_schema_resource_reference: NotRequired[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgsDict,
                SecretDeploymentResourceReferenceArgsDict,
            ]
        ]
    ]
    configuration_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationValueWithoutSecretsArgs:
    def __init__(
        __self__,
        *,
        configuration_type: pulumi.Input[_builtins.str],
        configuration_group_schema_resource_reference: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ] = ...,
        configuration_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationGroupSchemaResourceReference")
    def configuration_group_schema_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgs,
                SecretDeploymentResourceReferenceArgs,
            ]
        ]
    ]: ...
    @configuration_group_schema_resource_reference.setter
    def configuration_group_schema_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="configurationValue")
    def configuration_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_value.setter
    def configuration_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerizedNetworkFunctionDefinitionVersionArgsDict(TypedDict):
    network_function_type: pulumi.Input[_builtins.str]
    deploy_parameters: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    network_function_template: NotRequired[
        pulumi.Input[AzureArcKubernetesNetworkFunctionTemplateArgsDict]
    ]

@pulumi.input_type
class ContainerizedNetworkFunctionDefinitionVersionArgs:
    def __init__(
        __self__,
        *,
        network_function_type: pulumi.Input[_builtins.str],
        deploy_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        network_function_template: Optional[
            pulumi.Input[AzureArcKubernetesNetworkFunctionTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> pulumi.Input[_builtins.str]: ...
    @network_function_type.setter
    def network_function_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deploy_parameters.setter
    def deploy_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionTemplate")
    def network_function_template(
        self,
    ) -> Optional[pulumi.Input[AzureArcKubernetesNetworkFunctionTemplateArgs]]: ...
    @network_function_template.setter
    def network_function_template(
        self,
        value: Optional[pulumi.Input[AzureArcKubernetesNetworkFunctionTemplateArgs]],
    ): ...

class CustomProfileArgsDict(TypedDict):
    metadata_configuration_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomProfileArgs:
    def __init__(
        __self__,
        *,
        metadata_configuration_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataConfigurationPath")
    def metadata_configuration_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_configuration_path.setter
    def metadata_configuration_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DataDiskArgsDict(TypedDict):
    create_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    ]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataDiskArgs:
    def __init__(
        __self__,
        *,
        create_option: Optional[
            pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]]: ...
    @create_option.setter
    def create_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DependsOnProfileArgsDict(TypedDict):
    install_depends_on: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    uninstall_depends_on: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    update_depends_on: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DependsOnProfileArgs:
    def __init__(
        __self__,
        *,
        install_depends_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        uninstall_depends_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_depends_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="installDependsOn")
    def install_depends_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @install_depends_on.setter
    def install_depends_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uninstallDependsOn")
    def uninstall_depends_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @uninstall_depends_on.setter
    def uninstall_depends_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateDependsOn")
    def update_depends_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @update_depends_on.setter
    def update_depends_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HelmArtifactProfileArgsDict(TypedDict):
    helm_package_name: NotRequired[pulumi.Input[_builtins.str]]
    helm_package_version_range: NotRequired[pulumi.Input[_builtins.str]]
    image_pull_secrets_values_paths: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    registry_values_paths: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class HelmArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        helm_package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        helm_package_version_range: Optional[pulumi.Input[_builtins.str]] = ...,
        image_pull_secrets_values_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        registry_values_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="helmPackageName")
    def helm_package_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @helm_package_name.setter
    def helm_package_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="helmPackageVersionRange")
    def helm_package_version_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @helm_package_version_range.setter
    def helm_package_version_range(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imagePullSecretsValuesPaths")
    def image_pull_secrets_values_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @image_pull_secrets_values_paths.setter
    def image_pull_secrets_values_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="registryValuesPaths")
    def registry_values_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @registry_values_paths.setter
    def registry_values_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HelmInstallOptionsArgsDict(TypedDict):
    atomic: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    wait: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HelmInstallOptionsArgs:
    def __init__(
        __self__,
        *,
        atomic: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        wait: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def atomic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @atomic.setter
    def atomic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait.setter
    def wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HelmMappingRuleProfileOptionsArgsDict(TypedDict):
    install_options: NotRequired[pulumi.Input[HelmInstallOptionsArgsDict]]
    upgrade_options: NotRequired[pulumi.Input[HelmUpgradeOptionsArgsDict]]

@pulumi.input_type
class HelmMappingRuleProfileOptionsArgs:
    def __init__(
        __self__,
        *,
        install_options: Optional[pulumi.Input[HelmInstallOptionsArgs]] = ...,
        upgrade_options: Optional[pulumi.Input[HelmUpgradeOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="installOptions")
    def install_options(self) -> Optional[pulumi.Input[HelmInstallOptionsArgs]]: ...
    @install_options.setter
    def install_options(
        self, value: Optional[pulumi.Input[HelmInstallOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeOptions")
    def upgrade_options(self) -> Optional[pulumi.Input[HelmUpgradeOptionsArgs]]: ...
    @upgrade_options.setter
    def upgrade_options(
        self, value: Optional[pulumi.Input[HelmUpgradeOptionsArgs]]
    ): ...

class HelmMappingRuleProfileArgsDict(TypedDict):
    helm_package_version: NotRequired[pulumi.Input[_builtins.str]]
    options: NotRequired[pulumi.Input[HelmMappingRuleProfileOptionsArgsDict]]
    release_name: NotRequired[pulumi.Input[_builtins.str]]
    release_namespace: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HelmMappingRuleProfileArgs:
    def __init__(
        __self__,
        *,
        helm_package_version: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[HelmMappingRuleProfileOptionsArgs]] = ...,
        release_name: Optional[pulumi.Input[_builtins.str]] = ...,
        release_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="helmPackageVersion")
    def helm_package_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @helm_package_version.setter
    def helm_package_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[HelmMappingRuleProfileOptionsArgs]]: ...
    @options.setter
    def options(
        self, value: Optional[pulumi.Input[HelmMappingRuleProfileOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="releaseName")
    def release_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_name.setter
    def release_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseNamespace")
    def release_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_namespace.setter
    def release_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @values.setter
    def values(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HelmUpgradeOptionsArgsDict(TypedDict):
    atomic: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    wait: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HelmUpgradeOptionsArgs:
    def __init__(
        __self__,
        *,
        atomic: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        wait: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def atomic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @atomic.setter
    def atomic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait.setter
    def wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageArtifactProfileArgsDict(TypedDict):
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    image_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        image_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_version.setter
    def image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageMappingRuleProfileArgsDict(TypedDict):
    user_configuration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageMappingRuleProfileArgs:
    def __init__(
        __self__, *, user_configuration: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userConfiguration")
    def user_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_configuration.setter
    def user_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageReferenceArgsDict(TypedDict):
    exact_version: NotRequired[pulumi.Input[_builtins.str]]
    offer: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageReferenceArgs:
    def __init__(
        __self__,
        *,
        exact_version: Optional[pulumi.Input[_builtins.str]] = ...,
        offer: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact_version.setter
    def exact_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinuxConfigurationArgsDict(TypedDict):
    ssh: NotRequired[pulumi.Input[SshConfigurationArgsDict]]

@pulumi.input_type
class LinuxConfigurationArgs:
    def __init__(
        __self__, *, ssh: Optional[pulumi.Input[SshConfigurationArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[pulumi.Input[SshConfigurationArgs]]: ...
    @ssh.setter
    def ssh(self, value: Optional[pulumi.Input[SshConfigurationArgs]]): ...

class ManagedResourceGroupConfigurationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedResourceGroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ManifestArtifactFormatArgsDict(TypedDict):
    artifact_name: NotRequired[pulumi.Input[_builtins.str]]
    artifact_type: NotRequired[pulumi.Input[Union[_builtins.str, ArtifactType]]]
    artifact_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManifestArtifactFormatArgs:
    def __init__(
        __self__,
        *,
        artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_type: Optional[pulumi.Input[Union[_builtins.str, ArtifactType]]] = ...,
        artifact_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactName")
    def artifact_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_name.setter
    def artifact_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ArtifactType]]]: ...
    @artifact_type.setter
    def artifact_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ArtifactType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="artifactVersion")
    def artifact_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_version.setter
    def artifact_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NSDArtifactProfileArgsDict(TypedDict):
    artifact_name: NotRequired[pulumi.Input[_builtins.str]]
    artifact_store_reference: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]
    artifact_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NSDArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_store_reference: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
        artifact_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactName")
    def artifact_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_name.setter
    def artifact_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactStoreReference")
    def artifact_store_reference(
        self,
    ) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @artifact_store_reference.setter
    def artifact_store_reference(
        self, value: Optional[pulumi.Input[ReferencedResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="artifactVersion")
    def artifact_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_version.setter
    def artifact_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkFunctionDefinitionGroupPropertiesFormatArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkFunctionDefinitionGroupPropertiesFormatArgs:
    def __init__(
        __self__, *, description: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkFunctionDefinitionResourceElementTemplateDetailsArgsDict(TypedDict):
    resource_element_type: pulumi.Input[_builtins.str]
    configuration: NotRequired[
        pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgsDict]
    ]
    depends_on_profile: NotRequired[pulumi.Input[DependsOnProfileArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkFunctionDefinitionResourceElementTemplateDetailsArgs:
    def __init__(
        __self__,
        *,
        resource_element_type: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]
        ] = ...,
        depends_on_profile: Optional[pulumi.Input[DependsOnProfileArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceElementType")
    def resource_element_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_element_type.setter
    def resource_element_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]]: ...
    @configuration.setter
    def configuration(
        self,
        value: Optional[pulumi.Input[ArmResourceDefinitionResourceElementTemplateArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnProfile")
    def depends_on_profile(self) -> Optional[pulumi.Input[DependsOnProfileArgs]]: ...
    @depends_on_profile.setter
    def depends_on_profile(
        self, value: Optional[pulumi.Input[DependsOnProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkFunctionRoleConfigurationArgsDict(TypedDict):
    custom_profile: NotRequired[pulumi.Input[CustomProfileArgsDict]]
    network_interfaces: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgsDict]]]
    ]
    os_profile: NotRequired[pulumi.Input[OsProfileArgsDict]]
    role_name: NotRequired[pulumi.Input[_builtins.str]]
    role_type: NotRequired[
        pulumi.Input[Union[_builtins.str, NetworkFunctionRoleConfigurationType]]
    ]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    user_data_parameters: NotRequired[Any]
    user_data_template: NotRequired[Any]
    virtual_machine_size: NotRequired[
        pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]
    ]

@pulumi.input_type
class NetworkFunctionRoleConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_profile: Optional[pulumi.Input[CustomProfileArgs]] = ...,
        network_interfaces: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]
        ] = ...,
        os_profile: Optional[pulumi.Input[OsProfileArgs]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role_type: Optional[
            pulumi.Input[Union[_builtins.str, NetworkFunctionRoleConfigurationType]]
        ] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
        user_data_parameters: Optional[Any] = ...,
        user_data_template: Optional[Any] = ...,
        virtual_machine_size: Optional[
            pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customProfile")
    def custom_profile(self) -> Optional[pulumi.Input[CustomProfileArgs]]: ...
    @custom_profile.setter
    def custom_profile(self, value: Optional[pulumi.Input[CustomProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OsProfileArgs]]: ...
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OsProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, NetworkFunctionRoleConfigurationType]]
    ]: ...
    @role_type.setter
    def role_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NetworkFunctionRoleConfigurationType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userDataParameters")
    def user_data_parameters(self) -> Optional[Any]: ...
    @user_data_parameters.setter
    def user_data_parameters(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="userDataTemplate")
    def user_data_template(self) -> Optional[Any]: ...
    @user_data_template.setter
    def user_data_template(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineSize")
    def virtual_machine_size(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]]: ...
    @virtual_machine_size.setter
    def virtual_machine_size(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]],
    ): ...

class NetworkFunctionTemplateArgsDict(TypedDict):
    network_function_role_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkFunctionRoleConfigurationArgsDict]]]
    ]

@pulumi.input_type
class NetworkFunctionTemplateArgs:
    def __init__(
        __self__,
        *,
        network_function_role_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkFunctionRoleConfigurationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionRoleConfigurations")
    def network_function_role_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NetworkFunctionRoleConfigurationArgs]]]
    ]: ...
    @network_function_role_configurations.setter
    def network_function_role_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkFunctionRoleConfigurationArgs]]]
        ],
    ): ...

class NetworkFunctionValueWithSecretsArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    allow_software_update: NotRequired[pulumi.Input[_builtins.bool]]
    network_function_definition_group_name: NotRequired[pulumi.Input[_builtins.str]]
    network_function_definition_offering_location: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    network_function_definition_version: NotRequired[pulumi.Input[_builtins.str]]
    network_function_definition_version_resource_reference: NotRequired[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgsDict,
                SecretDeploymentResourceReferenceArgsDict,
            ]
        ]
    ]
    nfvi_id: NotRequired[pulumi.Input[_builtins.str]]
    nfvi_type: NotRequired[pulumi.Input[Union[_builtins.str, NFVIType]]]
    publisher_name: NotRequired[pulumi.Input[_builtins.str]]
    publisher_scope: NotRequired[pulumi.Input[Union[_builtins.str, PublisherScope]]]
    role_override_values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    secret_deployment_values: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkFunctionValueWithSecretsArgs:
    def __init__(
        __self__,
        *,
        configuration_type: pulumi.Input[_builtins.str],
        allow_software_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_function_definition_group_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_offering_location: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_version_resource_reference: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ] = ...,
        nfvi_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nfvi_type: Optional[pulumi.Input[Union[_builtins.str, NFVIType]]] = ...,
        publisher_name: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher_scope: Optional[
            pulumi.Input[Union[_builtins.str, PublisherScope]]
        ] = ...,
        role_override_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        secret_deployment_values: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowSoftwareUpdate")
    def allow_software_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_software_update.setter
    def allow_software_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionGroupName")
    def network_function_definition_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_group_name.setter
    def network_function_definition_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionOfferingLocation")
    def network_function_definition_offering_location(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_offering_location.setter
    def network_function_definition_offering_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionVersion")
    def network_function_definition_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_version.setter
    def network_function_definition_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionVersionResourceReference")
    def network_function_definition_version_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgs,
                SecretDeploymentResourceReferenceArgs,
            ]
        ]
    ]: ...
    @network_function_definition_version_resource_reference.setter
    def network_function_definition_version_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nfviId")
    def nfvi_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nfvi_id.setter
    def nfvi_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> Optional[pulumi.Input[Union[_builtins.str, NFVIType]]]: ...
    @nfvi_type.setter
    def nfvi_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NFVIType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher_name.setter
    def publisher_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publisherScope")
    def publisher_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]: ...
    @publisher_scope.setter
    def publisher_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleOverrideValues")
    def role_override_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @role_override_values.setter
    def role_override_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretDeploymentValues")
    def secret_deployment_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_deployment_values.setter
    def secret_deployment_values(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NetworkFunctionValueWithoutSecretsArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    allow_software_update: NotRequired[pulumi.Input[_builtins.bool]]
    deployment_values: NotRequired[pulumi.Input[_builtins.str]]
    network_function_definition_group_name: NotRequired[pulumi.Input[_builtins.str]]
    network_function_definition_offering_location: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    network_function_definition_version: NotRequired[pulumi.Input[_builtins.str]]
    network_function_definition_version_resource_reference: NotRequired[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgsDict,
                SecretDeploymentResourceReferenceArgsDict,
            ]
        ]
    ]
    nfvi_id: NotRequired[pulumi.Input[_builtins.str]]
    nfvi_type: NotRequired[pulumi.Input[Union[_builtins.str, NFVIType]]]
    publisher_name: NotRequired[pulumi.Input[_builtins.str]]
    publisher_scope: NotRequired[pulumi.Input[Union[_builtins.str, PublisherScope]]]
    role_override_values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class NetworkFunctionValueWithoutSecretsArgs:
    def __init__(
        __self__,
        *,
        configuration_type: pulumi.Input[_builtins.str],
        allow_software_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployment_values: Optional[pulumi.Input[_builtins.str]] = ...,
        network_function_definition_group_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_offering_location: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_function_definition_version_resource_reference: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ] = ...,
        nfvi_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nfvi_type: Optional[pulumi.Input[Union[_builtins.str, NFVIType]]] = ...,
        publisher_name: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher_scope: Optional[
            pulumi.Input[Union[_builtins.str, PublisherScope]]
        ] = ...,
        role_override_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowSoftwareUpdate")
    def allow_software_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_software_update.setter
    def allow_software_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentValues")
    def deployment_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_values.setter
    def deployment_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionGroupName")
    def network_function_definition_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_group_name.setter
    def network_function_definition_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionOfferingLocation")
    def network_function_definition_offering_location(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_offering_location.setter
    def network_function_definition_offering_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionVersion")
    def network_function_definition_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_function_definition_version.setter
    def network_function_definition_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionDefinitionVersionResourceReference")
    def network_function_definition_version_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgs,
                SecretDeploymentResourceReferenceArgs,
            ]
        ]
    ]: ...
    @network_function_definition_version_resource_reference.setter
    def network_function_definition_version_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nfviId")
    def nfvi_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nfvi_id.setter
    def nfvi_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfviType")
    def nfvi_type(self) -> Optional[pulumi.Input[Union[_builtins.str, NFVIType]]]: ...
    @nfvi_type.setter
    def nfvi_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NFVIType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher_name.setter
    def publisher_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publisherScope")
    def publisher_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]: ...
    @publisher_scope.setter
    def publisher_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleOverrideValues")
    def role_override_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @role_override_values.setter
    def role_override_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NetworkInterfaceIPConfigurationArgsDict(TypedDict):
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    gateway: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    ip_allocation_method: NotRequired[
        pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
    ]
    ip_version: NotRequired[pulumi.Input[Union[_builtins.str, IPVersion]]]
    subnet: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkInterfaceIPConfigurationArgs:
    def __init__(
        __self__,
        *,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
        ] = ...,
        ip_version: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAllocationMethod")
    def ip_allocation_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]: ...
    @ip_allocation_method.setter
    def ip_allocation_method(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]: ...
    @ip_version.setter
    def ip_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkInterfaceArgsDict(TypedDict):
    ip_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceIPConfigurationArgsDict]]]
    ]
    mac_address: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_name: NotRequired[pulumi.Input[_builtins.str]]
    vm_switch_type: NotRequired[pulumi.Input[Union[_builtins.str, VMSwitchType]]]

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        ip_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceIPConfigurationArgs]]]
        ] = ...,
        mac_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_switch_type: Optional[
            pulumi.Input[Union[_builtins.str, VMSwitchType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceIPConfigurationArgs]]]
    ]: ...
    @ip_configurations.setter
    def ip_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceIPConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceName")
    def network_interface_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_name.setter
    def network_interface_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmSwitchType")
    def vm_switch_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VMSwitchType]]]: ...
    @vm_switch_type.setter
    def vm_switch_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VMSwitchType]]]
    ): ...

class NetworkServiceDesignGroupPropertiesFormatArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkServiceDesignGroupPropertiesFormatArgs:
    def __init__(
        __self__, *, description: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkServiceDesignVersionPropertiesFormatArgsDict(TypedDict):
    configuration_group_schema_references: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgsDict]]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    nfvis_from_site: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[NfviDetailsArgsDict]]]
    ]
    resource_element_templates: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ArmResourceDefinitionResourceElementTemplateDetailsArgsDict,
                        NetworkFunctionDefinitionResourceElementTemplateDetailsArgsDict,
                    ]
                ]
            ]
        ]
    ]

@pulumi.input_type
class NetworkServiceDesignVersionPropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        configuration_group_schema_references: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        nfvis_from_site: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[NfviDetailsArgs]]]
        ] = ...,
        resource_element_templates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ArmResourceDefinitionResourceElementTemplateDetailsArgs,
                            NetworkFunctionDefinitionResourceElementTemplateDetailsArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationGroupSchemaReferences")
    def configuration_group_schema_references(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]]: ...
    @configuration_group_schema_references.setter
    def configuration_group_schema_references(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfvisFromSite")
    def nfvis_from_site(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[NfviDetailsArgs]]]]: ...
    @nfvis_from_site.setter
    def nfvis_from_site(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[NfviDetailsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceElementTemplates")
    def resource_element_templates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ArmResourceDefinitionResourceElementTemplateDetailsArgs,
                        NetworkFunctionDefinitionResourceElementTemplateDetailsArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @resource_element_templates.setter
    def resource_element_templates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ArmResourceDefinitionResourceElementTemplateDetailsArgs,
                            NetworkFunctionDefinitionResourceElementTemplateDetailsArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...

class NfviDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NfviDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OpenDeploymentResourceReferenceArgsDict(TypedDict):
    id_type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OpenDeploymentResourceReferenceArgs:
    def __init__(
        __self__,
        *,
        id_type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idType")
    def id_type(self) -> pulumi.Input[_builtins.str]: ...
    @id_type.setter
    def id_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsDiskArgsDict(TypedDict):
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]
    vhd: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]

@pulumi.input_type
class OsDiskArgs:
    def __init__(
        __self__,
        *,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_type: Optional[
            pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]
        ] = ...,
        vhd: Optional[pulumi.Input[VirtualHardDiskArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]: ...
    @os_type.setter
    def os_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def vhd(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]: ...
    @vhd.setter
    def vhd(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): ...

class OsProfileArgsDict(TypedDict):
    admin_username: NotRequired[pulumi.Input[_builtins.str]]
    custom_data: NotRequired[pulumi.Input[_builtins.str]]
    custom_data_required: NotRequired[pulumi.Input[_builtins.bool]]
    linux_configuration: NotRequired[pulumi.Input[LinuxConfigurationArgsDict]]

@pulumi.input_type
class OsProfileArgs:
    def __init__(
        __self__,
        *,
        admin_username: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_data: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_data_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        linux_configuration: Optional[pulumi.Input[LinuxConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDataRequired")
    def custom_data_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @custom_data_required.setter
    def custom_data_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[pulumi.Input[LinuxConfigurationArgs]]: ...
    @linux_configuration.setter
    def linux_configuration(
        self, value: Optional[pulumi.Input[LinuxConfigurationArgs]]
    ): ...

class PublisherPropertiesFormatArgsDict(TypedDict):
    scope: NotRequired[pulumi.Input[Union[_builtins.str, PublisherScope]]]

@pulumi.input_type
class PublisherPropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        scope: Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]: ...
    @scope.setter
    def scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublisherScope]]]
    ): ...

class ReferencedResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReferencedResourceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecretDeploymentResourceReferenceArgsDict(TypedDict):
    id_type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretDeploymentResourceReferenceArgs:
    def __init__(
        __self__,
        *,
        id_type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idType")
    def id_type(self) -> pulumi.Input[_builtins.str]: ...
    @id_type.setter
    def id_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SiteNetworkServicePropertiesFormatArgsDict(TypedDict):
    desired_state_configuration_group_value_references: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgsDict]]]
    ]
    managed_resource_group_configuration: NotRequired[
        pulumi.Input[ManagedResourceGroupConfigurationArgsDict]
    ]
    network_service_design_version_resource_reference: NotRequired[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgsDict,
                SecretDeploymentResourceReferenceArgsDict,
            ]
        ]
    ]
    site_reference: NotRequired[pulumi.Input[ReferencedResourceArgsDict]]

@pulumi.input_type
class SiteNetworkServicePropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        desired_state_configuration_group_value_references: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]
        ] = ...,
        managed_resource_group_configuration: Optional[
            pulumi.Input[ManagedResourceGroupConfigurationArgs]
        ] = ...,
        network_service_design_version_resource_reference: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ] = ...,
        site_reference: Optional[pulumi.Input[ReferencedResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredStateConfigurationGroupValueReferences")
    def desired_state_configuration_group_value_references(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]]: ...
    @desired_state_configuration_group_value_references.setter
    def desired_state_configuration_group_value_references(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReferencedResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]: ...
    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(
        self, value: Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkServiceDesignVersionResourceReference")
    def network_service_design_version_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                OpenDeploymentResourceReferenceArgs,
                SecretDeploymentResourceReferenceArgs,
            ]
        ]
    ]: ...
    @network_service_design_version_resource_reference.setter
    def network_service_design_version_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    OpenDeploymentResourceReferenceArgs,
                    SecretDeploymentResourceReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteReference")
    def site_reference(self) -> Optional[pulumi.Input[ReferencedResourceArgs]]: ...
    @site_reference.setter
    def site_reference(self, value: Optional[pulumi.Input[ReferencedResourceArgs]]): ...

class SitePropertiesFormatArgsDict(TypedDict):
    nfvis: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureArcK8sClusterNFVIDetailsArgsDict,
                        AzureCoreNFVIDetailsArgsDict,
                        AzureOperatorNexusClusterNFVIDetailsArgsDict,
                    ]
                ]
            ]
        ]
    ]

@pulumi.input_type
class SitePropertiesFormatArgs:
    def __init__(
        __self__,
        *,
        nfvis: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureArcK8sClusterNFVIDetailsArgs,
                            AzureCoreNFVIDetailsArgs,
                            AzureOperatorNexusClusterNFVIDetailsArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def nfvis(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AzureArcK8sClusterNFVIDetailsArgs,
                        AzureCoreNFVIDetailsArgs,
                        AzureOperatorNexusClusterNFVIDetailsArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @nfvis.setter
    def nfvis(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AzureArcK8sClusterNFVIDetailsArgs,
                            AzureCoreNFVIDetailsArgs,
                            AzureOperatorNexusClusterNFVIDetailsArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...

class SshConfigurationArgsDict(TypedDict):
    public_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgsDict]]]]

@pulumi.input_type
class SshConfigurationArgs:
    def __init__(
        __self__,
        *,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]: ...
    @public_keys.setter
    def public_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]
    ): ...

class SshPublicKeyArgsDict(TypedDict):
    key_data: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(
        __self__,
        *,
        key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_data.setter
    def key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageProfileArgsDict(TypedDict):
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataDiskArgsDict]]]]
    image_reference: NotRequired[pulumi.Input[ImageReferenceArgsDict]]
    os_disk: NotRequired[pulumi.Input[OsDiskArgsDict]]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(
        __self__,
        *,
        data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]] = ...,
        image_reference: Optional[pulumi.Input[ImageReferenceArgs]] = ...,
        os_disk: Optional[pulumi.Input[OsDiskArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]: ...
    @data_disks.setter
    def data_disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[pulumi.Input[ImageReferenceArgs]]: ...
    @image_reference.setter
    def image_reference(self, value: Optional[pulumi.Input[ImageReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[OsDiskArgs]]: ...
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[OsDiskArgs]]): ...

class VhdImageArtifactProfileArgsDict(TypedDict):
    vhd_name: NotRequired[pulumi.Input[_builtins.str]]
    vhd_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VhdImageArtifactProfileArgs:
    def __init__(
        __self__,
        *,
        vhd_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vhd_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vhdName")
    def vhd_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vhd_name.setter
    def vhd_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vhdVersion")
    def vhd_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vhd_version.setter
    def vhd_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VhdImageMappingRuleProfileArgsDict(TypedDict):
    user_configuration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VhdImageMappingRuleProfileArgs:
    def __init__(
        __self__, *, user_configuration: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userConfiguration")
    def user_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_configuration.setter
    def user_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualHardDiskArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualHardDiskArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkFunctionNetworkFunctionDefinitionVersionArgsDict(TypedDict):
    network_function_type: pulumi.Input[_builtins.str]
    deploy_parameters: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    network_function_template: NotRequired[
        pulumi.Input[
            Union[
                AzureCoreNetworkFunctionTemplateArgsDict,
                AzureOperatorNexusNetworkFunctionTemplateArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class VirtualNetworkFunctionNetworkFunctionDefinitionVersionArgs:
    def __init__(
        __self__,
        *,
        network_function_type: pulumi.Input[_builtins.str],
        deploy_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        network_function_template: Optional[
            pulumi.Input[
                Union[
                    AzureCoreNetworkFunctionTemplateArgs,
                    AzureOperatorNexusNetworkFunctionTemplateArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> pulumi.Input[_builtins.str]: ...
    @network_function_type.setter
    def network_function_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deploy_parameters.setter
    def deploy_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionTemplate")
    def network_function_template(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureCoreNetworkFunctionTemplateArgs,
                AzureOperatorNexusNetworkFunctionTemplateArgs,
            ]
        ]
    ]: ...
    @network_function_template.setter
    def network_function_template(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureCoreNetworkFunctionTemplateArgs,
                    AzureOperatorNexusNetworkFunctionTemplateArgs,
                ]
            ]
        ],
    ): ...
