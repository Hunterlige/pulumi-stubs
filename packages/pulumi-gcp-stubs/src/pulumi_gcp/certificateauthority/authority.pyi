

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
__all__ = ['AuthorityArgs', 'Authority']
@pulumi.input_type
class AuthorityArgs:
    def __init__(__self__, *, certificate_authority_id: pulumi.Input[_builtins.str], config: pulumi.Input[AuthorityConfigArgs], key_spec: pulumi.Input[AuthorityKeySpecArgs], location: pulumi.Input[_builtins.str], pool: pulumi.Input[_builtins.str], deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_active_certificates_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifetime: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_grace_period: Optional[pulumi.Input[_builtins.bool]] = ..., subordinate_config: Optional[pulumi.Input[AuthoritySubordinateConfigArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_access_urls: Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityId")
    def certificate_authority_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_authority_id.setter
    def certificate_authority_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[AuthorityConfigArgs]:
        
        ...
    
    @config.setter
    def config(self, value: pulumi.Input[AuthorityConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> pulumi.Input[AuthorityKeySpecArgs]:
        
        ...
    
    @key_spec.setter
    def key_spec(self, value: pulumi.Input[AuthorityKeySpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pool.setter
    def pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_active_certificates_on_deletion.setter
    def ignore_active_certificates_on_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificate")
    def pem_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pem_ca_certificate.setter
    def pem_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipGracePeriod")
    def skip_grace_period(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_grace_period.setter
    def skip_grace_period(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subordinateConfig")
    def subordinate_config(self) -> Optional[pulumi.Input[AuthoritySubordinateConfigArgs]]:
        
        ...
    
    @subordinate_config.setter
    def subordinate_config(self, value: Optional[pulumi.Input[AuthoritySubordinateConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedAccessUrls")
    def user_defined_access_urls(self) -> Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]]:
        
        ...
    
    @user_defined_access_urls.setter
    def user_defined_access_urls(self, value: Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AuthorityState:
    def __init__(__self__, *, access_urls: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorityAccessUrlArgs]]]] = ..., certificate_authority_id: Optional[pulumi.Input[_builtins.str]] = ..., config: Optional[pulumi.Input[AuthorityConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_active_certificates_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., key_spec: Optional[pulumi.Input[AuthorityKeySpecArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifetime: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., pool: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., skip_grace_period: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subordinate_config: Optional[pulumi.Input[AuthoritySubordinateConfigArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_access_urls: Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrls")
    def access_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthorityAccessUrlArgs]]]]:
        
        ...
    
    @access_urls.setter
    def access_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorityAccessUrlArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityId")
    def certificate_authority_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_authority_id.setter
    def certificate_authority_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[AuthorityConfigArgs]]:
        
        ...
    
    @config.setter
    def config(self, value: Optional[pulumi.Input[AuthorityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_active_certificates_on_deletion.setter
    def ignore_active_certificates_on_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> Optional[pulumi.Input[AuthorityKeySpecArgs]]:
        
        ...
    
    @key_spec.setter
    def key_spec(self, value: Optional[pulumi.Input[AuthorityKeySpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificate")
    def pem_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pem_ca_certificate.setter
    def pem_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificates")
    def pem_ca_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pem_ca_certificates.setter
    def pem_ca_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pool.setter
    def pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipGracePeriod")
    def skip_grace_period(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_grace_period.setter
    def skip_grace_period(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subordinateConfig")
    def subordinate_config(self) -> Optional[pulumi.Input[AuthoritySubordinateConfigArgs]]:
        
        ...
    
    @subordinate_config.setter
    def subordinate_config(self, value: Optional[pulumi.Input[AuthoritySubordinateConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedAccessUrls")
    def user_defined_access_urls(self) -> Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]]:
        
        ...
    
    @user_defined_access_urls.setter
    def user_defined_access_urls(self, value: Optional[pulumi.Input[AuthorityUserDefinedAccessUrlsArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:certificateauthority/authority:Authority")
class Authority(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate_authority_id: Optional[pulumi.Input[_builtins.str]] = ..., config: Optional[pulumi.Input[Union[AuthorityConfigArgs, AuthorityConfigArgsDict]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_active_certificates_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., key_spec: Optional[pulumi.Input[Union[AuthorityKeySpecArgs, AuthorityKeySpecArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifetime: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., pool: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., skip_grace_period: Optional[pulumi.Input[_builtins.bool]] = ..., subordinate_config: Optional[pulumi.Input[Union[AuthoritySubordinateConfigArgs, AuthoritySubordinateConfigArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_access_urls: Optional[pulumi.Input[Union[AuthorityUserDefinedAccessUrlsArgs, AuthorityUserDefinedAccessUrlsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthorityArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_urls: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AuthorityAccessUrlArgs, AuthorityAccessUrlArgsDict]]]]] = ..., certificate_authority_id: Optional[pulumi.Input[_builtins.str]] = ..., config: Optional[pulumi.Input[Union[AuthorityConfigArgs, AuthorityConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., ignore_active_certificates_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., key_spec: Optional[pulumi.Input[Union[AuthorityKeySpecArgs, AuthorityKeySpecArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifetime: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., pem_ca_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., pool: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., skip_grace_period: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subordinate_config: Optional[pulumi.Input[Union[AuthoritySubordinateConfigArgs, AuthoritySubordinateConfigArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_access_urls: Optional[pulumi.Input[Union[AuthorityUserDefinedAccessUrlsArgs, AuthorityUserDefinedAccessUrlsArgsDict]]] = ...) -> Authority:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrls")
    def access_urls(self) -> pulumi.Output[Sequence[outputs.AuthorityAccessUrl]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityId")
    def certificate_authority_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[outputs.AuthorityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> pulumi.Output[outputs.AuthorityKeySpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificate")
    def pem_ca_certificate(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificates")
    def pem_ca_certificates(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipGracePeriod")
    def skip_grace_period(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subordinateConfig")
    def subordinate_config(self) -> pulumi.Output[Optional[outputs.AuthoritySubordinateConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedAccessUrls")
    def user_defined_access_urls(self) -> pulumi.Output[Optional[outputs.AuthorityUserDefinedAccessUrls]]:
        
        ...
    


