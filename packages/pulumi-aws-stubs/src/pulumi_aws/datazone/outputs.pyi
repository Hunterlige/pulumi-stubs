

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssetTypeFormsInput', 'AssetTypeTimeouts', 'DomainSingleSignOn', 'DomainTimeouts', 'EnvironmentLastDeployment', 'EnvironmentLastDeploymentFailureReason', 'EnvironmentProfileUserParameter', 'EnvironmentProvisionedResource', 'EnvironmentTimeouts', 'EnvironmentUserParameter', 'FormTypeImport', 'FormTypeModel', 'FormTypeTimeouts', 'GlossaryTermTermRelations', 'GlossaryTermTimeouts', 'ProjectFailureReason', 'ProjectTimeouts', 'UserProfileDetail', 'UserProfileDetailIam', 'UserProfileDetailSso', 'UserProfileTimeouts']
@pulumi.output_type
class AssetTypeFormsInput(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, type_identifier: _builtins.str, type_revision: _builtins.str, required: Optional[_builtins.bool] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeIdentifier")
    def type_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeRevision")
    def type_revision(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class AssetTypeTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainSingleSignOn(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: Optional[_builtins.str] = ..., user_assignment: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignment")
    def user_assignment(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class DomainTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentLastDeployment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_id: _builtins.str, deployment_status: _builtins.str, deployment_type: _builtins.str, failure_reasons: Sequence[outputs.EnvironmentLastDeploymentFailureReason], is_deployment_complete: _builtins.bool, messages: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(self) -> Sequence[outputs.EnvironmentLastDeploymentFailureReason]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeploymentComplete")
    def is_deployment_complete(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class EnvironmentLastDeploymentFailureReason(dict):
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class EnvironmentProfileUserParameter(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentProvisionedResource(dict):
    def __init__(__self__, *, name: _builtins.str, provider: _builtins.str, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnvironmentTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentUserParameter(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FormTypeImport(dict):
    def __init__(__self__, *, name: _builtins.str, revision: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FormTypeModel(dict):
    def __init__(__self__, *, smithy: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def smithy(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FormTypeTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GlossaryTermTermRelations(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, classifies: Optional[Sequence[_builtins.str]] = ..., is_as: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classifies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAs")
    def is_as(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class GlossaryTermTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectFailureReason(dict):
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ProjectTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserProfileDetail(dict):
    def __init__(__self__, *, iams: Sequence[outputs.UserProfileDetailIam], ssos: Sequence[outputs.UserProfileDetailSso]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iams(self) -> Sequence[outputs.UserProfileDetailIam]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssos(self) -> Sequence[outputs.UserProfileDetailSso]:
        ...
    


@pulumi.output_type
class UserProfileDetailIam(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class UserProfileDetailSso(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, first_name: _builtins.str, last_name: _builtins.str, user_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class UserProfileTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


