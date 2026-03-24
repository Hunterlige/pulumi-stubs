

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketV2Args', 'BucketV2']
@pulumi.input_type
class BucketV2Args:
    def __init__(__self__, *, acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]] = ..., loggings: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]] = ..., object_lock_configuration: Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versionings: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]] = ..., websites: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]] = ...) -> None:
        
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
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]]): # -> None:
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
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    @_utilities.deprecated(...)
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def loggings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]]:
        
        ...
    
    @loggings.setter
    def loggings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]]:
        
        ...
    
    @object_lock_configuration.setter
    def object_lock_configuration(self, value: Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]]): # -> None:
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
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfigurations")
    @_utilities.deprecated(...)
    def replication_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]]:
        
        ...
    
    @replication_configurations.setter
    def replication_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]]): # -> None:
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
    @pulumi.getter(name="serverSideEncryptionConfigurations")
    @_utilities.deprecated(...)
    def server_side_encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]]:
        
        ...
    
    @server_side_encryption_configurations.setter
    def server_side_encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]]): # -> None:
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
    def versionings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]]:
        
        ...
    
    @versionings.setter
    def versionings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def websites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]]:
        
        ...
    
    @websites.setter
    def websites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketV2State:
    def __init__(__self__, *, acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., bucket_region: Optional[pulumi.Input[_builtins.str]] = ..., bucket_regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]] = ..., loggings: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]] = ..., object_lock_configuration: Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versionings: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]] = ..., website_domain: Optional[pulumi.Input[_builtins.str]] = ..., website_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., websites: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]] = ...) -> None:
        
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
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]]:
        
        ...
    
    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2CorsRuleArgs]]]]): # -> None:
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
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2GrantArgs]]]]): # -> None:
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
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def loggings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]]:
        
        ...
    
    @loggings.setter
    def loggings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LoggingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]]:
        
        ...
    
    @object_lock_configuration.setter
    def object_lock_configuration(self, value: Optional[pulumi.Input[BucketV2ObjectLockConfigurationArgs]]): # -> None:
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
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfigurations")
    @_utilities.deprecated(...)
    def replication_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]]:
        
        ...
    
    @replication_configurations.setter
    def replication_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationArgs]]]]): # -> None:
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
    @pulumi.getter(name="serverSideEncryptionConfigurations")
    @_utilities.deprecated(...)
    def server_side_encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]]:
        
        ...
    
    @server_side_encryption_configurations.setter
    def server_side_encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationArgs]]]]): # -> None:
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
    def versionings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]]:
        
        ...
    
    @versionings.setter
    def versionings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2VersioningArgs]]]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def websites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]]:
        
        ...
    
    @websites.setter
    def websites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2WebsiteArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucketV2:BucketV2")
class BucketV2(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2CorsRuleArgs, BucketV2CorsRuleArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2GrantArgs, BucketV2GrantArgsDict]]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2LifecycleRuleArgs, BucketV2LifecycleRuleArgsDict]]]]] = ..., loggings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2LoggingArgs, BucketV2LoggingArgsDict]]]]] = ..., object_lock_configuration: Optional[pulumi.Input[Union[BucketV2ObjectLockConfigurationArgs, BucketV2ObjectLockConfigurationArgsDict]]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2ReplicationConfigurationArgs, BucketV2ReplicationConfigurationArgsDict]]]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2ServerSideEncryptionConfigurationArgs, BucketV2ServerSideEncryptionConfigurationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versionings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2VersioningArgs, BucketV2VersioningArgsDict]]]]] = ..., websites: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2WebsiteArgs, BucketV2WebsiteArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[BucketV2Args] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acceleration_status: Optional[pulumi.Input[_builtins.str]] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., bucket_region: Optional[pulumi.Input[_builtins.str]] = ..., bucket_regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2CorsRuleArgs, BucketV2CorsRuleArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., grants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2GrantArgs, BucketV2GrantArgsDict]]]]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2LifecycleRuleArgs, BucketV2LifecycleRuleArgsDict]]]]] = ..., loggings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2LoggingArgs, BucketV2LoggingArgsDict]]]]] = ..., object_lock_configuration: Optional[pulumi.Input[Union[BucketV2ObjectLockConfigurationArgs, BucketV2ObjectLockConfigurationArgsDict]]] = ..., object_lock_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2ReplicationConfigurationArgs, BucketV2ReplicationConfigurationArgsDict]]]]] = ..., request_payer: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2ServerSideEncryptionConfigurationArgs, BucketV2ServerSideEncryptionConfigurationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., versionings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2VersioningArgs, BucketV2VersioningArgsDict]]]]] = ..., website_domain: Optional[pulumi.Input[_builtins.str]] = ..., website_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., websites: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketV2WebsiteArgs, BucketV2WebsiteArgsDict]]]]] = ...) -> BucketV2:
        
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
    def cors_rules(self) -> pulumi.Output[Sequence[outputs.BucketV2CorsRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def grants(self) -> pulumi.Output[Sequence[outputs.BucketV2Grant]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    @_utilities.deprecated(...)
    def lifecycle_rules(self) -> pulumi.Output[Sequence[outputs.BucketV2LifecycleRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def loggings(self) -> pulumi.Output[Sequence[outputs.BucketV2Logging]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockConfiguration")
    @_utilities.deprecated(...)
    def object_lock_configuration(self) -> pulumi.Output[outputs.BucketV2ObjectLockConfiguration]:
        
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
    @pulumi.getter(name="replicationConfigurations")
    @_utilities.deprecated(...)
    def replication_configurations(self) -> pulumi.Output[Sequence[outputs.BucketV2ReplicationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    @_utilities.deprecated(...)
    def request_payer(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfigurations")
    @_utilities.deprecated(...)
    def server_side_encryption_configurations(self) -> pulumi.Output[Sequence[outputs.BucketV2ServerSideEncryptionConfiguration]]:
        
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
    def versionings(self) -> pulumi.Output[Sequence[outputs.BucketV2Versioning]]:
        
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
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def websites(self) -> pulumi.Output[Sequence[outputs.BucketV2Website]]:
        
        ...
    


