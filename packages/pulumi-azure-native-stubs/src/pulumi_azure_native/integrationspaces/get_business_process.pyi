

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBusinessProcessResult', 'AwaitableGetBusinessProcessResult', 'get_business_process', 'get_business_process_output']
@pulumi.output_type
class GetBusinessProcessResult:
    
    def __init__(__self__, azure_api_version=..., business_process_mapping=..., business_process_stages=..., description=..., id=..., identifier=..., name=..., provisioning_state=..., system_data=..., table_name=..., tracking_data_store_reference_name=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessProcessMapping")
    def business_process_mapping(self) -> Optional[Mapping[str, outputs.BusinessProcessMappingItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessProcessStages")
    def business_process_stages(self) -> Optional[Mapping[str, outputs.BusinessProcessStageResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[outputs.BusinessProcessIdentifierResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingDataStoreReferenceName")
    def tracking_data_store_reference_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBusinessProcessResult(GetBusinessProcessResult):
    def __await__(self): # -> Generator[Never, Any, GetBusinessProcessResult]:
        ...
    


def get_business_process(application_name: Optional[_builtins.str] = ..., business_process_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., space_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBusinessProcessResult:
    
    ...

def get_business_process_output(application_name: Optional[pulumi.Input[_builtins.str]] = ..., business_process_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., space_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBusinessProcessResult]:
    
    ...

