

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainArgs', 'Domain']
@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *, domain_execution_role: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., domain_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., single_sign_on: Optional[pulumi.Input[DomainSingleSignOnArgs]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[DomainTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainExecutionRole")
    def domain_execution_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_execution_role.setter
    def domain_execution_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainVersion")
    def domain_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_version.setter
    def domain_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleSignOn")
    def single_sign_on(self) -> Optional[pulumi.Input[DomainSingleSignOnArgs]]:
        
        ...
    
    @single_sign_on.setter
    def single_sign_on(self, value: Optional[pulumi.Input[DomainSingleSignOnArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDeletionCheck")
    def skip_deletion_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_deletion_check.setter
    def skip_deletion_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DomainTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DomainTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., domain_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., portal_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_domain_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., single_sign_on: Optional[pulumi.Input[DomainSingleSignOnArgs]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[DomainTimeoutsArgs]] = ...) -> None:
        
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainExecutionRole")
    def domain_execution_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_execution_role.setter
    def domain_execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainVersion")
    def domain_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_version.setter
    def domain_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_url.setter
    def portal_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDomainUnitId")
    def root_domain_unit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_domain_unit_id.setter
    def root_domain_unit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleSignOn")
    def single_sign_on(self) -> Optional[pulumi.Input[DomainSingleSignOnArgs]]:
        
        ...
    
    @single_sign_on.setter
    def single_sign_on(self, value: Optional[pulumi.Input[DomainSingleSignOnArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDeletionCheck")
    def skip_deletion_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_deletion_check.setter
    def skip_deletion_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DomainTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DomainTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:datazone/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., domain_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., single_sign_on: Optional[pulumi.Input[Union[DomainSingleSignOnArgs, DomainSingleSignOnArgsDict]]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[DomainTimeoutsArgs, DomainTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., domain_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., portal_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_domain_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., single_sign_on: Optional[pulumi.Input[Union[DomainSingleSignOnArgs, DomainSingleSignOnArgsDict]]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[DomainTimeoutsArgs, DomainTimeoutsArgsDict]]] = ...) -> Domain:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainExecutionRole")
    def domain_execution_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainVersion")
    def domain_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDomainUnitId")
    def root_domain_unit_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleSignOn")
    def single_sign_on(self) -> pulumi.Output[Optional[outputs.DomainSingleSignOn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDeletionCheck")
    def skip_deletion_check(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.DomainTimeouts]]:
        ...
    


