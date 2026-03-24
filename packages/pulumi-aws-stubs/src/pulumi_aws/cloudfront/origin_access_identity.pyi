

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OriginAccessIdentityArgs', 'OriginAccessIdentity']
@pulumi.input_type
class OriginAccessIdentityArgs:
    def __init__(__self__, *, comment: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OriginAccessIdentityState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., cloudfront_access_identity_path: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., iam_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_canonical_user_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @caller_reference.setter
    def caller_reference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontAccessIdentityPath")
    def cloudfront_access_identity_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudfront_access_identity_path.setter
    def cloudfront_access_identity_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamArn")
    def iam_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_arn.setter
    def iam_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_canonical_user_id.setter
    def s3_canonical_user_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OriginAccessIdentity(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[OriginAccessIdentityArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., cloudfront_access_identity_path: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., iam_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_canonical_user_id: Optional[pulumi.Input[_builtins.str]] = ...) -> OriginAccessIdentity:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontAccessIdentityPath")
    def cloudfront_access_identity_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamArn")
    def iam_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


