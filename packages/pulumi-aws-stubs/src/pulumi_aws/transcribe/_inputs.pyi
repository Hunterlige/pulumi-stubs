

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LanguageModelInputDataConfigArgs', 'LanguageModelInputDataConfigArgsDict']
class LanguageModelInputDataConfigArgsDict(TypedDict):
    data_access_role_arn: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    tuning_data_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LanguageModelInputDataConfigArgs:
    def __init__(__self__, *, data_access_role_arn: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], tuning_data_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tuningDataS3Uri")
    def tuning_data_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tuning_data_s3_uri.setter
    def tuning_data_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


