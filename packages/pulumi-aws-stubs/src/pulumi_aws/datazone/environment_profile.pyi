

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
__all__ = ['EnvironmentProfileArgs', 'EnvironmentProfile']
@pulumi.input_type
class EnvironmentProfileArgs:
    def __init__(__self__, *, aws_account_region: pulumi.Input[_builtins.str], domain_identifier: pulumi.Input[_builtins.str], environment_blueprint_identifier: pulumi.Input[_builtins.str], project_identifier: pulumi.Input[_builtins.str], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aws_account_region.setter
    def aws_account_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_identifier.setter
    def project_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]]:
        
        ...
    
    @user_parameters.setter
    def user_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EnvironmentProfileState:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_region: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., environment_blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ..., user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_region.setter
    def aws_account_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_identifier.setter
    def project_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]]:
        
        ...
    
    @user_parameters.setter
    def user_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentProfileUserParameterArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:datazone/environmentProfile:EnvironmentProfile")
class EnvironmentProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_region: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., environment_blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EnvironmentProfileUserParameterArgs, EnvironmentProfileUserParameterArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EnvironmentProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_region: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., environment_blueprint_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ..., user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EnvironmentProfileUserParameterArgs, EnvironmentProfileUserParameterArgsDict]]]]] = ...) -> EnvironmentProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> pulumi.Output[_builtins.str]:
        
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
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> pulumi.Output[Optional[Sequence[outputs.EnvironmentProfileUserParameter]]]:
        
        ...
    


