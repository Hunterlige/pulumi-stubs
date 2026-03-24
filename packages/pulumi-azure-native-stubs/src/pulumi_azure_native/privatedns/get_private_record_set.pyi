

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateRecordSetResult', 'AwaitableGetPrivateRecordSetResult', 'get_private_record_set', 'get_private_record_set_output']
@pulumi.output_type
class GetPrivateRecordSetResult:
    
    def __init__(__self__, a_records=..., aaaa_records=..., azure_api_version=..., cname_record=..., etag=..., fqdn=..., id=..., is_auto_registered=..., metadata=..., mx_records=..., name=..., ptr_records=..., soa_record=..., srv_records=..., system_data=..., ttl=..., txt_records=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aRecords")
    def a_records(self) -> Optional[Sequence[outputs.ARecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aaaaRecords")
    def aaaa_records(self) -> Optional[Sequence[outputs.AaaaRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cnameRecord")
    def cname_record(self) -> Optional[outputs.CnameRecordResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoRegistered")
    def is_auto_registered(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mxRecords")
    def mx_records(self) -> Optional[Sequence[outputs.MxRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecords")
    def ptr_records(self) -> Optional[Sequence[outputs.PtrRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="soaRecord")
    def soa_record(self) -> Optional[outputs.SoaRecordResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="srvRecords")
    def srv_records(self) -> Optional[Sequence[outputs.SrvRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="txtRecords")
    def txt_records(self) -> Optional[Sequence[outputs.TxtRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateRecordSetResult(GetPrivateRecordSetResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateRecordSetResult]:
        ...
    


def get_private_record_set(private_zone_name: Optional[_builtins.str] = ..., record_type: Optional[_builtins.str] = ..., relative_record_set_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateRecordSetResult:
    
    ...

def get_private_record_set_output(private_zone_name: Optional[pulumi.Input[_builtins.str]] = ..., record_type: Optional[pulumi.Input[_builtins.str]] = ..., relative_record_set_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateRecordSetResult]:
    
    ...

