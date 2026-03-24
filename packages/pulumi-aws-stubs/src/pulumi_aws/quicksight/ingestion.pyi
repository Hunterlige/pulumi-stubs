

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IngestionArgs', 'Ingestion']
@pulumi.input_type
class IngestionArgs:
    def __init__(__self__, *, data_set_id: pulumi.Input[_builtins.str], ingestion_id: pulumi.Input[_builtins.str], ingestion_type: pulumi.Input[_builtins.str], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionId")
    def ingestion_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ingestion_id.setter
    def ingestion_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionType")
    def ingestion_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ingestion_type.setter
    def ingestion_type(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _IngestionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_status: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_set_id.setter
    def data_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionId")
    def ingestion_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingestion_id.setter
    def ingestion_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionStatus")
    def ingestion_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingestion_status.setter
    def ingestion_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionType")
    def ingestion_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingestion_type.setter
    def ingestion_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:quicksight/ingestion:Ingestion")
class Ingestion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IngestionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_id: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_status: Optional[pulumi.Input[_builtins.str]] = ..., ingestion_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Ingestion:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionId")
    def ingestion_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionStatus")
    def ingestion_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionType")
    def ingestion_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


