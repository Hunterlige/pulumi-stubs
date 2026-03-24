

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketArgs', 'Bucket']
@pulumi.input_type
class BucketArgs:
    def __init__(__self__, *, acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]] = ..., logging: Optional[pulumi.Input[BucketLoggingArgs]] = ..., object_lock_configuration: Optional[pulumi.Input[BucketObjectLockConfigurationArgs]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configuration: Optional[pulumi.Input[BucketReplicationConfigurationArgs]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versioning: Optional[pulumi.Input[BucketVersioningArgs]] = ..., website: Optional[pulumi.Input[BucketWebsiteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accelerationStatus")
    @_utilities.deprecated(...)
    def acceleration_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acceleration_status.setter
    def acceleration_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def acl(self) -> Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    @_utilities.deprecated(...)
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    @_utilities.deprecated(...)
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def logging(self) -> Optional[pulumi.Input[BucketLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[BucketLoggingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> Optional[pulumi.Input[BucketObjectLockConfigurationArgs]]:
        
        ...
    
    @object_lock_configuration.setter
    def object_lock_configuration(self, value: Optional[pulumi.Input[BucketObjectLockConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    @_utilities.deprecated(...)
    def replication_configuration(self) -> Optional[pulumi.Input[BucketReplicationConfigurationArgs]]:
        
        ...
    
    @replication_configuration.setter
    def replication_configuration(self, value: Optional[pulumi.Input[BucketReplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    @_utilities.deprecated(...)
    def request_payer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_payer.setter
    def request_payer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    @_utilities.deprecated(...)
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def versioning(self) -> Optional[pulumi.Input[BucketVersioningArgs]]:
        
        ...
    
    @versioning.setter
    def versioning(self, value: Optional[pulumi.Input[BucketVersioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def website(self) -> Optional[pulumi.Input[BucketWebsiteArgs]]:
        
        ...
    
    @website.setter
    def website(self, value: Optional[pulumi.Input[BucketWebsiteArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketState:
    def __init__(__self__, *, acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., bucket_region: Optional[pulumi.Input[_builtins.str]] = ..., bucket_regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]] = ..., logging: Optional[pulumi.Input[BucketLoggingArgs]] = ..., object_lock_configuration: Optional[pulumi.Input[BucketObjectLockConfigurationArgs]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configuration: Optional[pulumi.Input[BucketReplicationConfigurationArgs]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versioning: Optional[pulumi.Input[BucketVersioningArgs]] = ..., website: Optional[pulumi.Input[BucketWebsiteArgs]] = ..., website_domain: Optional[pulumi.Input[_builtins.str]] = ..., website_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accelerationStatus")
    @_utilities.deprecated(...)
    def acceleration_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acceleration_status.setter
    def acceleration_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def acl(self) -> Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketDomainName")
    def bucket_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_domain_name.setter
    def bucket_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegionalDomainName")
    def bucket_regional_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_regional_domain_name.setter
    def bucket_regional_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    @_utilities.deprecated(...)
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorsRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketGrantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    @_utilities.deprecated(...)
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def logging(self) -> Optional[pulumi.Input[BucketLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[BucketLoggingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> Optional[pulumi.Input[BucketObjectLockConfigurationArgs]]:
        
        ...
    
    @object_lock_configuration.setter
    def object_lock_configuration(self, value: Optional[pulumi.Input[BucketObjectLockConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    @_utilities.deprecated(...)
    def replication_configuration(self) -> Optional[pulumi.Input[BucketReplicationConfigurationArgs]]:
        
        ...
    
    @replication_configuration.setter
    def replication_configuration(self, value: Optional[pulumi.Input[BucketReplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    @_utilities.deprecated(...)
    def request_payer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_payer.setter
    def request_payer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    @_utilities.deprecated(...)
    def server_side_encryption_configuration(self) -> Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]]:
        
        ...
    
    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(self, value: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationArgs]]): # -> None:
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
    @pulumi.getter
    @_utilities.deprecated(...)
    def versioning(self) -> Optional[pulumi.Input[BucketVersioningArgs]]:
        
        ...
    
    @versioning.setter
    def versioning(self, value: Optional[pulumi.Input[BucketVersioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def website(self) -> Optional[pulumi.Input[BucketWebsiteArgs]]:
        
        ...
    
    @website.setter
    def website(self, value: Optional[pulumi.Input[BucketWebsiteArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteDomain")
    @_utilities.deprecated(...)
    def website_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_domain.setter
    def website_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    @_utilities.deprecated(...)
    def website_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_endpoint.setter
    def website_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucket:Bucket")
class Bucket(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorsRuleArgs, BucketCorsRuleArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketGrantArgs, BucketGrantArgsDict]]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleRuleArgs, BucketLifecycleRuleArgsDict]]]]] = ..., logging: Optional[pulumi.Input[Union[BucketLoggingArgs, BucketLoggingArgsDict]]] = ..., object_lock_configuration: Optional[pulumi.Input[Union[BucketObjectLockConfigurationArgs, BucketObjectLockConfigurationArgsDict]]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configuration: Optional[pulumi.Input[Union[BucketReplicationConfigurationArgs, BucketReplicationConfigurationArgsDict]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[BucketServerSideEncryptionConfigurationArgs, BucketServerSideEncryptionConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versioning: Optional[pulumi.Input[Union[BucketVersioningArgs, BucketVersioningArgsDict]]] = ..., website: Optional[pulumi.Input[Union[BucketWebsiteArgs, BucketWebsiteArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[BucketArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[Union[_builtins.str, CannedAcl]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., bucket_region: Optional[pulumi.Input[_builtins.str]] = ..., bucket_regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorsRuleArgs, BucketCorsRuleArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketGrantArgs, BucketGrantArgsDict]]]]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleRuleArgs, BucketLifecycleRuleArgsDict]]]]] = ..., logging: Optional[pulumi.Input[Union[BucketLoggingArgs, BucketLoggingArgsDict]]] = ..., object_lock_configuration: Optional[pulumi.Input[Union[BucketObjectLockConfigurationArgs, BucketObjectLockConfigurationArgsDict]]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configuration: Optional[pulumi.Input[Union[BucketReplicationConfigurationArgs, BucketReplicationConfigurationArgsDict]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configuration: Optional[pulumi.Input[Union[BucketServerSideEncryptionConfigurationArgs, BucketServerSideEncryptionConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versioning: Optional[pulumi.Input[Union[BucketVersioningArgs, BucketVersioningArgsDict]]] = ..., website: Optional[pulumi.Input[Union[BucketWebsiteArgs, BucketWebsiteArgsDict]]] = ..., website_domain: Optional[pulumi.Input[_builtins.str]] = ..., website_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> Bucket:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accelerationStatus")
    @_utilities.deprecated(...)
    def acceleration_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def acl(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketDomainName")
    def bucket_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketRegionalDomainName")
    def bucket_regional_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    @_utilities.deprecated(...)
    def cors_rules(self) -> pulumi.Output[Sequence[outputs.BucketCorsRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def grants(self) -> pulumi.Output[Sequence[outputs.BucketGrant]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    @_utilities.deprecated(...)
    def lifecycle_rules(self) -> pulumi.Output[Sequence[outputs.BucketLifecycleRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def logging(self) -> pulumi.Output[outputs.BucketLogging]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> pulumi.Output[outputs.BucketObjectLockConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    @_utilities.deprecated(...)
    def replication_configuration(self) -> pulumi.Output[outputs.BucketReplicationConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    @_utilities.deprecated(...)
    def request_payer(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfiguration")
    @_utilities.deprecated(...)
    def server_side_encryption_configuration(self) -> pulumi.Output[outputs.BucketServerSideEncryptionConfiguration]:
        
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
    @pulumi.getter
    @_utilities.deprecated(...)
    def versioning(self) -> pulumi.Output[outputs.BucketVersioning]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def website(self) -> pulumi.Output[outputs.BucketWebsite]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteDomain")
    @_utilities.deprecated(...)
    def website_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteEndpoint")
    @_utilities.deprecated(...)
    def website_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


