

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HostingReleaseArgs', 'HostingRelease']
@pulumi.input_type
class HostingReleaseArgs:
    def __init__(__self__, *, site_id: pulumi.Input[_builtins.str], channel_id: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @site_id.setter
    def site_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _HostingReleaseState:
    def __init__(__self__, *, channel_id: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., release_id: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseId")
    def release_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_id.setter
    def release_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firebase/hostingRelease:HostingRelease")
class HostingRelease(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., channel_id: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HostingReleaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., channel_id: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., release_id: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ...) -> HostingRelease:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseId")
    def release_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


