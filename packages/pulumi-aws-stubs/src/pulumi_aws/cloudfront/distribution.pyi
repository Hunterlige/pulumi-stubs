

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
__all__ = ['DistributionArgs', 'Distribution']
@pulumi.input_type
class DistributionArgs:
    def __init__(__self__, *, default_cache_behavior: pulumi.Input[DistributionDefaultCacheBehaviorArgs], enabled: pulumi.Input[_builtins.bool], origins: pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]], restrictions: pulumi.Input[DistributionRestrictionsArgs], viewer_certificate: pulumi.Input[DistributionViewerCertificateArgs], aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., anycast_ip_list_id: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_association: Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]] = ..., continuous_deployment_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]] = ..., default_root_object: Optional[pulumi.Input[_builtins.str]] = ..., http_version: Optional[pulumi.Input[_builtins.str]] = ..., is_ipv6_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., logging_config: Optional[pulumi.Input[DistributionLoggingConfigArgs]] = ..., ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]] = ..., origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]] = ..., price_class: Optional[pulumi.Input[_builtins.str]] = ..., retain_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., staging: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., viewer_mtls_config: Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]] = ..., wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> pulumi.Input[DistributionDefaultCacheBehaviorArgs]:
        
        ...
    
    @default_cache_behavior.setter
    def default_cache_behavior(self, value: pulumi.Input[DistributionDefaultCacheBehaviorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]]:
        
        ...
    
    @origins.setter
    def origins(self, value: pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def restrictions(self) -> pulumi.Input[DistributionRestrictionsArgs]:
        
        ...
    
    @restrictions.setter
    def restrictions(self, value: pulumi.Input[DistributionRestrictionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(self) -> pulumi.Input[DistributionViewerCertificateArgs]:
        
        ...
    
    @viewer_certificate.setter
    def viewer_certificate(self, value: pulumi.Input[DistributionViewerCertificateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anycastIpListId")
    def anycast_ip_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @anycast_ip_list_id.setter
    def anycast_ip_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionAssociation")
    def connection_function_association(self) -> Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]]:
        
        ...
    
    @connection_function_association.setter
    def connection_function_association(self, value: Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousDeploymentPolicyId")
    def continuous_deployment_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @continuous_deployment_policy_id.setter
    def continuous_deployment_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]]:
        
        ...
    
    @custom_error_responses.setter
    def custom_error_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_root_object.setter
    def default_root_object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_version.setter
    def http_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isIpv6Enabled")
    def is_ipv6_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_ipv6_enabled.setter
    def is_ipv6_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[DistributionLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[DistributionLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedCacheBehaviors")
    def ordered_cache_behaviors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]]:
        
        ...
    
    @ordered_cache_behaviors.setter
    def ordered_cache_behaviors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]]:
        
        ...
    
    @origin_groups.setter
    def origin_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceClass")
    def price_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @price_class.setter
    def price_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainOnDelete")
    def retain_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_on_delete.setter
    def retain_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def staging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @staging.setter
    def staging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerMtlsConfig")
    def viewer_mtls_config(self) -> Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]]:
        
        ...
    
    @viewer_mtls_config.setter
    def viewer_mtls_config(self, value: Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_deployment.setter
    def wait_for_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_acl_id.setter
    def web_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DistributionState:
    def __init__(__self__, *, aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., anycast_ip_list_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_association: Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]] = ..., continuous_deployment_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]] = ..., default_cache_behavior: Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]] = ..., default_root_object: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., http_version: Optional[pulumi.Input[_builtins.str]] = ..., in_progress_validation_batches: Optional[pulumi.Input[_builtins.int]] = ..., is_ipv6_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[DistributionLoggingConfigArgs]] = ..., logging_v1_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]] = ..., origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]] = ..., origins: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]]] = ..., price_class: Optional[pulumi.Input[_builtins.str]] = ..., restrictions: Optional[pulumi.Input[DistributionRestrictionsArgs]] = ..., retain_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., staging: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trusted_key_groups: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupArgs]]]] = ..., trusted_signers: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerArgs]]]] = ..., viewer_certificate: Optional[pulumi.Input[DistributionViewerCertificateArgs]] = ..., viewer_mtls_config: Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]] = ..., wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anycastIpListId")
    def anycast_ip_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @anycast_ip_list_id.setter
    def anycast_ip_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @caller_reference.setter
    def caller_reference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionAssociation")
    def connection_function_association(self) -> Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]]:
        
        ...
    
    @connection_function_association.setter
    def connection_function_association(self, value: Optional[pulumi.Input[DistributionConnectionFunctionAssociationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousDeploymentPolicyId")
    def continuous_deployment_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @continuous_deployment_policy_id.setter
    def continuous_deployment_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]]:
        
        ...
    
    @custom_error_responses.setter
    def custom_error_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCustomErrorResponseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]]:
        
        ...
    
    @default_cache_behavior.setter
    def default_cache_behavior(self, value: Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_root_object.setter
    def default_root_object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_version.setter
    def http_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inProgressValidationBatches")
    def in_progress_validation_batches(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @in_progress_validation_batches.setter
    def in_progress_validation_batches(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isIpv6Enabled")
    def is_ipv6_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_ipv6_enabled.setter
    def is_ipv6_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[DistributionLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[DistributionLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingV1Enabled")
    def logging_v1_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @logging_v1_enabled.setter
    def logging_v1_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedCacheBehaviors")
    def ordered_cache_behaviors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]]:
        
        ...
    
    @ordered_cache_behaviors.setter
    def ordered_cache_behaviors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]]:
        
        ...
    
    @origin_groups.setter
    def origin_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]]]:
        
        ...
    
    @origins.setter
    def origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceClass")
    def price_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @price_class.setter
    def price_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def restrictions(self) -> Optional[pulumi.Input[DistributionRestrictionsArgs]]:
        
        ...
    
    @restrictions.setter
    def restrictions(self, value: Optional[pulumi.Input[DistributionRestrictionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainOnDelete")
    def retain_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_on_delete.setter
    def retain_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def staging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @staging.setter
    def staging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupArgs]]]]:
        
        ...
    
    @trusted_key_groups.setter
    def trusted_key_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerArgs]]]]:
        
        ...
    
    @trusted_signers.setter
    def trusted_signers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(self) -> Optional[pulumi.Input[DistributionViewerCertificateArgs]]:
        
        ...
    
    @viewer_certificate.setter
    def viewer_certificate(self, value: Optional[pulumi.Input[DistributionViewerCertificateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerMtlsConfig")
    def viewer_mtls_config(self) -> Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]]:
        
        ...
    
    @viewer_mtls_config.setter
    def viewer_mtls_config(self, value: Optional[pulumi.Input[DistributionViewerMtlsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_deployment.setter
    def wait_for_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_acl_id.setter
    def web_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudfront/distribution:Distribution")
class Distribution(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., anycast_ip_list_id: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_association: Optional[pulumi.Input[Union[DistributionConnectionFunctionAssociationArgs, DistributionConnectionFunctionAssociationArgsDict]]] = ..., continuous_deployment_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionCustomErrorResponseArgs, DistributionCustomErrorResponseArgsDict]]]]] = ..., default_cache_behavior: Optional[pulumi.Input[Union[DistributionDefaultCacheBehaviorArgs, DistributionDefaultCacheBehaviorArgsDict]]] = ..., default_root_object: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., http_version: Optional[pulumi.Input[_builtins.str]] = ..., is_ipv6_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., logging_config: Optional[pulumi.Input[Union[DistributionLoggingConfigArgs, DistributionLoggingConfigArgsDict]]] = ..., ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOrderedCacheBehaviorArgs, DistributionOrderedCacheBehaviorArgsDict]]]]] = ..., origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOriginGroupArgs, DistributionOriginGroupArgsDict]]]]] = ..., origins: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOriginArgs, DistributionOriginArgsDict]]]]] = ..., price_class: Optional[pulumi.Input[_builtins.str]] = ..., restrictions: Optional[pulumi.Input[Union[DistributionRestrictionsArgs, DistributionRestrictionsArgsDict]]] = ..., retain_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., staging: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., viewer_certificate: Optional[pulumi.Input[Union[DistributionViewerCertificateArgs, DistributionViewerCertificateArgsDict]]] = ..., viewer_mtls_config: Optional[pulumi.Input[Union[DistributionViewerMtlsConfigArgs, DistributionViewerMtlsConfigArgsDict]]] = ..., wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., web_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DistributionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., anycast_ip_list_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., connection_function_association: Optional[pulumi.Input[Union[DistributionConnectionFunctionAssociationArgs, DistributionConnectionFunctionAssociationArgsDict]]] = ..., continuous_deployment_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionCustomErrorResponseArgs, DistributionCustomErrorResponseArgsDict]]]]] = ..., default_cache_behavior: Optional[pulumi.Input[Union[DistributionDefaultCacheBehaviorArgs, DistributionDefaultCacheBehaviorArgsDict]]] = ..., default_root_object: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., http_version: Optional[pulumi.Input[_builtins.str]] = ..., in_progress_validation_batches: Optional[pulumi.Input[_builtins.int]] = ..., is_ipv6_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[DistributionLoggingConfigArgs, DistributionLoggingConfigArgsDict]]] = ..., logging_v1_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOrderedCacheBehaviorArgs, DistributionOrderedCacheBehaviorArgsDict]]]]] = ..., origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOriginGroupArgs, DistributionOriginGroupArgsDict]]]]] = ..., origins: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionOriginArgs, DistributionOriginArgsDict]]]]] = ..., price_class: Optional[pulumi.Input[_builtins.str]] = ..., restrictions: Optional[pulumi.Input[Union[DistributionRestrictionsArgs, DistributionRestrictionsArgsDict]]] = ..., retain_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., staging: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trusted_key_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionTrustedKeyGroupArgs, DistributionTrustedKeyGroupArgsDict]]]]] = ..., trusted_signers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionTrustedSignerArgs, DistributionTrustedSignerArgsDict]]]]] = ..., viewer_certificate: Optional[pulumi.Input[Union[DistributionViewerCertificateArgs, DistributionViewerCertificateArgsDict]]] = ..., viewer_mtls_config: Optional[pulumi.Input[Union[DistributionViewerMtlsConfigArgs, DistributionViewerMtlsConfigArgsDict]]] = ..., wait_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., web_acl_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Distribution:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anycastIpListId")
    def anycast_ip_list_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionFunctionAssociation")
    def connection_function_association(self) -> pulumi.Output[Optional[outputs.DistributionConnectionFunctionAssociation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousDeploymentPolicyId")
    def continuous_deployment_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(self) -> pulumi.Output[Optional[Sequence[outputs.DistributionCustomErrorResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> pulumi.Output[outputs.DistributionDefaultCacheBehavior]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inProgressValidationBatches")
    def in_progress_validation_batches(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isIpv6Enabled")
    def is_ipv6_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional[outputs.DistributionLoggingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingV1Enabled")
    def logging_v1_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedCacheBehaviors")
    def ordered_cache_behaviors(self) -> pulumi.Output[Optional[Sequence[outputs.DistributionOrderedCacheBehavior]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> pulumi.Output[Optional[Sequence[outputs.DistributionOriginGroup]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> pulumi.Output[Sequence[outputs.DistributionOrigin]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceClass")
    def price_class(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def restrictions(self) -> pulumi.Output[outputs.DistributionRestrictions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainOnDelete")
    def retain_on_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def staging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> pulumi.Output[Sequence[outputs.DistributionTrustedKeyGroup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> pulumi.Output[Sequence[outputs.DistributionTrustedSigner]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(self) -> pulumi.Output[outputs.DistributionViewerCertificate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerMtlsConfig")
    def viewer_mtls_config(self) -> pulumi.Output[Optional[outputs.DistributionViewerMtlsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


