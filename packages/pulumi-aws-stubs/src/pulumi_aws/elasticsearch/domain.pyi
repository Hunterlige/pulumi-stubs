

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainArgs', 'Domain']
@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *, access_policies: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., advanced_security_options: Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]] = ..., auto_tune_options: Optional[pulumi.Input[DomainAutoTuneOptionsArgs]] = ..., cluster_config: Optional[pulumi.Input[DomainClusterConfigArgs]] = ..., cognito_options: Optional[pulumi.Input[DomainCognitoOptionsArgs]] = ..., domain_endpoint_options: Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ebs_options: Optional[pulumi.Input[DomainEbsOptionsArgs]] = ..., elasticsearch_version: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_at_rest: Optional[pulumi.Input[DomainEncryptAtRestArgs]] = ..., log_publishing_options: Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]] = ..., node_to_node_encryption: Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_options: Optional[pulumi.Input[DomainSnapshotOptionsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_options: Optional[pulumi.Input[DomainVpcOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @advanced_options.setter
    def advanced_options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]]:
        
        ...
    
    @advanced_security_options.setter
    def advanced_security_options(self, value: Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoTuneOptions")
    def auto_tune_options(self) -> Optional[pulumi.Input[DomainAutoTuneOptionsArgs]]:
        
        ...
    
    @auto_tune_options.setter
    def auto_tune_options(self, value: Optional[pulumi.Input[DomainAutoTuneOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> Optional[pulumi.Input[DomainClusterConfigArgs]]:
        
        ...
    
    @cluster_config.setter
    def cluster_config(self, value: Optional[pulumi.Input[DomainClusterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional[pulumi.Input[DomainCognitoOptionsArgs]]:
        
        ...
    
    @cognito_options.setter
    def cognito_options(self, value: Optional[pulumi.Input[DomainCognitoOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]]:
        
        ...
    
    @domain_endpoint_options.setter
    def domain_endpoint_options(self, value: Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Optional[pulumi.Input[DomainEbsOptionsArgs]]:
        
        ...
    
    @ebs_options.setter
    def ebs_options(self, value: Optional[pulumi.Input[DomainEbsOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elasticsearch_version.setter
    def elasticsearch_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptAtRest")
    def encrypt_at_rest(self) -> Optional[pulumi.Input[DomainEncryptAtRestArgs]]:
        
        ...
    
    @encrypt_at_rest.setter
    def encrypt_at_rest(self, value: Optional[pulumi.Input[DomainEncryptAtRestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]]:
        
        ...
    
    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeToNodeEncryption")
    def node_to_node_encryption(self) -> Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]]:
        
        ...
    
    @node_to_node_encryption.setter
    def node_to_node_encryption(self, value: Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional[pulumi.Input[DomainSnapshotOptionsArgs]]:
        
        ...
    
    @snapshot_options.setter
    def snapshot_options(self, value: Optional[pulumi.Input[DomainSnapshotOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input[DomainVpcOptionsArgs]]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input[DomainVpcOptionsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *, access_policies: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., advanced_security_options: Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_tune_options: Optional[pulumi.Input[DomainAutoTuneOptionsArgs]] = ..., cluster_config: Optional[pulumi.Input[DomainClusterConfigArgs]] = ..., cognito_options: Optional[pulumi.Input[DomainCognitoOptionsArgs]] = ..., domain_endpoint_options: Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ebs_options: Optional[pulumi.Input[DomainEbsOptionsArgs]] = ..., elasticsearch_version: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_at_rest: Optional[pulumi.Input[DomainEncryptAtRestArgs]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., kibana_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., log_publishing_options: Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]] = ..., node_to_node_encryption: Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_options: Optional[pulumi.Input[DomainSnapshotOptionsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_options: Optional[pulumi.Input[DomainVpcOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @advanced_options.setter
    def advanced_options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]]:
        
        ...
    
    @advanced_security_options.setter
    def advanced_security_options(self, value: Optional[pulumi.Input[DomainAdvancedSecurityOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoTuneOptions")
    def auto_tune_options(self) -> Optional[pulumi.Input[DomainAutoTuneOptionsArgs]]:
        
        ...
    
    @auto_tune_options.setter
    def auto_tune_options(self, value: Optional[pulumi.Input[DomainAutoTuneOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> Optional[pulumi.Input[DomainClusterConfigArgs]]:
        
        ...
    
    @cluster_config.setter
    def cluster_config(self, value: Optional[pulumi.Input[DomainClusterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional[pulumi.Input[DomainCognitoOptionsArgs]]:
        
        ...
    
    @cognito_options.setter
    def cognito_options(self, value: Optional[pulumi.Input[DomainCognitoOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]]:
        
        ...
    
    @domain_endpoint_options.setter
    def domain_endpoint_options(self, value: Optional[pulumi.Input[DomainDomainEndpointOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Optional[pulumi.Input[DomainEbsOptionsArgs]]:
        
        ...
    
    @ebs_options.setter
    def ebs_options(self, value: Optional[pulumi.Input[DomainEbsOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elasticsearch_version.setter
    def elasticsearch_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptAtRest")
    def encrypt_at_rest(self) -> Optional[pulumi.Input[DomainEncryptAtRestArgs]]:
        
        ...
    
    @encrypt_at_rest.setter
    def encrypt_at_rest(self, value: Optional[pulumi.Input[DomainEncryptAtRestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kibanaEndpoint")
    def kibana_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kibana_endpoint.setter
    def kibana_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]]:
        
        ...
    
    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainLogPublishingOptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeToNodeEncryption")
    def node_to_node_encryption(self) -> Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]]:
        
        ...
    
    @node_to_node_encryption.setter
    def node_to_node_encryption(self, value: Optional[pulumi.Input[DomainNodeToNodeEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional[pulumi.Input[DomainSnapshotOptionsArgs]]:
        
        ...
    
    @snapshot_options.setter
    def snapshot_options(self, value: Optional[pulumi.Input[DomainSnapshotOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input[DomainVpcOptionsArgs]]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input[DomainVpcOptionsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:elasticsearch/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_policies: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., advanced_security_options: Optional[pulumi.Input[Union[DomainAdvancedSecurityOptionsArgs, DomainAdvancedSecurityOptionsArgsDict]]] = ..., auto_tune_options: Optional[pulumi.Input[Union[DomainAutoTuneOptionsArgs, DomainAutoTuneOptionsArgsDict]]] = ..., cluster_config: Optional[pulumi.Input[Union[DomainClusterConfigArgs, DomainClusterConfigArgsDict]]] = ..., cognito_options: Optional[pulumi.Input[Union[DomainCognitoOptionsArgs, DomainCognitoOptionsArgsDict]]] = ..., domain_endpoint_options: Optional[pulumi.Input[Union[DomainDomainEndpointOptionsArgs, DomainDomainEndpointOptionsArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ebs_options: Optional[pulumi.Input[Union[DomainEbsOptionsArgs, DomainEbsOptionsArgsDict]]] = ..., elasticsearch_version: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_at_rest: Optional[pulumi.Input[Union[DomainEncryptAtRestArgs, DomainEncryptAtRestArgsDict]]] = ..., log_publishing_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainLogPublishingOptionArgs, DomainLogPublishingOptionArgsDict]]]]] = ..., node_to_node_encryption: Optional[pulumi.Input[Union[DomainNodeToNodeEncryptionArgs, DomainNodeToNodeEncryptionArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_options: Optional[pulumi.Input[Union[DomainSnapshotOptionsArgs, DomainSnapshotOptionsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_options: Optional[pulumi.Input[Union[DomainVpcOptionsArgs, DomainVpcOptionsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DomainArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_policies: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., advanced_security_options: Optional[pulumi.Input[Union[DomainAdvancedSecurityOptionsArgs, DomainAdvancedSecurityOptionsArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_tune_options: Optional[pulumi.Input[Union[DomainAutoTuneOptionsArgs, DomainAutoTuneOptionsArgsDict]]] = ..., cluster_config: Optional[pulumi.Input[Union[DomainClusterConfigArgs, DomainClusterConfigArgsDict]]] = ..., cognito_options: Optional[pulumi.Input[Union[DomainCognitoOptionsArgs, DomainCognitoOptionsArgsDict]]] = ..., domain_endpoint_options: Optional[pulumi.Input[Union[DomainDomainEndpointOptionsArgs, DomainDomainEndpointOptionsArgsDict]]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ebs_options: Optional[pulumi.Input[Union[DomainEbsOptionsArgs, DomainEbsOptionsArgsDict]]] = ..., elasticsearch_version: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_at_rest: Optional[pulumi.Input[Union[DomainEncryptAtRestArgs, DomainEncryptAtRestArgsDict]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., kibana_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., log_publishing_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainLogPublishingOptionArgs, DomainLogPublishingOptionArgsDict]]]]] = ..., node_to_node_encryption: Optional[pulumi.Input[Union[DomainNodeToNodeEncryptionArgs, DomainNodeToNodeEncryptionArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_options: Optional[pulumi.Input[Union[DomainSnapshotOptionsArgs, DomainSnapshotOptionsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_options: Optional[pulumi.Input[Union[DomainVpcOptionsArgs, DomainVpcOptionsArgsDict]]] = ...) -> Domain:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> pulumi.Output[outputs.DomainAdvancedSecurityOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoTuneOptions")
    def auto_tune_options(self) -> pulumi.Output[outputs.DomainAutoTuneOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> pulumi.Output[outputs.DomainClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> pulumi.Output[Optional[outputs.DomainCognitoOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> pulumi.Output[outputs.DomainDomainEndpointOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> pulumi.Output[outputs.DomainEbsOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptAtRest")
    def encrypt_at_rest(self) -> pulumi.Output[outputs.DomainEncryptAtRest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kibanaEndpoint")
    def kibana_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> pulumi.Output[Optional[Sequence[outputs.DomainLogPublishingOption]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeToNodeEncryption")
    def node_to_node_encryption(self) -> pulumi.Output[outputs.DomainNodeToNodeEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> pulumi.Output[Optional[outputs.DomainSnapshotOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output[Optional[outputs.DomainVpcOptions]]:
        
        ...
    


