

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssetIamPolicyArgs', 'AssetIamPolicy']
@pulumi.input_type
class AssetIamPolicyArgs:
    def __init__(__self__, *, asset: pulumi.Input[_builtins.str], dataplex_zone: pulumi.Input[_builtins.str], lake: pulumi.Input[_builtins.str], policy_data: pulumi.Input[_builtins.str], location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asset(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @asset.setter
    def asset(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataplex_zone.setter
    def dataplex_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lake.setter
    def lake(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AssetIamPolicyState:
    def __init__(__self__, *, asset: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @asset.setter
    def asset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataplex_zone.setter
    def dataplex_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lake.setter
    def lake(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataplex/assetIamPolicy:AssetIamPolicy")
class AssetIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., asset: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AssetIamPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., asset: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> AssetIamPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asset(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


