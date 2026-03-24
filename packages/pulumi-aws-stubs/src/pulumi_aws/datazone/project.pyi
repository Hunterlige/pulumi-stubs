

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProjectArgs', 'Project']
@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *, domain_identifier: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[ProjectTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @glossary_terms.setter
    def glossary_terms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="skipDeletionCheck")
    def skip_deletion_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_deletion_check.setter
    def skip_deletion_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ProjectTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ProjectTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., failure_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectFailureReasonArgs]]]] = ..., glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., last_updated_at: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[ProjectTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectFailureReasonArgs]]]]:
        
        ...
    
    @failure_reasons.setter
    def failure_reasons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectFailureReasonArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @glossary_terms.setter
    def glossary_terms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_at.setter
    def last_updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_status.setter
    def project_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[ProjectTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ProjectTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:datazone/project:Project")
class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[ProjectTimeoutsArgs, ProjectTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProjectArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., failure_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ProjectFailureReasonArgs, ProjectFailureReasonArgsDict]]]]] = ..., glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., last_updated_at: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_deletion_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[ProjectTimeoutsArgs, ProjectTimeoutsArgsDict]]] = ...) -> Project:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(self) -> pulumi.Output[Sequence[outputs.ProjectFailureReason]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDeletionCheck")
    def skip_deletion_check(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ProjectTimeouts]]:
        ...
    


