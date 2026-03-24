

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessCacheResult', 'AwaitableGetServerlessCacheResult', 'get_serverless_cache', 'get_serverless_cache_output']
@pulumi.output_type
class GetServerlessCacheResult:
    
    def __init__(__self__, arn=..., cache_usage_limits=..., create_time=..., daily_snapshot_time=..., description=..., endpoint=..., engine=..., full_engine_version=..., id=..., kms_key_id=..., major_engine_version=..., name=..., reader_endpoint=..., region=..., security_group_ids=..., snapshot_retention_limit=..., status=..., subnet_ids=..., user_group_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheUsageLimits")
    def cache_usage_limits(self) -> outputs.GetServerlessCacheCacheUsageLimitsResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySnapshotTime")
    def daily_snapshot_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> outputs.GetServerlessCacheEndpointResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullEngineVersion")
    def full_engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorEngineVersion")
    def major_engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> outputs.GetServerlessCacheReaderEndpointResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerlessCacheResult(GetServerlessCacheResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessCacheResult]:
        ...
    


def get_serverless_cache(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessCacheResult:
    
    ...

def get_serverless_cache_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessCacheResult]:
    
    ...

