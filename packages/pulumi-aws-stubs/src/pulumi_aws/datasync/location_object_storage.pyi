

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LocationObjectStorageArgs', 'LocationObjectStorage']
@pulumi.input_type
class LocationObjectStorageArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], server_hostname: pulumi.Input[_builtins.str], access_key: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_key: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate: Optional[pulumi.Input[_builtins.str]] = ..., server_port: Optional[pulumi.Input[_builtins.int]] = ..., server_protocol: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_hostname.setter
    def server_hostname(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @agent_arns.setter
    def agent_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_certificate.setter
    def server_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @server_port.setter
    def server_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverProtocol")
    def server_protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_protocol.setter
    def server_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _LocationObjectStorageState:
    def __init__(__self__, *, access_key: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_key: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate: Optional[pulumi.Input[_builtins.str]] = ..., server_hostname: Optional[pulumi.Input[_builtins.str]] = ..., server_port: Optional[pulumi.Input[_builtins.int]] = ..., server_protocol: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @agent_arns.setter
    def agent_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_certificate.setter
    def server_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_hostname.setter
    def server_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @server_port.setter
    def server_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverProtocol")
    def server_protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_protocol.setter
    def server_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class LocationObjectStorage(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_key: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_key: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate: Optional[pulumi.Input[_builtins.str]] = ..., server_hostname: Optional[pulumi.Input[_builtins.str]] = ..., server_port: Optional[pulumi.Input[_builtins.int]] = ..., server_protocol: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LocationObjectStorageArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_key: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_key: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate: Optional[pulumi.Input[_builtins.str]] = ..., server_hostname: Optional[pulumi.Input[_builtins.str]] = ..., server_port: Optional[pulumi.Input[_builtins.int]] = ..., server_protocol: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> LocationObjectStorage:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverProtocol")
    def server_protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


