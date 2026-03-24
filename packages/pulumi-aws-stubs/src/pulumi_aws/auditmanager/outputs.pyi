

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssessmentAssessmentReportsDestination', 'AssessmentRole', 'AssessmentRolesAll', 'AssessmentScope', 'AssessmentScopeAwsAccount', 'AssessmentScopeAwsService', 'ControlControlMappingSource', 'ControlControlMappingSourceSourceKeyword', 'FrameworkControlSet', 'FrameworkControlSetControl', 'GetControlControlMappingSourceResult', 'GetControlControlMappingSourceSourceKeywordResult', 'GetFrameworkControlSetResult', 'GetFrameworkControlSetControlResult']
@pulumi.output_type
class AssessmentAssessmentReportsDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination: _builtins.str, destination_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentRole(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, role_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentRolesAll(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, role_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentScope(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_accounts: Optional[Sequence[outputs.AssessmentScopeAwsAccount]] = ..., aws_services: Optional[Sequence[outputs.AssessmentScopeAwsService]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccounts")
    def aws_accounts(self) -> Optional[Sequence[outputs.AssessmentScopeAwsAccount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsServices")
    def aws_services(self) -> Optional[Sequence[outputs.AssessmentScopeAwsService]]:
        
        ...
    


@pulumi.output_type
class AssessmentScopeAwsAccount(dict):
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AssessmentScopeAwsService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ControlControlMappingSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_name: _builtins.str, source_set_up_option: _builtins.str, source_type: _builtins.str, source_description: Optional[_builtins.str] = ..., source_frequency: Optional[_builtins.str] = ..., source_id: Optional[_builtins.str] = ..., source_keyword: Optional[outputs.ControlControlMappingSourceSourceKeyword] = ..., troubleshooting_text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetUpOption")
    def source_set_up_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDescription")
    def source_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFrequency")
    def source_frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKeyword")
    def source_keyword(self) -> Optional[outputs.ControlControlMappingSourceSourceKeyword]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="troubleshootingText")
    def troubleshooting_text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlControlMappingSourceSourceKeyword(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, keyword_input_type: _builtins.str, keyword_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keywordInputType")
    def keyword_input_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keywordValue")
    def keyword_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FrameworkControlSet(dict):
    def __init__(__self__, *, name: _builtins.str, controls: Optional[Sequence[outputs.FrameworkControlSetControl]] = ..., id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def controls(self) -> Optional[Sequence[outputs.FrameworkControlSetControl]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkControlSetControl(dict):
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlControlMappingSourceResult(dict):
    def __init__(__self__, *, source_description: _builtins.str, source_frequency: _builtins.str, source_id: _builtins.str, source_keywords: Sequence[outputs.GetControlControlMappingSourceSourceKeywordResult], source_name: _builtins.str, source_set_up_option: _builtins.str, source_type: _builtins.str, troubleshooting_text: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDescription")
    def source_description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFrequency")
    def source_frequency(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKeywords")
    def source_keywords(self) -> Sequence[outputs.GetControlControlMappingSourceSourceKeywordResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetUpOption")
    def source_set_up_option(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="troubleshootingText")
    def troubleshooting_text(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetControlControlMappingSourceSourceKeywordResult(dict):
    def __init__(__self__, *, keyword_input_type: _builtins.str, keyword_value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keywordInputType")
    def keyword_input_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keywordValue")
    def keyword_value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFrameworkControlSetResult(dict):
    def __init__(__self__, *, controls: Sequence[outputs.GetFrameworkControlSetControlResult], id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def controls(self) -> Sequence[outputs.GetFrameworkControlSetControlResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFrameworkControlSetControlResult(dict):
    def __init__(__self__, *, id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    


