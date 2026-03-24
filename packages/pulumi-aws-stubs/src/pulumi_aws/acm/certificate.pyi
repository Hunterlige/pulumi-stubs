

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
__all__ = ['CertificateArgs', 'Certificate']
@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *, certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_body: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., early_renewal_duration: Optional[pulumi.Input[_builtins.str]] = ..., key_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[CertificateOptionsArgs]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., validation_method: Optional[pulumi.Input[_builtins.str]] = ..., validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_body.setter
    def certificate_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyRenewalDuration")
    def early_renewal_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @early_renewal_duration.setter
    def early_renewal_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[CertificateOptionsArgs]]:
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[CertificateOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationMethod")
    def validation_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @validation_method.setter
    def validation_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]]:
        ...
    
    @validation_options.setter
    def validation_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CertificateState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_body: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateDomainValidationOptionArgs]]]] = ..., early_renewal_duration: Optional[pulumi.Input[_builtins.str]] = ..., key_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., not_after: Optional[pulumi.Input[_builtins.str]] = ..., not_before: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[CertificateOptionsArgs]] = ..., pending_renewal: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., renewal_eligibility: Optional[pulumi.Input[_builtins.str]] = ..., renewal_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateRenewalSummaryArgs]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validation_emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., validation_method: Optional[pulumi.Input[_builtins.str]] = ..., validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_body.setter
    def certificate_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainValidationOptions")
    def domain_validation_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateDomainValidationOptionArgs]]]]:
        
        ...
    
    @domain_validation_options.setter
    def domain_validation_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateDomainValidationOptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyRenewalDuration")
    def early_renewal_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @early_renewal_duration.setter
    def early_renewal_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_after.setter
    def not_after(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[CertificateOptionsArgs]]:
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[CertificateOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingRenewal")
    def pending_renewal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @pending_renewal.setter
    def pending_renewal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalEligibility")
    def renewal_eligibility(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renewal_eligibility.setter
    def renewal_eligibility(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalSummaries")
    def renewal_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateRenewalSummaryArgs]]]]:
        
        ...
    
    @renewal_summaries.setter
    def renewal_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateRenewalSummaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationEmails")
    def validation_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @validation_emails.setter
    def validation_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationMethod")
    def validation_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @validation_method.setter
    def validation_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]]:
        ...
    
    @validation_options.setter
    def validation_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateValidationOptionArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:acm/certificate:Certificate")
class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_body: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., early_renewal_duration: Optional[pulumi.Input[_builtins.str]] = ..., key_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Union[CertificateOptionsArgs, CertificateOptionsArgsDict]]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., validation_method: Optional[pulumi.Input[_builtins.str]] = ..., validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CertificateValidationOptionArgs, CertificateValidationOptionArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[CertificateArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_body: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CertificateDomainValidationOptionArgs, CertificateDomainValidationOptionArgsDict]]]]] = ..., early_renewal_duration: Optional[pulumi.Input[_builtins.str]] = ..., key_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., not_after: Optional[pulumi.Input[_builtins.str]] = ..., not_before: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Union[CertificateOptionsArgs, CertificateOptionsArgsDict]]] = ..., pending_renewal: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., renewal_eligibility: Optional[pulumi.Input[_builtins.str]] = ..., renewal_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CertificateRenewalSummaryArgs, CertificateRenewalSummaryArgsDict]]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validation_emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., validation_method: Optional[pulumi.Input[_builtins.str]] = ..., validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CertificateValidationOptionArgs, CertificateValidationOptionArgsDict]]]]] = ...) -> Certificate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainValidationOptions")
    def domain_validation_options(self) -> pulumi.Output[Sequence[outputs.CertificateDomainValidationOption]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyRenewalDuration")
    def early_renewal_duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Output[outputs.CertificateOptions]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingRenewal")
    def pending_renewal(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalEligibility")
    def renewal_eligibility(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalSummaries")
    def renewal_summaries(self) -> pulumi.Output[Sequence[outputs.CertificateRenewalSummary]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
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
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationEmails")
    def validation_emails(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationMethod")
    def validation_method(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> pulumi.Output[Optional[Sequence[outputs.CertificateValidationOption]]]:
        ...
    


