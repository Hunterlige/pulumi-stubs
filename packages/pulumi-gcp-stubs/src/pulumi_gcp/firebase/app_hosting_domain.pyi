

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
__all__ = ['AppHostingDomainArgs', 'AppHostingDomain']
@pulumi.input_type
class AppHostingDomainArgs:
    def __init__(__self__, *, backend: pulumi.Input[_builtins.str], domain_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ..., serve: Optional[pulumi.Input[AppHostingDomainServeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backend.setter
    def backend(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_id.setter
    def domain_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def serve(self) -> Optional[pulumi.Input[AppHostingDomainServeArgs]]:
        
        ...
    
    @serve.setter
    def serve(self, value: Optional[pulumi.Input[AppHostingDomainServeArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AppHostingDomainState:
    def __init__(__self__, *, backend: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusArgs]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_time: Optional[pulumi.Input[_builtins.str]] = ..., serve: Optional[pulumi.Input[AppHostingDomainServeArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backend.setter
    def backend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainStatuses")
    def custom_domain_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusArgs]]]]:
        
        ...
    
    @custom_domain_statuses.setter
    def custom_domain_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purgeTime")
    def purge_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purge_time.setter
    def purge_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def serve(self) -> Optional[pulumi.Input[AppHostingDomainServeArgs]]:
        
        ...
    
    @serve.setter
    def serve(self, value: Optional[pulumi.Input[AppHostingDomainServeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firebase/appHostingDomain:AppHostingDomain")
class AppHostingDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backend: Optional[pulumi.Input[_builtins.str]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., serve: Optional[pulumi.Input[Union[AppHostingDomainServeArgs, AppHostingDomainServeArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppHostingDomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backend: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppHostingDomainCustomDomainStatusArgs, AppHostingDomainCustomDomainStatusArgsDict]]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_time: Optional[pulumi.Input[_builtins.str]] = ..., serve: Optional[pulumi.Input[Union[AppHostingDomainServeArgs, AppHostingDomainServeArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> AppHostingDomain:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backend(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainStatuses")
    def custom_domain_statuses(self) -> pulumi.Output[Sequence[outputs.AppHostingDomainCustomDomainStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purgeTime")
    def purge_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serve(self) -> pulumi.Output[Optional[outputs.AppHostingDomainServe]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


